#!/usr/bin/env python3
"""Quick automated QC of a unit content file: every '## n.m' answer must have
Source/⚠, Conclusion, Memory trick; 'Differentiate' questions must contain a table."""
import re, sys
t = open(sys.argv[1], encoding="utf-8").read()
parts = re.split(r"\n## (?=\d+\.\d+ )", t)[1:]
ok = True
for p in parts:
    head = p.splitlines()[0]
    body = p.split("\n# ")[0]
    probs = []
    if "**Source:**" not in body: probs.append("no source")
    if "Source:** ⚠" not in body and "IR Sem7.pdf" not in body and "⚠" not in body: probs.append("no citation/flag")
    if "### Conclusion" not in body: probs.append("no conclusion")
    if "Memory trick" not in body and "Exam tip" not in body: probs.append("no memory trick")
    if re.search(r"difference|differentiate|compare|distinguish", head, re.I) and "\n|" not in body: probs.append("diff w/o table")
    words = len(re.sub(r"```.*?```", "", body, flags=re.S).split())
    print(f"{head[:70]:72s} words={words:4d} {'OK' if not probs else probs}")
    ok &= not probs
print("ANSWERS:", len(parts), "ALL OK" if ok else "PROBLEMS")
