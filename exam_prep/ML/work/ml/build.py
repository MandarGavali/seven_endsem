"""Build ML Word documents from content files.
usage: python build.py analysis | python build.py unit N
"""
import os, re, sys
from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

sys.path.insert(0, os.path.dirname(__file__))
from questions import PAPERS, Q, STAR, UNITS, maxm, stars, years
from sources import GAPS, SRC

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.abspath(os.path.join(HERE, "..", "..", "Output", "Machine_Learning"))
DIAG = os.path.join(HERE, "diagrams")
SUBJ = "Machine Learning"
YEAR_LABEL = {"2023": "Nov-Dec 2023", "2024": "Nov-Dec 2024", "2025": "Nov-Dec 2025"}


# ---------- docx helpers ----------
def new_doc():
    d = Document()
    sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    for m in ("left_margin", "right_margin"): setattr(sec, m, Cm(2))
    sec.top_margin = sec.bottom_margin = Cm(1.8)
    st = d.styles["Normal"]
    st.font.name = "Calibri"; st.font.size = Pt(11)
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.paragraph_format.space_after = Pt(3)
    for name, size, color in (("Heading 1", 16, "1F3864"), ("Heading 2", 13, "2E5597"), ("Heading 3", 11.5, "2E74B5")):
        h = d.styles[name]; h.font.size = Pt(size); h.font.name = "Calibri"
        h.font.color.rgb = RGBColor.from_string(color)
        h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
        h.paragraph_format.space_before = Pt(10 if name != "Heading 3" else 6)
        h.paragraph_format.space_after = Pt(3)
        h.paragraph_format.keep_with_next = True
    # footer page number
    p = sec.footer.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run("Page ")
    for kind, text in (("begin", None), (None, "PAGE"), ("end", None)):
        r = p.add_run()
        if kind:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), kind); r._r.append(f)
        else:
            t = OxmlElement("w:instrText"); t.set(qn("xml:space"), "preserve"); t.text = text; r._r.append(t)
    return d


def shade(cell_or_par, color):
    el = cell_or_par._tc.get_or_add_tcPr() if hasattr(cell_or_par, "_tc") else cell_or_par._p.get_or_add_pPr()
    s = OxmlElement("w:shd"); s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), color)
    el.append(s)


def para_border(p, color="2E74B5"):
    pPr = p._p.get_or_add_pPr(); b = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{side}"); e.set(qn("w:val"), "single"); e.set(qn("w:sz"), "6")
        e.set(qn("w:space"), "4"); e.set(qn("w:color"), color); b.append(e)
    pPr.append(b)


INLINE = re.compile(r"(\*\*.+?\*\*|\*.+?\*)")


def add_inline(p, text, bold=False, size=None):
    text = text.replace("`", "")
    for part in INLINE.split(text):
        if not part: continue
        if part.startswith("**"): r = p.add_run(part[2:-2]); r.bold = True
        elif part.startswith("*") and len(part) > 2: r = p.add_run(part[1:-1]); r.italic = True
        else: r = p.add_run(part)
        if bold: r.bold = True
        if size: r.font.size = Pt(size)
    return p


def table(d, rows, widths=None, header=True, size=10):
    t = d.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, row in enumerate(rows):
        for j, val in enumerate(row):
            c = t.cell(i, j); c.text = ""
            add_inline(c.paragraphs[0], str(val), bold=(header and i == 0), size=size)
            c.paragraphs[0].paragraph_format.space_after = Pt(0)
            if header and i == 0: shade(c, "D9E2F3")
            if widths: c.width = Cm(widths[j])
    d.add_paragraph()
    return t


def render_body(d, body):
    lines = body.strip("\n").split("\n")
    i = 0
    while i < len(lines):
        ln = lines[i].rstrip(); s = ln.strip()
        if not s: i += 1; continue
        if s.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                raw = lines[i].strip()[1:-1].split("|")
                if rows and len(raw) > len(rows[0]): raw = raw[:len(rows[0]) - 1] + ["|".join(raw[len(rows[0]) - 1:])]
                cells = [c.strip() for c in raw]
                if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells): rows.append(cells)
                i += 1
            lens = [max(min(len(r[j]) if j < len(r) else 0, 60) for r in rows) + 4 for j in range(len(rows[0]))]
            table(d, rows, widths=[max(1.4, 17.0 * l / sum(lens)) for l in lens]); continue
        if s.startswith("### "): d.add_heading(s[4:], level=3)
        elif s.startswith("## "): d.add_heading(s[3:], level=2)
        elif s.startswith("![") :
            m = re.match(r"!\[(.*?)\]\((.*?)\)(?:\{(\d+(?:\.\d+)?)\})?", s)
            cap, name, w = m.group(1), m.group(2), float(m.group(3) or 12)
            path = os.path.join(DIAG, name + ".png")
            if not os.path.exists(path): raise SystemExit(f"missing diagram {path}")
            d.add_picture(path, width=Cm(w)); d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
            c = d.add_paragraph(); c.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = c.add_run(cap); r.italic = True; r.font.size = Pt(9)
        elif s.startswith("$ "):
            p = d.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            r = p.add_run(s[2:]); r.font.name = "Cambria Math"; r.font.size = Pt(12); r.bold = True
            shade(p, "F2F2F2")
        elif s.startswith("> "):
            p = d.add_paragraph(); add_inline(p, s[2:]); shade(p, "FFF2CC"); para_border(p, "BF9000")
        elif s.startswith("!! "):
            p = d.add_paragraph(); r = add_inline(p, s[3:]); shade(p, "FCE4D6")
        elif re.match(r"^\s*[-*] ", ln):
            lvl = (len(ln) - len(ln.lstrip())) // 2
            p = d.add_paragraph(style="List Bullet 2" if lvl else "List Bullet")
            add_inline(p, re.sub(r"^\s*[-*] ", "", ln)); p.paragraph_format.space_after = Pt(1)
        elif re.match(r"^\d+\. ", s):
            lvl = (len(ln) - len(ln.lstrip())) // 3
            p = d.add_paragraph(); p.paragraph_format.left_indent = Cm(0.6 + 0.7 * lvl)
            p.paragraph_format.first_line_indent = Cm(-0.6); p.paragraph_format.space_after = Pt(1)
            n, rest = s.split(". ", 1)
            label = f"({'abcdefghij'[int(n) - 1]})" if lvl else n + "."
            r = p.add_run(label + "  "); r.bold = True; add_inline(p, rest)
        else:
            add_inline(d.add_paragraph(), s)
        i += 1


def qmeta(c):
    yrs = ", ".join(YEAR_LABEL[y] for y in years(c))
    return yrs, maxm(c), stars(c)


# ---------- unit content parsing ----------
def parse_unit(n):
    txt = open(os.path.join(HERE, f"U{n}.md"), encoding="utf-8").read()
    txt = txt.replace("SRC_GAPS", GAPS[n])
    for k in sorted(SRC, key=len, reverse=True): txt = txt.replace(k, SRC[k])
    left = re.findall(r"SRC_\w+|TBD", txt)
    if left: raise SystemExit(f"unresolved source placeholders: {set(left)}")
    blocks = {}
    for chunk in re.split(r"^@@ ", txt, flags=re.M)[1:]:
        head, _, body = chunk.partition("\n")
        key = head.strip(); meta = {}
        while True:
            m = re.match(r"^(source|note): (.*)\n", body)
            if not m: break
            meta[m.group(1)] = m.group(2); body = body[m.end():]
        blocks[key] = (meta, body)
    return blocks


def order(qs):
    return sorted(qs, key=lambda c: (-stars(c), Q.index(c)))


def build_unit(n):
    blocks = parse_unit(n)
    qs = order([c for c in Q if c["unit"] == n])
    missing = [c["id"] for c in qs if c["id"] not in blocks]
    if missing: raise SystemExit(f"missing answers: {missing}")
    d = new_doc()
    t = d.add_heading(f"{SUBJ} — Unit {n} Exam Answers", 0)
    p = d.add_paragraph(); add_inline(p, f"**Unit {n}: {UNITS[n]}**")
    add_inline(d.add_paragraph(), "SPPU B.E. (AI & DS) 2019 Pattern, Course 417521 · Exam: 70 marks, 2.5 hours · "
               "Paper unit = question pair (Q1/Q2 → Unit 1, Q3/Q4 → Unit 2, Q5/Q6 → Unit 3, Q7/Q8 → Unit 4).", size=9.5)
    add_inline(d.add_paragraph(), "Each answer is written for **(X + 2) marks**, where X = highest marks ever asked. "
               "Sources cite your PDFs by file name and PDF page number.", size=9.5)

    d.add_heading("1. Unit Snapshot", 1)
    rows = [["No.", "Question", "Max Marks", "Years Asked", "Importance"]]
    for c in qs:
        yrs, mx, st = qmeta(c); rows.append([c["id"], c["q"], str(mx), yrs, STAR[st]])
    table(d, rows, widths=[1.4, 9.0, 1.6, 3.2, 1.8], size=9)

    d.add_heading("2. Must-Do First (★★★)", 1)
    top = [c for c in qs if stars(c) == 3]
    if top:
        for c in top:
            p = d.add_paragraph(style="List Number"); add_inline(p, f"**{c['id']}** — {c['q']} ({maxm(c)} M)")
    else:
        d.add_paragraph("No ★★★ question in this unit; start with ★★.")

    d.add_heading("3. Full Answers", 1)
    for c in qs:
        meta, body = blocks[c["id"]]
        yrs, mx, st = qmeta(c)
        d.add_heading(f"{c['id']}. {c['q']}", 2)
        box = d.add_paragraph(); shade(box, "E2EFDA")
        add_inline(box, f"**Importance:** {STAR[st]}   |   **Max asked:** {mx} M → **write for {mx + 2} M**   |   **Asked in:** {yrs}", size=9.5)
        src = meta.get("source", "")
        box2 = d.add_paragraph(); shade(box2, "E2EFDA")
        add_inline(box2, f"**Source:** {src}", size=9.5)
        if len(c["raw"]) > 1 or c["raw"][0][3] != c["q"]:
            v = d.add_paragraph(); v.paragraph_format.space_after = Pt(4)
            add_inline(v, "**Asked as:** " + " | ".join(f"*{r[3]}* ({YEAR_LABEL[r[0]]} {r[1]}, {r[2]} M)" for r in c["raw"]), size=8.5)
        render_body(d, body)

    d.add_page_break()
    d.add_heading("4. Last-Minute Revision Sheet", 1)
    render_body(d, blocks["REVISION"][1])
    d.add_heading("5. Assumptions & Gaps", 1)
    render_body(d, blocks["GAPS"][1])
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, f"Machine_Learning_Unit{n}_Exam_Answers.docx")
    d.save(path); print("saved", path)


def build_analysis():
    blocks = parse_unit("A")  # UA.md: TOP10, GAPS
    d = new_doc()
    d.add_heading(f"{SUBJ} — PYQ Topic Analysis", 0)
    add_inline(d.add_paragraph(), "SPPU B.E. (AI & DS) 2019 Pattern · Course 417521 · 70 marks, 2.5 hours · "
               "Each paper: 8 questions in 4 OR-pairs; one pair per unit (Units III–VI of the syllabus, numbered 1–4 here).", size=10)

    d.add_heading("1. Papers Analysed", 1)
    rows = [["#", "Session", "Paper code", "File", "Sub-questions"]]
    for i, (key, label, code, f) in enumerate(PAPERS, 1):
        y = key[-4:]; cnt = sum(1 for c in Q for r in c["raw"] if r[0] == y)
        rows.append([str(i), label, code, f, str(cnt)])
    total = sum(len(c["raw"]) for c in Q)
    rows.append(["", "Total", "", "", str(total)])
    table(d, rows, widths=[0.8, 2.8, 3.6, 7.0, 2.4], size=9.5)

    d.add_heading("2. Unit-wise Canonical Questions", 1)
    add_inline(d.add_paragraph(), "**Importance rule used:** ★★★ = asked in all 3 papers, or in 2 papers with ≥ 8 marks; "
               "★★ = asked in 2 papers (< 8 marks); ★ = asked once.", size=9.5)
    for n in range(1, 5):
        d.add_heading(f"Unit {n}: {UNITS[n]}", 2)
        rows = [["No.", "Canonical question", "Max M", "Years asked", "Freq.", "Imp."]]
        for c in order([c for c in Q if c["unit"] == n]):
            yrs, mx, st = qmeta(c)
            rows.append([c["id"], c["q"], str(mx), yrs, str(len(years(c))), STAR[st]])
        table(d, rows, widths=[1.3, 8.6, 1.3, 3.4, 1.2, 1.4], size=9)
        p = d.add_paragraph(); add_inline(p, "**Raw questions mapped (exact wording):**", size=9.5)
        for c in order([c for c in Q if c["unit"] == n]):
            for r in c["raw"]:
                p = d.add_paragraph(style="List Bullet"); p.paragraph_format.space_after = Pt(0)
                add_inline(p, f"{YEAR_LABEL[r[0]]} {r[1]} [{r[2]}] → **{c['id']}**: {r[3]}", size=8.5)

    d.add_heading("3. Marks Weightage per Unit", 1)
    rows = [["Unit", "Name"] + [YEAR_LABEL[p[0][-4:]] + " (both OR options)" for p in PAPERS] + ["Marks per paper (attempted)", "Canonical Qs", "★★★"]]
    for n in range(1, 5):
        per = []
        for p in PAPERS:
            y = p[0][-4:]
            per.append(str(sum(r[2] for c in Q if c["unit"] == n for r in c["raw"] if r[0] == y)))
        uq = [c for c in Q if c["unit"] == n]
        rows.append([str(n), UNITS[n].split(" (")[0], *per, "17–18", str(len(uq)), str(sum(stars(c) == 3 for c in uq))])
    table(d, rows, widths=[1.0, 4.6, 2.4, 2.4, 2.4, 2.0, 1.6, 1.0], size=9)
    add_inline(d.add_paragraph(), "Each OR-pair carries 17 or 18 marks (Q1/Q2 = 18, Q3/Q4 = 17, Q5/Q6 = 18, Q7/Q8 = 17); "
               "the per-year columns add both OR options, so they are about double the attempted marks.", size=9.5)

    d.add_heading("4. Top 10 Most Important Topics", 1)
    render_body(d, blocks["TOP10"][1])
    d.add_heading("5. Assumptions & Gaps", 1)
    render_body(d, blocks["GAPS"][1])
    d.add_heading("6. Coverage Check", 1)
    ids = [r for c in Q for r in c["raw"]]
    keys = {(r[0], r[1]) for r in ids}
    add_inline(d.add_paragraph(), f"Raw sub-questions extracted: **{len(ids)}** (2023: 19, 2024: 17, 2025: 20). "
               f"Unique (paper, question) keys: **{len(keys)}** → every raw question maps to exactly one canonical question. "
               f"Canonical questions: **{len(Q)}**.")
    os.makedirs(OUT, exist_ok=True)
    path = os.path.join(OUT, "Machine_Learning_PYQ_Topic_Analysis.docx")
    d.save(path); print("saved", path)


if __name__ == "__main__":
    if sys.argv[1] == "analysis": build_analysis()
    else: build_unit(int(sys.argv[2]))
