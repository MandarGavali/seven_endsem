# Raw PYQ questions for Quantum Artificial Intelligence (417523A). Wording copied from the PDFs.
# (paper, qno, unit, text, marks, canon)
PAPERS = {"2022": "Nov/Dec 2022 (In-sem, 30 marks, 1 hr)", "2023": "Nov/Dec 2023 (End-sem, 70 marks)",
          "2024": "Nov/Dec 2024 (End-sem, 70 marks)", "2025": "Nov/Dec 2025 (End-sem, 70 marks)"}
R = [
# ---- 2022 in-sem ----
("2022","Q1a",1,"Describe the differences in measurement in bases and computational basis.",5,"1.8"),
("2022","Q1b",1,"Explain Single qubit and multiple qubit gates with diagram.",5,"1.9"),
("2022","Q1c",3,"Demonstrate quantum teleportation with suitable example.",5,"3.1"),
("2022","Q2a",1,"Describe Qubit copying circuit.",6,"1.10"),
("2022","Q2b",1,"Draw quantum circuits diagram that represents the operations.",6,"1.11"),
("2022","Q2c",1,"Describe how tensor product combines qubit states?",3,"1.12"),
("2022","Q3a",1,"Describe Time-Evolution of a Closed System.",5,"1.13"),
("2022","Q3b",1,"Describe role of quantum entanglement in quantum architecture.",5,"1.14"),
("2022","Q3c",3,"Explain Mixed States and General Quantum Operations.",5,"3.9"),
("2022","Q4a",1,"Describe hidden sub group problem for quantum Fourier transform.",5,"1.15"),
("2022","Q4b",1,"Explain universal sets of quantum gates.",5,"1.16"),
("2022","Q4c",1,"Compare order-finding and factoring for Fourier transform.",5,"1.17"),
# ---- 2023 ----
("2023","Q1a",1,"Describe Shor's Algorithm with example.",6,"1.1"),
("2023","Q1b",1,"Explain Simon's Algorithm.",6,"1.6"),
("2023","Q1c",1,"Explain Factoring Integers, with example.",6,"1.3"),
("2023","Q2a",1,"Describe Grover's Algorithm with example.",6,"1.2"),
("2023","Q2b",1,"Discuss analysis of Deutsch algorithm in details.",6,"1.4"),
("2023","Q2c",1,"Write a short note on: Phase Kick-Back.",6,"1.7"),
("2023","Q3a",2,"Explain in details quantum support vector machines.",6,"2.1"),
("2023","Q3b",2,"Explain Nearest Neighbour Search in detail.",6,"2.3"),
("2023","Q3c",2,"Explain in detail - Quantum Boosting.",6,"2.4"),
("2023","Q4a",2,"Write a short note on: Variational Quantum Algorithms.",6,"2.5"),
("2023","Q4b",2,"Explain Quantum Neural Networks.",6,"2.6"),
("2023","Q4c",2,"Describe classification in quantum machine learning with examples.",6,"2.7"),
("2023","Q5a",3,"What are some practical challenges and limitations associated with error model encoding in quantum computing.",6,"3.8"),
("2023","Q5b",3,"Describe Quantum Key Distribution in short.",6,"3.4"),
("2023","Q5c",3,"Discuss the Classical Three-Bit Code.",5,"3.5"),
("2023","Q6a",3,"Explain in short Quantum Dense Coding.",6,"3.2"),
("2023","Q6b",3,"Discuss in detail Quantum cryptography.",6,"3.3"),
("2023","Q6c",3,"Write a short Note on Fault Tolerance.",5,"3.6"),
("2023","Q7a",4,"Write short note on Quantum Walk.",6,"4.1"),
("2023","Q7b",4,"Explain Quantum Neural Computation.",6,"4.2"),
("2023","Q7c",4,"Write a short note on Quantum Tree Search.",5,"4.3"),
("2023","Q8a",4,"State the challenges and limitations are associated with quantum computing in data sciences.",6,"4.4"),
("2023","Q8b",4,"Explain Quantum Production System in detail.",6,"4.5"),
("2023","Q8c",4,"Describe the Heuristic Search with example.",5,"4.6"),
# ---- 2024 ----
("2024","Q1a",1,"Explain Quantum Part of the Shor's Algorithm.",9,"1.1"),
("2024","Q1b",1,"Describe Grover's Algorithm.",9,"1.2"),
("2024","Q2a",1,"Explain Factoring Integers, with example.",9,"1.3"),
("2024","Q2b",1,"Discuss analysis of Deutsch algorithm in details.",9,"1.4"),
("2024","Q3a",2,"Explain Nearest Neighbour Search in detail.",9,"2.3"),
("2024","Q3b",2,"Explain Quantum Algorithms for Linear Algebra.",9,"2.8"),
("2024","Q4a",2,"Identify the key differences between classical SVM and Quantum SVM in terms of their advantages?",9,"2.2"),
("2024","Q4b",2,"Explain quantum boosting with example.",9,"2.4"),
("2024","Q5a",3,"Explain Quantum Teleportation in detail.",9,"3.1"),
("2024","Q5b",3,"Describe Quantum cryptography and secure communication in detail.",8,"3.3"),
("2024","Q6a",3,"Explain in short Quantum Dense Coding.",9,"3.2"),
("2024","Q6b",3,"Explain Noise and error models in quantum systems.",8,"3.7"),
("2024","Q7a",4,"State the challenges and limitations are associated with quantum computing in data sciences.",9,"4.4"),
("2024","Q7b",4,"Describe Heuristic Search with example.",8,"4.6"),
("2024","Q8a",4,"Describe the Quantum Walk-Random Insect.",9,"4.1"),
("2024","Q8b",4,"Write a short note on Quantum Tree Search.",8,"4.3"),
# ---- 2025 ----
("2025","Q1a",1,"Discuss factoring integers with example.",6,"1.3"),
("2025","Q1b",1,"Describe Simon's algorithm with example.",6,"1.6"),
("2025","Q1c",1,"Compare Deutsch algorithm and Deutsch-Jozsa algorithm.",6,"1.5"),
("2025","Q2a",1,"Discuss the working of Shor's algorithm with its significance in breaking classical cryptosystems.",6,"1.1"),
("2025","Q2b",1,"Discuss how Grover's algorithm is used in searching in unsorted databases?",6,"1.2"),
("2025","Q2c",1,"Write a short note on Phase Kick-Back and its usage.",6,"1.7"),
("2025","Q3a",2,"Discuss regression with example.",6,"2.9"),
("2025","Q3b",2,"Write a note on variational quantum algorithms.",6,"2.5"),
("2025","Q3c",2,"Discuss quantum neural network in detail with small example.",6,"2.6"),
("2025","Q4a",2,"Describe quantum machine learning classification with appropriate example.",6,"2.7"),
("2025","Q4b",2,"Discuss quantum algorithms for linear algebra.",6,"2.8"),
("2025","Q4c",2,"Elaborate the steps for nearest neighbour search with example.",6,"2.3"),
("2025","Q5a",3,"Discuss in detail quantum cryptography.",6,"3.3"),
("2025","Q5b",3,"Write a short note on Fault Tolerance.",5,"3.6"),
("2025","Q5c",3,"Explain quantum dense coding.",6,"3.2"),
("2025","Q6a",3,"Discuss the concept of quantum teleportation and its significance in quantum communication.",6,"3.1"),
("2025","Q6b",3,"Describe with appropriate steps quantum key distribution process.",6,"3.4"),
("2025","Q6c",3,"Write a note on classical three bit code.",5,"3.5"),
("2025","Q7a",4,"Discuss penny lane a cross platform python library.",6,"4.7"),
("2025","Q7b",4,"Write a note on Quantum search.",5,"4.8"),
("2025","Q7c",4,"Elaborate tarrataca's quantum production system.",6,"4.5"),
("2025","Q8a",4,"Discuss quantum neural computations with its significance.",6,"4.2"),
("2025","Q8b",4,"Enlist and discuss challenges and limitations associated with quantum computing utilised in Data Science.",6,"4.4"),
("2025","Q8c",4,"Write a note on Quantum walk.",5,"4.1"),
]
UNITS = {1:"Quantum Algorithms (Shor, Grover, Deutsch, Simon, QFT) + in-sem foundations",
         2:"Quantum Machine Learning",
         3:"Quantum Communication, Cryptography and Error Correction",
         4:"Quantum Search, Quantum Walks and Quantum AI / Data Science"}
# canonical id -> (short title, canonical wording)
CANON = {
"1.1":"Shor's Algorithm (quantum part, example, significance in breaking cryptosystems)",
"1.2":"Grover's Algorithm (with example; searching unsorted databases)",
"1.3":"Factoring Integers, with example",
"1.4":"Analysis of Deutsch Algorithm",
"1.5":"Compare Deutsch algorithm and Deutsch-Jozsa algorithm",
"1.6":"Simon's Algorithm (with example)",
"1.7":"Phase Kick-Back (and its usage)",
"1.8":"Differences in measurement in bases and computational basis",
"1.9":"Single qubit and multiple qubit gates with diagram",
"1.10":"Qubit copying circuit",
"1.11":"Draw quantum circuit diagrams that represent the operations",
"1.12":"How tensor product combines qubit states",
"1.13":"Time-Evolution of a Closed System",
"1.14":"Role of quantum entanglement in quantum architecture",
"1.15":"Hidden subgroup problem for quantum Fourier transform",
"1.16":"Universal sets of quantum gates",
"1.17":"Compare order-finding and factoring for Fourier transform",
"2.1":"Quantum Support Vector Machines",
"2.2":"Classical SVM vs Quantum SVM (key differences / advantages)",
"2.3":"Nearest Neighbour Search (quantum, with steps and example)",
"2.4":"Quantum Boosting (with example)",
"2.5":"Variational Quantum Algorithms",
"2.6":"Quantum Neural Networks (with small example)",
"2.7":"Classification in Quantum Machine Learning (with examples)",
"2.8":"Quantum Algorithms for Linear Algebra",
"2.9":"Regression (quantum) with example",
"3.1":"Quantum Teleportation (with example; significance in quantum communication)",
"3.2":"Quantum Dense Coding",
"3.3":"Quantum Cryptography (and secure communication)",
"3.4":"Quantum Key Distribution (process / steps)",
"3.5":"Classical Three-Bit Code",
"3.6":"Fault Tolerance",
"3.7":"Noise and error models in quantum systems",
"3.8":"Practical challenges and limitations of error model encoding",
"3.9":"Mixed States and General Quantum Operations",
"4.1":"Quantum Walk (incl. Random Insect / short note)",
"4.2":"Quantum Neural Computation (and its significance)",
"4.3":"Quantum Tree Search",
"4.4":"Challenges and limitations of quantum computing in Data Science",
"4.5":"Quantum Production System (Tarrataca's)",
"4.6":"Heuristic Search with example",
"4.7":"PennyLane - cross-platform Python library",
"4.8":"Quantum Search",
}
def build():
    from collections import defaultdict
    c=defaultdict(list)
    for r in R: c[r[5]].append(r)
    out={}
    for cid,title in CANON.items():
        rs=c[cid]; yrs=sorted({r[0] for r in rs}); n=len(yrs); X=max(r[4] for r in rs)
        units={r[2] for r in rs}; assert len(units)==1,(cid,units); 
        hi=sum(1 for r in rs if r[4]>=8)
        stars=3 if (n>=3 or hi>=2) else (2 if n==2 else 1)
        out[cid]=dict(id=cid,title=title,unit=units.pop(),raws=rs,years=yrs,X=X,ans=X+2,stars=stars,insem_only=(yrs==["2022"]))
    return out
if __name__=="__main__":
    out=build(); used=sum(len(v['raws']) for v in out.values())
    assert used==len(R)==76, (used,len(R)); assert set(r[5] for r in R)<=set(CANON)
    from collections import Counter
    print("raw",len(R),"canon",len(out),Counter(v['stars'] for v in out.values()))
    for p in PAPERS: print(p, sum(1 for r in R if r[0]==p))
    for u in range(1,5): print(u, sum(1 for v in out.values() if v['unit']==u), "canon;", sum(len(v['raws']) for v in out.values() if v['unit']==u),"raw")
