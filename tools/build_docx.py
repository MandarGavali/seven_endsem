#!/usr/bin/env python3
"""Build a .docx from a Markdown content file.
Usage: build_docx.py content.md out.docx
- ```dot name ... ``` blocks are rendered with Graphviz to PNG and embedded.
- Pandoc does the conversion; python-docx post-processes (borders, page numbers, fonts).
"""
import os, re, subprocess, sys, tempfile
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

src, out = sys.argv[1], sys.argv[2]
work = tempfile.mkdtemp()
text = open(src, encoding="utf-8").read()

def render_dot(m):
    name, body = m.group(1), m.group(2)
    dot = os.path.join(work, name + ".dot"); png = os.path.join(work, name + ".png")
    open(dot, "w").write(body)
    subprocess.run(["dot", "-Tpng", "-Gdpi=150", dot, "-o", png], check=True)
    # pick width: keep inside page
    from PIL import Image
    w, h = Image.open(png).size
    width_in = min(6.0, w / 150)
    if width_in * h / w > 4.2:  # too tall: cap height at 4.2 in
        width_in = 4.2 * (w / h)
    return f"\n![]({png}){{width={width_in:.2f}in}}\n"

text = re.sub(r"```dot (\S+)\n(.*?)```", render_dot, text, flags=re.S)

def render_mpl(m):
    """```mpl name ... ``` : matplotlib code; figure saved automatically."""
    name, body = m.group(1), m.group(2)
    png = os.path.join(work, name + ".png")
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    plt.close("all"); plt.rcParams.update({"font.size": 11})
    exec(body, {"plt": plt})
    plt.tight_layout(); plt.savefig(png, dpi=150); plt.close("all")
    from PIL import Image
    w, h = Image.open(png).size
    width_in = min(5.5, w / 150)
    if width_in * h / w > 4.2:
        width_in = 4.2 * (w / h)
    return f"\n![]({png}){{width={width_in:.2f}in}}\n"

text = re.sub(r"```mpl (\S+)\n(.*?)```", render_mpl, text, flags=re.S)
# '|' / \mid inside math -> U+01C0 (looks like a bar in Word AND LibreOffice; does not break pipe tables)
BAR = "\u01c0"
text = re.sub(r"(\$\$?)(.+?)(\1)", lambda m: m.group(1) + re.sub(r"\\mid\b ?|(?<!\\)\|", BAR, m.group(2)) + m.group(3), text, flags=re.S)
text = re.sub(r"\$\$\n(?=[-*] |\d+\. )", "$$\n\n", text)  # list right after display math
text = re.sub(r"(?m)^((?![-*] |\d+\. |\s|\||#|```).+)\n(?=[-*] |\d+\. )", r"\1\n\n", text)  # blank line before lists
md = os.path.join(work, "c.md"); open(md, "w", encoding="utf-8").write(text)
tmp = os.path.join(work, "t.docx")
subprocess.run(["pandoc", md, "-f", "markdown+pipe_tables+grid_tables", "-o", tmp], check=True)

d = Document(tmp)
# fonts
for sname in ["Normal", "Body Text", "First Paragraph", "Compact"]:
    try:
        st = d.styles[sname]; st.font.name = "Calibri"; st.font.size = Pt(11)
    except KeyError:
        pass
for lvl, size in [(1, 18), (2, 14), (3, 12)]:
    try:
        st = d.styles[f"Heading {lvl}"]; st.font.name = "Calibri"; st.font.size = Pt(size)
        st.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
    except KeyError:
        pass
# margins
for s in d.sections:
    s.left_margin = s.right_margin = Inches(0.9); s.top_margin = s.bottom_margin = Inches(0.8)
# table borders + header shading
def set_borders(tbl):
    tblPr = tbl._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{edge}")
        e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "6"); e.set(qn("w:color"), "555555")
        b.append(e)
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    tblPr.append(b)
    if tbl.rows:
        for c in tbl.rows[0].cells:
            tcPr = c._tc.get_or_add_tcPr()
            sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:fill"), "D9E2F3")
            tcPr.append(sh)
def fit_columns(tbl, total_in=6.7):
    ncol = len(tbl.columns)
    lens = [1] * ncol; longw = [1] * ncol
    for row in tbl.rows:
        for i, c in enumerate(row.cells[:ncol]):
            words = c.text.split()
            longw[i] = max(longw[i], max((len(w) for w in words), default=1))
            lens[i] = max(lens[i], min(len(c.text), 80))
    floors = [max(0.5, min(longw[i], 14) * 0.085 + 0.15) for i in range(ncol)]
    weights = [l ** 0.9 for l in lens]
    widths_in = floors[:]
    for _ in range(10):  # proportional share, respecting floors
        free = [i for i in range(ncol) if True]
        s_w = sum(weights)
        widths_in = [max(floors[i], total_in * weights[i] / s_w) for i in range(ncol)]
        excess = sum(widths_in) - total_in
        if excess <= 0.01:
            break
        big = [i for i in range(ncol) if widths_in[i] > floors[i] + 0.01]
        tot_big = sum(widths_in[i] for i in big)
        widths_in = [w - excess * w / tot_big if i in big else w for i, w in enumerate(widths_in)]
        break
    widths = [Inches(w) for w in widths_in]
    grid = tbl._tbl.tblGrid
    for gc, w in zip(grid.findall(qn("w:gridCol")), widths):
        gc.set(qn("w:w"), str(int(w.inches * 1440)))
    for row in tbl.rows:
        for i, c in enumerate(row.cells[:ncol]):
            c.width = widths[i]
    tblPr = tbl._tbl.tblPr
    for old in tblPr.findall(qn("w:tblW")):
        tblPr.remove(old)
    tw = OxmlElement("w:tblW"); tw.set(qn("w:w"), str(int(total_in * 1440))); tw.set(qn("w:type"), "dxa")
    tblPr.append(tw)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)

for t in d.tables:
    set_borders(t)
    fit_columns(t)
# page number footer
for s in d.sections:
    p = s.footer.paragraphs[0] if s.footer.paragraphs else s.footer.add_paragraph()
    p.alignment = 1
    r = p.add_run("Page ")
    for kind, txt in (("begin", None), (None, "PAGE"), ("end", None)):
        run = p.add_run()
        if kind:
            fc = OxmlElement("w:fldChar"); fc.set(qn("w:fldCharType"), kind); run._r.append(fc)
        else:
            it = OxmlElement("w:instrText"); it.set(qn("xml:space"), "preserve"); it.text = txt; run._r.append(it)
d.save(out)
print("built", out)
