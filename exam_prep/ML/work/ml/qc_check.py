import re, sys
from questions import Q, maxm
for n in (1, 2, 3, 4):
    txt = open(f"U{n}.md", encoding="utf-8").read()
    blocks = {c.split("\n", 1)[0].strip(): c for c in re.split(r"^@@ ", txt, flags=re.M)[1:]}
    for c in [c for c in Q if c["unit"] == n]:
        b = blocks.get(c["id"], "")
        words = len(re.sub(r"[|#*>$!\[\]()-]", " ", b).split())
        flags = []
        if "### Conclusion" not in b: flags.append("NO-CONCL")
        if not re.search(r"^> ", b, re.M): flags.append("NO-TIP")
        if "source:" not in b: flags.append("NO-SRC")
        if re.search(r"differentiate|compare", c["q"], re.I) and "\n|" not in b: flags.append("NO-TABLE")
        if "](" not in b: flags.append("no-diagram")
        print(f"{c['id']:6} max={maxm(c):2} write={maxm(c)+2:2} words={words:4} {' '.join(flags)}")
