import sys, re
# usage: find.py file kw1 [kw2...]  -> pages containing all keywords (case-insensitive, spaces ignored)
txt = open(sys.argv[1], encoding="utf-8").read()
pages = re.split(r"=== PAGE (\d+) ===", txt)
norm = lambda s: re.sub(r"\s+", "", s.lower())
kws = [norm(k) for k in sys.argv[2:]]
hits = []
for i in range(1, len(pages), 2):
    t = norm(pages[i + 1])
    if all(k in t for k in kws): hits.append(f"{pages[i]}({sum(t.count(k) for k in kws)})")
print(" ".join(hits))
