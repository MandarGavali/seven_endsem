import sys,importlib; sys.path.insert(0,'/home/user/seven_endsem/exam_prep/tools')
from blib import *; from qdata import *
C=build()
SRC={}
for u in range(1,5):
    M=importlib.import_module(f"unit{u}")
    for cid,a in M.A.items():
        f=a.get('flag') or ''
        SRC[cid]="⚠ Partly" if f.startswith('Partly') else ("⚠ Not in books" if f else "✔ In books")
d=new_doc("Quantum Artificial Intelligence — PYQ Topic Analysis")
d.add_heading("Quantum Artificial Intelligence (417523A) — PYQ Topic Analysis",0)
para(d,"B.E. (AI & DS) 2019 Pattern, Sem VII, Elective III  |  End-sem: 70 marks, 2.5 hrs, 4 units (solve Q1 or Q2, Q3 or Q4, Q5 or Q6, Q7 or Q8)",size=10,color='595959')
# 1
d.add_heading("1. Papers analysed",1)
table(d,["Paper","Type","Max marks","Raw questions (all sub-parts & OR)"],
 [[PAPERS[p].split(' (')[0],PAPERS[p].split('(')[1].rstrip(')'),"30" if p=="2022" else "70",sum(1 for r in R if r[0]==p)] for p in PAPERS]+[["**Total**","","",f"**{len(R)}**"]],[1.6,2.4,0.9,2.0])
cnt={s:sum(1 for v in C.values() if v['stars']==s) for s in (3,2,1)}
bullets(d,[f"**Coverage check:** {len(R)} raw questions = 12 + 24 + 16 + 24; each maps to exactly one of **{len(C)} canonical questions** (verified by script; every raw wording also appears in the unit answer files).",
f"**Importance:** ★★★ = {cnt[3]}, ★★ = {cnt[2]}, ★ = {cnt[1]}. Rule (4 papers): ★★★ = asked in ≥ 3 papers or repeatedly for 8+ marks; ★★ = 2 papers; ★ = once.",
"**Unit mapping:** Q1/Q2 → Unit 1, Q3/Q4 → Unit 2, Q5/Q6 → Unit 3, Q7/Q8 → Unit 4 (papers print no unit names).",
f"**Source coverage:** {sum(1 for x in SRC.values() if x.startswith('✔'))} of {len(C)} answers are fully backed by your books, {sum(1 for x in SRC.values() if 'Partly' in x)} partly, {sum(1 for x in SRC.values() if 'Not' in x)} not at all (standard-knowledge answers, flagged ⚠)."])
# 2
d.add_heading("2. Unit-wise list of ALL canonical questions",1)
for u in range(1,5):
    d.add_heading(f"Unit {u}: {UNITS[u]}",2)
    rows=[]
    for v in sorted([v for v in C.values() if v['unit']==u],key=lambda v:(-v['stars'],-v['X'],v['id'])):
        rows.append([v['id'],"**"+v['title']+"**\n"+"\n".join(f"• {r[0]} {r[1]} [{r[4]}]: “{r[3]}”" for r in v['raws']),v['X'],", ".join(v['years'])+(" (in-sem)" if v['insem_only'] else ""),len(v['years']),STAR[v['stars']],SRC[v['id']]])
    table(d,["No.","Canonical question + every variant wording","Max","Years asked","Freq.","Imp.","Source"],rows,[0.42,3.0,0.4,0.95,0.42,0.55,0.9],8.5)
# 3 matrix
d.add_page_break(); d.add_heading("3. Year-wise appearance matrix (marks shown)",1)
para(d,"Read across a row to see how often and for how many marks a topic was asked. Blank = not asked that year.",size=10)
rows=[]
for v in sorted(C.values(),key=lambda v:(v['unit'],-v['stars'],v['id'])):
    cells=[]
    for p in ("2022","2023","2024","2025"):
        rs=[r for r in v['raws'] if r[0]==p]
        cells.append(", ".join(f"{r[1]} [{r[4]}]" for r in rs))
    rows.append([v['id'],v['title'][:60]]+cells+[STAR[v['stars']]])
table(d,["No.","Topic","2022 (in-sem)","2023","2024","2025","Imp."],rows,[0.42,2.5,0.85,0.75,0.75,0.75,0.55],8)
# 4 weightage
d.add_heading("4. Marks weightage per unit",1)
rows=[]
for u in range(1,5):
    row=[f"Unit {u}"]
    for p in ("2023","2024","2025"):
        off=sum(r[4] for r in R if r[0]==p and r[2]==u); row.append(f"{off} offered / {round(off/2)} attempted")
    rows.append(row+[str(sum(1 for v in C.values() if v['unit']==u))])
table(d,["Unit","2023","2024","2025","Canonical Qs"],rows,[0.8,1.6,1.6,1.6,1.0])
para(d,"Each unit offers two alternatives and you answer one, so every unit carries **≈ 17–18 of the 70 marks**. Pattern change: 2023 and 2025 used three sub-questions of 5–6 marks per Q; **2024 used two sub-questions of 8–9 marks** – so every important topic must be prepared as a full 9-mark answer.")
# 5 slot pattern
d.add_heading("5. Slot pattern – which topics appear in which question",1)
rows=[]
for q in ("Q1","Q2","Q3","Q4","Q5","Q6","Q7","Q8"):
    row=[q]
    for p in ("2023","2024","2025"):
        rs=[r for r in R if r[0]==p and r[1].startswith(q)]
        row.append("\n".join(f"{r[1][-1]}) {C[r[5]]['title'].split(' (')[0]} [{r[4]}]" for r in rs))
    rows.append(row)
table(d,["Slot","2023","2024","2025"],rows,[0.5,2.1,2.1,2.1],8.5)
bullets(d,["**Unit 1:** Shor, Grover and Factoring appear every year; Deutsch/Simon/Phase kick-back fill the remaining slots.","**Unit 2:** Nearest-neighbour search every year; QSVM, boosting, VQA, QNN, classification and linear algebra rotate.","**Unit 3:** Dense coding and Quantum cryptography every year (often in Q6/Q5); teleportation 2024–25; three-bit code and fault tolerance as 5-mark short notes.","**Unit 4:** Quantum walk and Data-science challenges every year; tree search, production system, heuristic search, neural computation rotate.","**Strategy:** prepare all ★★★ + ★★ topics of a unit – that has always been enough to answer one complete alternative of each pair."])
# 6 top 10
d.add_heading("6. Top 10 most important topics",1)
top=sorted([v for v in C.values() if not v['insem_only']],key=lambda v:(-len(v['years']),-v['X'],-sum(r[4] for r in v['raws'])))[:10]
table(d,["#","Topic","Unit","Years","Max","Source","Why"],
 [[i+1,v['title'],v['unit'],", ".join(v['years']),v['X'],SRC[v['id']],"Every end-sem" if len([y for y in v['years'] if y!='2022'])==3 else "2 end-sems, 9 marks"] for i,v in enumerate(top)],[0.3,2.4,0.4,1.1,0.4,0.9,1.2],8.5)
para(d,"**High-probability for the next paper:** the ‘every end-sem’ topics above (Shor, Grover, Factoring, Nearest-neighbour search, Dense coding, Quantum cryptography, Data-science challenges, Quantum walk) plus Teleportation and Deutsch, which were asked for 9 marks.")
# 7
d.add_heading("7. Assumptions & gaps",1)
bullets(d,[
"**2022 paper is an In-sem** (30 marks, 1 hr, 2 units). Its 12 questions are analysed for completeness: 10 foundation items mapped to **Unit 1** (Q1.8–1.17), teleportation and mixed states mapped to **Unit 3**. Tagged ‘in-sem’ and rated ★.",
"2022 Q2b (‘Draw quantum circuits diagram that represents the operations’): the operations are not printed in the paper text; its only embedded image is a ‘SPPUQuestionPapers.com’ watermark. Standard circuits are drawn in the answer.",
"Unit names are my labels; no syllabus PDF was provided. No lecture notes exist for this subject; the two scanned textbooks (QAI.pdf 34 pp., QAI-ii.pdf 37 pp.) were read via OCR and cited by PDF page number.",
"**Not merged on purpose** (different tasks): 1.4 vs 1.5 (Deutsch analysis vs Deutsch–Jozsa comparison), 2.1 vs 2.2 (QSVM vs SVM-vs-QSVM), 3.7 vs 3.8 (noise models vs encoding challenges), 4.8 vs 1.2 (quantum search short note vs Grover).",
"**Corrections in this version:** Q1.8 (QAI.pdf p.7–8) and Q2.2 (QAI-ii.pdf p.36) were wrongly marked ‘not found’ earlier – both are in your books and are now cited. Textbook Shor example (N = 91) contains an arithmetic slip; verified examples are used.",
"**Gaps in your materials:** Unit 3 (except teleportation and mixed states) and most of Unit 4 are not covered by the two books. Unit 4 topics appear to follow A. Wichert, *Principles of Quantum Artificial Intelligence* (not in the repo). Answers for these are standard-knowledge answers, flagged ⚠ – verify Tarrataca's quantum production system and ‘Random Insect’ against class notes.",
"Marks ‘offered’ counts both OR-alternatives; ‘attempted’ is half."])
d.save('/home/user/seven_endsem/exam_prep/QAI/QAI_PYQ_Topic_Analysis.docx'); print("saved")
