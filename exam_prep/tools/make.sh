#!/bin/bash
# make.sh <Name>  -> builds DMV/output/<Name>.docx and a PDF preview in DMV/output/pdf/
set -e
cd "$(dirname "$0")/../DMV"
python3 ../tools/build.py content/$1.md output/$1.docx
mkdir -p /tmp/claude-0/pdfprev
soffice --headless --convert-to pdf --outdir /tmp/claude-0/pdfprev output/$1.docx >/dev/null 2>&1
pdfinfo /tmp/claude-0/pdfprev/$1.pdf | grep Pages
