import re, subprocess, hashlib, os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
SCR="/tmp/claude-0/-home-user-seven-endsem/44ff7970-fe2a-534e-b1bc-198b0b780dca/scratchpad"
IMG=SCR+"/diagrams"; os.makedirs(IMG,exist_ok=True)
STAR={3:"★★★",2:"★★",1:"★"}
def new_doc():
    d=Document()
    s=d.sections[0]; s.left_margin=s.right_margin=Inches(0.9); s.top_margin=s.bottom_margin=Inches(0.8)
    st=d.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(11)
    st.element.rPr.rFonts.set(qn('w:eastAsia'),'Calibri')
    for n,sz,col in (('Heading 1',18,'1F3864'),('Heading 2',14,'2E74B5'),('Heading 3',12,'C55A11')):
        h=d.styles[n]; h.font.name='Calibri'; h.font.size=Pt(sz); h.font.bold=True; h.font.color.rgb=RGBColor.from_string(col)
        h.element.rPr.rFonts.set(qn('w:eastAsia'),'Calibri')
    # footer page number
    p=s.footer.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    r=p.add_run("Page "); 
    for t,txt in (("begin",None),("instr"," PAGE "),("end",None)):
        run=p.add_run(); 
        if t=="instr":
            e=OxmlElement('w:instrText'); e.set(qn('xml:space'),'preserve'); e.text=txt
        else:
            e=OxmlElement('w:fldChar'); e.set(qn('w:fldCharType'),t)
        run._r.append(e)
    return d
def rich(p,text,size=None,color=None):
    for part in re.split(r'(\*\*.+?\*\*|(?<![\w*])\*[^*\s][^*]*?\*(?![\w*]))',text):
        if not part: continue
        b=part.startswith('**') and part.endswith('**') and len(part)>4
        it=(not b) and part.startswith('*') and part.endswith('*') and len(part)>2
        r=p.add_run(part[2:-2] if b else (part[1:-1] if it else part)); r.bold=b; r.italic=it
        if size: r.font.size=Pt(size)
        if color: r.font.color.rgb=RGBColor.from_string(color)
    return p
def para(d,text,style=None,size=None,color=None,space=4,align=None):
    p=d.add_paragraph(style=style); rich(p,text,size,color); p.paragraph_format.space_after=Pt(space)
    if align: p.alignment=align
    return p
def bullets(d,items,style='List Bullet'):
    if style=='List Number':
        for i,it in enumerate(items,1):
            p=d.add_paragraph(); p.paragraph_format.left_indent=Inches(0.35); p.paragraph_format.first_line_indent=Inches(-0.25); p.paragraph_format.space_after=Pt(1)
            rich(p,f"{i}. "+it)
        return
    for it in items:
        p=d.add_paragraph(style=style); rich(p,it); p.paragraph_format.space_after=Pt(1)
def shade(cell,hexcol):
    tcPr=cell._tc.get_or_add_tcPr(); sh=OxmlElement('w:shd'); sh.set(qn('w:val'),'clear'); sh.set(qn('w:color'),'auto'); sh.set(qn('w:fill'),hexcol); tcPr.append(sh)
def table(d,header,rows,widths=None,size=10):
    t=d.add_table(rows=1,cols=len(header)); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER
    for i,h in enumerate(header):
        c=t.rows[0].cells[i]; c.text=''; rich(c.paragraphs[0],"**"+h+"**",size); shade(c,'D9E2F3')
    for row in rows:
        cells=t.add_row().cells
        for i,v in enumerate(row):
            cells[i].text=''; rich(cells[i].paragraphs[0],str(v),size)
    if widths:
        t.autofit=False
        for i,g in enumerate(t._tbl.tblGrid.findall(qn('w:gridCol'))): g.set(qn('w:w'),str(int(widths[i]*1440)))
        for row in t.rows:
            for i,w in enumerate(widths): row.cells[i].width=Inches(w)
    d.add_paragraph().paragraph_format.space_after=Pt(2)
    return t
def dot_png(dot,name=None):
    h=hashlib.md5(dot.encode()).hexdigest()[:10]; f=f"{IMG}/{h}.png"
    if not os.path.exists(f):
        r=subprocess.run(["dot","-Tpng","-Gdpi=150",f"-o{f}"],input=dot.encode(),capture_output=True)
        if r.returncode: raise RuntimeError(r.stderr.decode()+dot)
    return f
def diagram(d,dot,caption,width=5.2):
    f=dot_png(dot); d.add_picture(f,width=Inches(width))
    d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
    para(d,"*Fig.* "+caption if False else "Fig: "+caption,size=9,color='595959',align=WD_ALIGN_PARAGRAPH.CENTER)
def callout(d,label,text,fill):
    t=d.add_table(rows=1,cols=1); t.style='Table Grid'; c=t.rows[0].cells[0]; shade(c,fill); c.text=''
    rich(c.paragraphs[0],f"**{label}** "+text,10.5); d.add_paragraph().paragraph_format.space_after=Pt(2)
def render_blocks(d,blocks):
    for b in blocks:
        k=b[0]
        if k=="p": para(d,b[1])
        elif k=="h": d.add_heading(b[1],level=3)
        elif k=="b": bullets(d,b[1])
        elif k=="n": bullets(d,b[1],'List Number')
        elif k=="t": table(d,b[1],b[2],b[3] if len(b)>3 else None)
        elif k=="d": diagram(d,b[1],b[2],b[3] if len(b)>3 else 5.2)
        elif k=="f": 
            for line in b[1]:
                p=d.add_paragraph(); p.paragraph_format.left_indent=Inches(0.4); r=p.add_run(line); r.font.name='Cambria Math'; r.italic=True; p.paragraph_format.space_after=Pt(1)
        elif k=="i":
            d.add_picture(b[1],width=Inches(b[3] if len(b)>3 else 5.0)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER; para(d,"Fig: "+b[2],size=9,color='595959',align=WD_ALIGN_PARAGRAPH.CENTER)
        elif k=="code":
            for line in b[1]:
                p=d.add_paragraph(); p.paragraph_format.left_indent=Inches(0.3); p.paragraph_format.space_after=Pt(0); r=p.add_run(line); r.font.name='Consolas'; r.font.size=Pt(9)
            d.add_paragraph().paragraph_format.space_after=Pt(2)
        elif k=="def": callout(d,"Definition:",b[1],'E2EFDA')
        elif k=="concl": callout(d,"Conclusion:",b[1],'FFF2CC')
        elif k=="tip": callout(d,"💡 Memory trick / Exam tip:",b[1],'FCE4D6')
        else: raise ValueError(k)
def dg(nodes_edges,rankdir="LR",extra=""):
    return f'digraph G {{ rankdir={rankdir}; node [shape=box,style="rounded,filled",fillcolor="#EAF1FB",fontname="Helvetica",fontsize=11]; edge [fontname="Helvetica",fontsize=10]; {extra} {nodes_edges} }}'

# ---------- quantum circuit drawing (matplotlib) ----------
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Arc
def circuit_png(labels,ops,ncols=None,outs=None,title=None):
    key=hashlib.md5(repr((labels,ops,outs,title)).encode()).hexdigest()[:10]; f=f"{IMG}/c{key}.png"
    if os.path.exists(f): return f
    nq=len(labels); nc=ncols or (max(o[-1] for o in ops)+1)
    fig,ax=plt.subplots(figsize=(1.0*nc+1.8,0.75*nq+0.4)); ax.set_xlim(-1.3,nc+0.9); ax.set_ylim(-nq+0.4,0.6); ax.axis('off')
    y=lambda q:-q
    for q in range(nq):
        ax.plot([-0.4,nc-0.2],[y(q)]*2,color='k',lw=1,zorder=1); ax.text(-0.5,y(q),labels[q],ha='right',va='center',fontsize=11)
        if outs and outs[q]: ax.text(nc-0.1,y(q),outs[q],ha='left',va='center',fontsize=10)
    for o in ops:
        k=o[0]; col=o[-1]
        if k in("H","X","Y","Z","S","T","U","Uf","QFT","H⊗n","B"):
            q=o[1]; lab=o[2] if len(o)>3 else k; h=o[3] if False else 0.36
            span=o[4] if len(o)>5 else 1
            ax.add_patch(Rectangle((col-0.3,y(q)-h-(span-1)*1),0.6,2*h+(span-1)*1,fc='#EAF1FB',ec='k',zorder=3)); ax.text(col,y(q)-(span-1)*0.5,lab,ha='center',va='center',fontsize=10,zorder=4)
        elif k in("CX","CZ","CBOX"):
            c,t=o[1],o[2]; ax.plot([col,col],[y(c),y(t)],'k',lw=1,zorder=2); ax.add_patch(Circle((col,y(c)),0.07,fc='k',zorder=4))
            if k=="CX":
                ax.add_patch(Circle((col,y(t)),0.2,fc='w',ec='k',zorder=3)); ax.plot([col-0.2,col+0.2],[y(t)]*2,'k',lw=1,zorder=4); ax.plot([col,col],[y(t)-0.2,y(t)+0.2],'k',lw=1,zorder=4)
            elif k=="CZ": ax.add_patch(Circle((col,y(t)),0.07,fc='k',zorder=4))
            else: ax.add_patch(Rectangle((col-0.3,y(t)-0.34),0.6,0.68,fc='#EAF1FB',ec='k',zorder=3)); ax.text(col,y(t),o[3],ha='center',va='center',fontsize=10,zorder=4)
        elif k=="U2":
            a,b,lab=o[1],o[2],o[3]; ax.add_patch(Rectangle((col-0.35,y(b)-0.36),0.7,(b-a)+0.72,fc='#E2EFDA',ec='k',zorder=3)); ax.text(col,(y(a)+y(b))/2,lab,ha='center',va='center',fontsize=10,zorder=4)
        elif k=="M":
            q=o[1]; ax.add_patch(Rectangle((col-0.3,y(q)-0.34),0.6,0.68,fc='#FFF2CC',ec='k',zorder=3)); ax.add_patch(Arc((col,y(q)-0.1),0.4,0.36,theta1=0,theta2=180,zorder=4)); ax.plot([col,col+0.17],[y(q)-0.1,y(q)+0.15],'k',lw=1,zorder=4)
        elif k=="SWAP":
            a,b=o[1],o[2]; ax.plot([col,col],[y(a),y(b)],'k',lw=1,zorder=2)
            for q in (a,b): ax.plot([col-.15,col+.15],[y(q)-.15,y(q)+.15],'k',lw=1.5,zorder=4); ax.plot([col-.15,col+.15],[y(q)+.15,y(q)-.15],'k',lw=1.5,zorder=4)
        elif k=="BAR":
            ax.plot([col,col],[0.45,-nq+0.55],ls='--',color='gray',lw=0.8,zorder=0); 
            if len(o)>2 and o[1]: ax.text(col,0.52,o[1],ha='center',va='bottom',fontsize=8,color='gray')
    if title: ax.set_title(title,fontsize=10)
    fig.savefig(f,dpi=170,bbox_inches='tight'); plt.close(fig); return f
def circuit(d,labels,ops,caption,outs=None,width=5.4,ncols=None):
    f=circuit_png(labels,ops,ncols,outs); d.add_picture(f,width=Inches(width)); d.paragraphs[-1].alignment=WD_ALIGN_PARAGRAPH.CENTER
    para(d,"Fig: "+caption,size=9,color='595959',align=WD_ALIGN_PARAGRAPH.CENTER)
_old=render_blocks
def render_blocks(d,blocks):
    for b in blocks:
        if b[0]=="c": circuit(d,b[1],b[2],b[3],b[4] if len(b)>4 else None,b[5] if len(b)>5 else 5.4)
        else: _old(d,[b])
def smoke():
    d=new_doc(); circuit(d,["|0⟩","|0⟩"],[("H",0,"H",0),("CX",0,1,1),("M",0,2),("M",1,2)],"Bell",outs=["",""]); d.save("/tmp/claude-0/work/smoke.docx"); print("circuit ok")
