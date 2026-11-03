import sys,importlib,subprocess,os; sys.path.insert(0,os.path.dirname(__file__))
from qdata import build,R
from docx import Document
C=build(); u=int(sys.argv[1])
def wc(blocks):
    n=0
    for b in blocks:
        k=b[0]
        if k in("p","h","def","concl","tip"): n+=len(b[1].split())
        elif k in("b","n","f","code"): n+=sum(len(x.split()) for x in b[1])
        elif k=="t": n+=sum(len(str(c).split()) for r in b[2] for c in r)
    return n
T={5:200,7:300,8:350,10:450,11:450}
M=importlib.import_module(f"unit{u}"); bad=[]
for cid,a in M.A.items():
    v=C[cid]; w=wc(a['blocks']); kinds={b[0] for b in a['blocks']}
    nd=sum(1 for b in a['blocks'] if b[0] in('d','c','i'))
    probs=[]
    if w<0.9*T.get(v["ans"],150): probs.append(f"short({w}<{T[v['ans']]})")
    if 'concl' not in kinds: probs.append("no-concl")
    if 'tip' not in kinds: probs.append("no-tip")
    if not a.get('src'): probs.append("no-src")
    if v['ans']>=8 and nd==0 and 't' not in kinds: probs.append("no-diagram/table")
    if any(x in v['title'].lower() for x in("compare","differen","distingu")) and 't' not in kinds: probs.append("compare-without-table")
    print(f"{cid:5} ans={v['ans']:2} words={w:4} diag={nd} {' '.join(probs) or 'OK'}")
    if probs: bad.append(cid)
f=f"/home/user/seven_endsem/exam_prep/QAI/QAI_Unit{u}_Exam_Answers.docx"
d=Document(f); txt="\n".join(p.text for p in d.paragraphs)
miss=[f"{r[0]} {r[1]}" for r in R if r[2]==u and r[3] not in txt]
print("raw questions missing:",miss,"| images:",len(d.inline_shapes))
r=subprocess.run(["soffice","--headless","--convert-to","pdf",f,"--outdir","/tmp/claude-0/work"],capture_output=True)
pdf=f"/tmp/claude-0/work/QAI_Unit{u}_Exam_Answers.pdf"
print("pdf pages:",subprocess.run(["pdfinfo",pdf],capture_output=True,text=True).stdout.split("Pages:")[1].split()[0])
print("RESULT:","PASS" if not bad and not miss else f"FAIL {bad} {miss}")
