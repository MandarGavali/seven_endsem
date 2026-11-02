#!/bin/bash
# make.sh <name> [pages...]: build docx from content/<name>.md, convert to PDF, make preview strip of pages
cd "/home/user/seven_endsem/Exam_Prep/Information Retrieval"
S=/tmp/claude-0/-home-user-seven-endsem/58c7fa05-803d-53c5-a33a-f3e7f6709712/scratchpad/pdf; mkdir -p $S
n=$1; shift
python3 /home/user/seven_endsem/tools/build_docx.py content/$n.md $n.docx | tail -1
soffice --headless --convert-to pdf --outdir $S $n.docx >/dev/null 2>&1
echo "pages: $(pdfinfo $S/$n.pdf | awk '/Pages/{print $2}')"
rm -f $S/v-*.png
for p in "$@"; do pdftoppm -r 50 -png -f $p -l $p $S/$n.pdf $S/v; done
python3 -c "
from PIL import Image; import glob
ims=[Image.open(f) for f in sorted(glob.glob('$S/v-*.png'))]
if ims:
    w=sum(i.width for i in ims); h=max(i.height for i in ims); c=Image.new('RGB',(w,h),'white'); x=0
    for i in ims: c.paste(i,(x,0)); x+=i.width
    c.save('$S/strip.png')"
