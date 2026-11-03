import sys, os, fitz
from docx2pdf import convert
src = sys.argv[1]; pages = [int(x) for x in sys.argv[2].split(",")]
out = os.path.join(os.path.dirname(__file__), "..", "qc")
pdf = os.path.join(out, os.path.basename(src).replace(".docx", ".pdf"))
convert(src, pdf)
d = fitz.open(pdf); print("pages:", d.page_count)
for p in pages:
    if p <= d.page_count:
        d[p - 1].get_pixmap(dpi=70).save(os.path.join(out, f"{os.path.basename(src)[:-5]}_p{p}.png"))
