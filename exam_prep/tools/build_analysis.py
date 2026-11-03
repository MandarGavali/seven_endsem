import sys; sys.path.insert(0,'/home/user/seven_endsem/exam_prep/tools')
from blib import *; from qdata import *
C=build(); d=new_doc()
d.add_heading("Quantum Artificial Intelligence (417523A) — PYQ Topic Analysis",0)
para(d,"B.E. (AI & DS) 2019 Pattern, Semester VII, Elective III  |  End-sem: 70 marks, 2.5 hrs, 4 units (solve Q1 or Q2, Q3 or Q4, Q5 or Q6, Q7 or Q8)",size=10,color='595959')
d.add_heading("1. Papers analysed",1)
table(d,["Paper","Type","Marks","Raw questions (incl. sub-parts & OR)"],
 [[PAPERS[p].split(' (')[0],PAPERS[p].split('(')[1].rstrip(')'),"30" if p=="2022" else "70",sum(1 for r in R if r[0]==p)] for p in PAPERS]+[["**Total**","","",f"**{len(R)}**"]],[1.6,2.4,0.8,2.0])
para(d,f"**Coverage check:** {len(R)} raw questions extracted = 12 + 24 + 16 + 24 (every sub-part a/b/c of every Q and every OR-alternative). Each raw question maps to exactly one of the **{len(C)} canonical questions** (verified by script). Unit mapping used: Q1/Q2 → Unit 1, Q3/Q4 → Unit 2, Q5/Q6 → Unit 3, Q7/Q8 → Unit 4.")
cnt={s:sum(1 for v in C.values() if v['stars']==s) for s in (3,2,1)}
para(d,f"**Importance summary:** ★★★ = {cnt[3]} questions, ★★ = {cnt[2]}, ★ = {cnt[1]}.  Rule used (4 papers analysed): ★★★ = asked in ≥3 papers (more than half) or asked for 8+ marks repeatedly; ★★ = 2 papers; ★ = once.")
d.add_heading("2. Unit-wise list of ALL canonical questions",1)
for u in range(1,5):
    d.add_heading(f"Unit {u}: {UNITS[u]}",2)
    rows=[]
    for v in sorted([v for v in C.values() if v['unit']==u],key=lambda v:(-v['stars'],-v['X'],v['id'])):
        rows.append([v['id'],"**"+v['title']+"**\n"+"; ".join(f"{r[0]} {r[1]}: “{r[3]}” [{r[4]}]" for r in v['raws']),v['X'],", ".join(v['years'])+(" (in-sem only)" if v['insem_only'] else ""),len(v['years']),STAR[v['stars']]])
    table(d,["No.","Canonical question + every variant wording asked","Max marks","Years asked","Freq.","Importance"],rows,[0.45,3.15,0.55,1.1,0.45,0.9],9)
d.add_heading("3. Marks weightage per unit",1)
rows=[]
for u in range(1,5):
    row=[f"Unit {u}"]
    for p in ("2023","2024","2025"):
        rs=[r for r in R if r[0]==p and r[2]==u]; off=sum(r[4] for r in rs); row.append(f"{off} offered / {round(off/2)} to attempt")
    rows.append(row)
table(d,["Unit","2023","2024","2025"],rows,[1.0,1.9,1.9,1.9])
para(d,"Each unit offers two alternatives (Q-or-Q); you answer one, so about **17–18 marks per unit** are scored (4 × ~17.5 = 70). Every unit is equally weighted, so skipping a unit is not an option — prepare at least the ★★★ and ★★ questions of ALL four units.")
d.add_heading("4. Top 10 most important topics",1)
top=sorted([v for v in C.values() if not v['insem_only']],key=lambda v:(-len(v['years']),-v['X'],-sum(r[4] for r in v['raws'])))[:10]
table(d,["#","Topic","Unit","Years asked","Max marks","Why it matters"],
 [[i+1,v['title'],v['unit'],", ".join(v['years']),v['X'],"Asked in every end-sem paper" if len(v['years'])==3 else "Asked in 2 end-sems; high marks"] for i,v in enumerate(top)],[0.3,2.8,0.45,1.2,0.6,1.5],9)
para(d,"**Strategy tip:** In every end-sem, each Q-or-Q pair has at least one question built from the ★★★/★★ list above. Learn all ten topics first, then the remaining ★★ topics, then ★ topics only if time permits. Because marks per sub-question jumped to 8–9 in 2024 (two sub-questions) versus 5–6 (three sub-questions) in 2023/2025, prepare each answer in a **short (5-6 mark) and long (9 mark)** version — the answer documents are written for (max marks + 2).")
d.add_heading("5. Assumptions & gaps",1)
bullets(d,[
"**2022 paper is an In-sem** (30 marks, 1 hr, only 2 units: Q1/Q2, Q3/Q4), not an end-sem. Its topics (qubits, gates, circuits, entanglement, hidden subgroup…) belong to the first half of the course. Assumption: all 12 questions are analysed for completeness; foundation/algorithm-prerequisite items were mapped to **Unit 1** (Q1.8–1.17), while **teleportation** and **mixed states / quantum operations** were mapped to **Unit 3** (they merge with end-sem topics 3.1 and fit the noise/communication theme). They are tagged “in-sem only” and rated ★ (asked once); marks as printed (out of 30).",
"The papers do not print unit names; units were inferred from the question-pair pattern (Q1/2, Q3/4, Q5/6, Q7/8) and topic content. No syllabus PDF was provided, so unit titles are my own labels.",
"**Not merged on purpose** (different wording/task): 1.4 Deutsch analysis vs 1.5 Deutsch vs Deutsch-Jozsa (comparison); 2.1 QSVM vs 2.2 Classical-vs-Quantum SVM; 3.7 Noise & error models vs 3.8 Challenges of error-model encoding. The answer documents cross-reference them, so learning one largely covers the other.",
"2025 Q7b “Quantum search” (5 marks) is treated as a distinct short-note topic (4.8); it overlaps with Grover (1.2).",
"2022 Q2b “Draw quantum circuits diagram that represents the operations” refers to operations that are not stated in the extracted paper text (figure missing). Assumption: the standard circuits for common operations (Bell-state creation, CNOT, swap, measurement) are expected.",
"Marks “offered” in Section 3 count all questions in the paper (both OR alternatives); “to attempt” is half of that.",
"No lecture notes were found in the repo for this subject. The two scanned textbooks (QAI.pdf, QAI-ii.pdf) were OCR'd; OCR errors in formulas were corrected from standard knowledge. See the unit answer files for per-topic source citations and ⚠ flags."])
d.save('/home/user/seven_endsem/exam_prep/QAI/QAI_PYQ_Topic_Analysis.docx')
print("saved; top10:",[v['id'] for v in top])
