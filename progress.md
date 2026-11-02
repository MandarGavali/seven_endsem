# Progress
Budget mode: this session processes Information Retrieval only.

- [x] Phase 0 inventory (inventory.md)
- [x] IR_PYQ_Topic_Analysis.docx (86 raw → 32 canonical; QC passed)
- [x] IR_Unit1_Exam_Answers.docx (10 answers; QC passed)
- [x] IR_Unit2_Exam_Answers.docx (9 answers; QC passed)
- [x] IR_Unit3_Exam_Answers.docx (8 answers incl. PageRank numerical; QC passed)
- [x] IR_Unit4_Exam_Answers.docx (5 answers; QC passed)

## Information Retrieval — DONE (5/5 documents)
Folder: `Exam_Prep/Information Retrieval/` (content/*.md = editable sources; rebuild with `tools/make.sh <name>`).
- PYQs analysed: 4 (N23, M24, N24, N25) · raw questions 86 · canonical 32 · ★★★ 19 · ★★ 2 · ★ 11
- ⚠ Not found in materials (standard answers): NLP challenges (1.5), NLP levels (1.6), n-gram problems (1.10), VSM part of 1.9,
  general Bayesian-network types (1.4, partial), interactive PRP (1.7, partial), contiguity hypothesis (2.8),
  Web challenges structure (3.3, partial), RS four phases (4.1), IR vs RS (4.3), RS evaluation metrics (4.4).

## Pending (later sessions — say "continue")
- Machine Learning: OCR `Textbooks/ML Textbook.pdf`, `Textbooks/ML Unit 3-6.pdf` → Topic Analysis → Units 1–4
- Data Modeling & Visualization: OCR `Textbooks/DMV Textbook.pdf` → Topic Analysis → Units 1–4
- Quantum AI: OCR `Textbooks/QAI.pdf`, `Textbooks/QAI-ii.pdf` → Topic Analysis → Units 1–4
Tools: `tools/build_docx.py` (md → docx, dot/mpl diagrams, borders, page numbers), `tools/qc.py`, `tools/make.sh`.
Setup needed in a fresh container: `apt-get install -y tesseract-ocr graphviz libreoffice-math` and `pip install matplotlib`.
