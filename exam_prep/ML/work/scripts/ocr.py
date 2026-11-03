import sys, os, re, fitz, numpy as np, warnings
warnings.filterwarnings("ignore")
from rapidocr_onnxruntime import RapidOCR
eng = RapidOCR()
src, out = sys.argv[1], sys.argv[2]
done = len(re.findall(r"=== PAGE \d+ ===", open(out, encoding="utf-8").read())) if os.path.exists(out) else 0
d = fitz.open(src)
with open(out, "a", encoding="utf-8") as f:
    for i in range(done, d.page_count):
        pix = d[i].get_pixmap(dpi=150)
        img = np.frombuffer(pix.samples, np.uint8).reshape(pix.h, pix.w, pix.n)[:, :, :3]
        res, _ = eng(img)
        f.write(f"\n=== PAGE {i+1} ===\n" + ("\n".join(r[1] for r in res) + "\n" if res else ""))
        f.flush()
        print(i+1, flush=True)
