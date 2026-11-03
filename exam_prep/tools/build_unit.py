import sys,importlib; sys.path.insert(0,'/home/user/seven_endsem/exam_prep/tools')
from blib import *; from qdata import *
def build_unit(n):
    C=build(); M=importlib.import_module(f"unit{n}"); A=M.ANSWERS
    vs=sorted([v for v in C.values() if v['unit']==n],key=lambda v:(-v['stars'],-v['X'],v['id']))
    missing=[v['id'] for v in vs if v['id'] not in A]; assert not missing,("missing answers",missing)
    d=new_doc(f"Quantum Artificial Intelligence — Unit {n} Exam Answers")
    d.add_heading(f"Quantum Artificial Intelligence — Unit {n}: {UNITS[n]}",0)
    para(d,"Exam answers for 70-mark end-sem (2.5 hrs). Each answer is written for (max marks asked + 2). Sources are PDF page numbers of the files in your repo; ⚠ marks content NOT found in your materials.",size=10,color='595959')
    d.add_heading("1. Unit snapshot",1)
    table(d,["No.","Question","Max Marks","Years Asked","Importance"],[[v['id'],v['title'],v['X'],", ".join(v['years'])+(" (in-sem)" if v['insem_only'] else ""),STAR[v['stars']]] for v in vs],[0.5,3.4,0.7,1.5,0.8],9.5)
    d.add_heading("2. Must-do first (★★★)",1)
    m3=[v for v in vs if v['stars']==3]
    if m3: bullets(d,[f"**Q{v['id']}** {v['title']} — max {v['X']} marks, asked {', '.join(v['years'])}" for v in m3],'List Number')
    else: para(d,"No ★★★ question in this unit. Start with the ★★ questions (asked in 2 papers) listed first in Section 3.")
    d.add_page_break(); d.add_heading("3. Full answers (★★★ → ★★ → ★)",1)
    for v in vs:
        a=A[v['id']]
        d.add_heading(f"Q{v['id']}. {v['title']}",2)
        flag=a.get('flag')
        table(d,["Importance","Max marks asked","Answer written for","Asked in","Source"],[[STAR[v['stars']],v['X'],f"{v['ans']} marks","; ".join(f"{r[0]} {r[1]}" for r in v['raws']),a['src']]],[0.8,0.8,0.9,1.9,2.5],9)
        para(d,"**Question wording(s) asked:** "+" | ".join(f"{r[0]} {r[1]} [{r[4]}]: “{r[3]}”" for r in v['raws']),size=9.5,color='404040')
        if flag: callout(d,"Source status:",flag,'F8CBAD')
        if a.get('note'): callout(d,"Note:",a['note'],'DDEBF7')
        render_blocks(d,a['blocks'])
        d.add_page_break()
    d.add_heading("4. Last-minute revision sheet",1)
    render_blocks(d,M.REVISION)
    d.add_page_break()
    d.add_heading("5. Assumptions & gaps",1)
    bullets(d,M.ASSUMPTIONS)
    nf=[f"Q{v['id']} {v['title']}"+(" (partly)" if A[v['id']]['flag'].startswith('Partly') else '') for v in vs if A[v['id']].get('flag')]
    para(d,"**Questions flagged ⚠ (not found in your materials): **"+("; ".join(nf) if nf else "none"))
    out=f"/home/user/seven_endsem/exam_prep/QAI/QAI_Unit{n}_Exam_Answers.docx"; d.save(out); print("saved",out,"flagged:",nf)
if __name__=="__main__": build_unit(int(sys.argv[1]))
