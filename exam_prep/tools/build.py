#!/usr/bin/env python3
"""Build a .docx from a Markdown content file.

Usage: build.py <content.md> <output.docx>

- Renders every diagrams/*.dot (next to the content dir) to PNG via Graphviz (only if stale).
- Converts Markdown -> DOCX with pandoc.
- Post-processes with python-docx: borders on all tables, page numbers in footer,
  readable font, image width capped to page.
"""
import pathlib
import subprocess
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Inches, RGBColor


def render_diagrams(diag_dir: pathlib.Path):
    for dot in sorted(diag_dir.glob("*.dot")):
        png = dot.with_suffix(".png")
        if not png.exists() or png.stat().st_mtime < dot.stat().st_mtime:
            subprocess.run(["dot", "-Tpng", "-Gdpi=150", str(dot), "-o", str(png)], check=True)


def set_borders(table):
    tbl = table._tbl
    tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "6")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "555555")
        borders.append(el)
    for old in tblPr.findall(qn("w:tblBorders")):
        tblPr.remove(old)
    tblPr.append(borders)
    # header row shading + bold
    if table.rows:
        for cell in table.rows[0].cells:
            tcPr = cell._tc.get_or_add_tcPr()
            shd = OxmlElement("w:shd")
            shd.set(qn("w:val"), "clear")
            shd.set(qn("w:color"), "auto")
            shd.set(qn("w:fill"), "D9E2F3")
            tcPr.append(shd)
            for p in cell.paragraphs:
                for r in p.runs:
                    r.bold = True


def size_columns(table, total_in=6.7):
    """Give each column a width proportional to its (capped) longest text."""
    ncol = len(table.columns)
    weights = [4] * ncol
    for row in table.rows:
        for i, cell in enumerate(row.cells[:ncol]):
            txt = cell.text.strip()
            n = len(txt)
            longest_word = max((len(w) for w in txt.split()), default=0)
            weights[i] = max(weights[i], min(n, 55), longest_word + 3, 8)
    total = sum(weights)
    widths = [Inches(total_in * w / total) for w in weights]
    tblPr = table._tbl.tblPr
    for old in tblPr.findall(qn("w:tblW")):
        tblPr.remove(old)
    tblW = OxmlElement("w:tblW")
    tblW.set(qn("w:w"), str(int(total_in * 1440)))
    tblW.set(qn("w:type"), "dxa")
    tblPr.append(tblW)
    grid = table._tbl.tblGrid
    for i, gc in enumerate(grid.findall(qn("w:gridCol"))):
        if i < ncol:
            gc.set(qn("w:w"), str(int(widths[i].inches * 1440)))
    for row in table.rows:
        for i, cell in enumerate(row.cells[:ncol]):
            cell.width = widths[i]


def add_page_number(section):
    footer = section.footer
    p = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run("Page ")
    for kind, text in (("begin", None), (None, "PAGE"), ("end", None)):
        r = p.add_run()
        if kind:
            fc = OxmlElement("w:fldChar")
            fc.set(qn("w:fldCharType"), kind)
            r._r.append(fc)
        else:
            it = OxmlElement("w:instrText")
            it.set(qn("xml:space"), "preserve")
            it.text = text
            r._r.append(it)


def postprocess(path: pathlib.Path):
    doc = Document(str(path))
    styles = doc.styles
    for name in ("Normal", "Body Text", "First Paragraph", "Compact"):
        if name in [s.name for s in styles]:
            st = styles[name]
            st.font.name = "Calibri"
            st.font.size = Pt(11)
            st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    for lvl, size in ((1, 18), (2, 14), (3, 12)):
        try:
            st = styles[f"Heading {lvl}"]
            st.font.name = "Calibri"
            st.font.size = Pt(size)
            st.font.color.rgb = RGBColor(0x1F, 0x3A, 0x68)
        except KeyError:
            pass
    for t in doc.tables:
        set_borders(t)
        size_columns(t)
    for s in doc.sections:
        s.left_margin = s.right_margin = Inches(0.9)
        s.top_margin = s.bottom_margin = Inches(0.8)
        add_page_number(s)
    # cap image widths
    max_w = Inches(6.2)
    for shape in doc.inline_shapes:
        if shape.width > max_w:
            ratio = max_w / shape.width
            shape.width = int(shape.width * ratio)
            shape.height = int(shape.height * ratio)
    doc.save(str(path))


def main():
    src = pathlib.Path(sys.argv[1]).resolve()
    out = pathlib.Path(sys.argv[2]).resolve()
    base = src.parent.parent
    render_diagrams(base / "diagrams")
    subprocess.run(
        ["pandoc", str(src), "-f", "markdown+pipe_tables+grid_tables", "-o", str(out),
         "--resource-path", f"{src.parent}:{base}"],
        check=True,
    )
    postprocess(out)
    print("built", out.name)


if __name__ == "__main__":
    main()
