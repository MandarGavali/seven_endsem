from blib import dg
A={}
# ---------- 2.3 NEAREST NEIGHBOUR SEARCH ----------
A['2.3']=dict(src="QAI-ii.pdf p.29–30 (quantum algorithms for nearest-neighbour search: Grover-based and amplitude-estimation-based, steps), p.23 (listing), p.26–27 (quantum distance measurement)",blocks=[
("def","**Nearest Neighbour Search (NNS)** finds the data point in a dataset closest to a given query point (basis of k-NN classification). **Quantum NNS** uses superposition and interference to examine all N points at once and **Grover-type amplitude amplification** to extract the nearest one in about **O(√N)** steps instead of O(N)."),
("h","1. Classical vs quantum"),
("b",["Classical: compute distance of the query to each of N points → O(N·d) time.","Quantum: all N distances are evaluated in superposition; Grover search finds the minimum → **quadratic speed-up** (QAI-ii.pdf p.29)."]),
("h","2. Steps (Grover-based NNS, QAI-ii.pdf p.29)"),
("n",["**Input:** dataset of N points {x₁…x_N} and query point q.","**Encode data:** index register |i⟩ in uniform superposition (1/√N) Σᵢ |i⟩|xᵢ⟩ (Hadamard + state preparation / amplitude encoding).",
"**Distance computation:** using quantum operations (e.g. swap test / inner-product circuit) compute dᵢ = D(xᵢ, q) in a register: Σᵢ |i⟩|dᵢ⟩.",
"**Oracle:** mark the index whose distance is smallest (below a threshold); the threshold is lowered each round (Dürr–Høyer minimum finding).","**Grover iterations:** amplify the amplitude of the marked point (≈ (π/4)√N times).","**Measure** → index of the nearest neighbour; verify classically."]),
("d",dg('a[label="Dataset x₁…x_N\\n+ query q"]; b[label="Encode: Σ|i⟩|xᵢ⟩\\n(superposition)"]; c[label="Compute distances\\nΣ|i⟩|dᵢ⟩ (swap test)"]; d[label="Oracle marks\\nsmallest distance",fillcolor="#FFF2CC"]; e[label="Grover amplification\\n≈ √N iterations",fillcolor="#E2EFDA"]; f[label="Measure → nearest\\nneighbour",shape=oval]; a->b->c->d->e->f; e->d[label="repeat",constraint=false];',"LR"),"Quantum nearest-neighbour search (Grover based)",6.3),
("p","**Explanation:** *Encode* loads every point simultaneously; *distance step* is done once for all points (parallelism); *oracle* flags the best; *Grover* boosts its probability; *measurement* returns it."),
("h","3. Small example"),
("t",["Point","Coordinates","Distance to q = (1,1)"],[["A","(0,0)","1.41"],["B","(1,2)","**1.00 (nearest)**"],["C","(4,1)","3.00"],["D","(5,5)","5.66"]],[1.0,1.5,2.5]),
("p","N = 4 points need 2 qubits for the index. Initial P(B) = 1/4; after **one** Grover iteration P(B) = 1 (exact for N = 4, M = 1) → measurement gives B. Classically 4 distance computations (worst case)."),
("h","4. Alternative: amplitude-estimation method (QAI-ii.pdf p.29–30)"),
("b",["Prepare a state containing all points + query; amplify the nearest-neighbour amplitude; use **amplitude estimation** to estimate it; measure to obtain the nearest point."]),
("h","5. Applications / limitations"),
("b",["k-NN classification, recommendation, image/pattern matching, clustering (quantum k-means uses the same distance routine).","Needs efficient **QRAM/state preparation**; speed-up quadratic; noise on current hardware."]),
("concl","Quantum NNS combines parallel distance evaluation with Grover amplification to find the closest point in O(√N) queries."),
("tip","**“Encode – Distance – Mark – Amplify – Measure.”** Say ‘quadratic speed-up’, not exponential."),
])
# ---------- 2.4 BOOSTING ----------
A['2.4']=dict(src="QAI-ii.pdf p.30–31 (quantum boosting: fundamental steps 1–6), p.23 (listing)",blocks=[
("def","**Boosting** combines many **weak learners** (slightly better than random) into one **strong learner** by re-weighting the training data. **Quantum boosting** uses quantum superposition/parallelism to evaluate and select weak learners faster (QAI-ii.pdf p.30)."),
("h","1. Steps of quantum boosting (book p.30–31)"),
("n",["**Weak learner selection:** choose a set of weak learners (decision stumps, small trees, small neural networks).","**Quantum data representation:** encode data into quantum states, using superposition for parallel processing.","**Quantum operations:** apply quantum gates/circuits to improve (evaluate) the weak learners.",
"**Measurement and weighting:** measure to get classical results; assign each weak learner a weight according to accuracy.","**Weighted combination:** combine weak learners' predictions into the first strong learner.","**Iterate:** repeat, re-emphasising examples that were mis-classified."]),
("d",dg('a[label="Training data\\n(equal weights)"]; b[label="Encode in\\nquantum states"]; c[label="Quantum search /\\nevaluate weak learners",fillcolor="#E2EFDA"]; d[label="Measure + weight\\nlearner (α)"]; e[label="Update example\\nweights"]; f[label="Strong learner\\nH(x)=sign(Σαₜhₜ(x))",shape=oval]; a->b->c->d->e->f; e->c[label="next round T",constraint=false];',"LR"),"Quantum boosting loop",6.3),
("h","2. Formulas (AdaBoost-style weighting)"),
("f",["Error of weak learner:  ε = Σ wᵢ · [hₜ(xᵢ) ≠ yᵢ]","Learner weight:  αₜ = ½ ln((1 − ε)/ε)","Example weights: wᵢ ← wᵢ · e^(αₜ) if misclassified (else e^(−αₜ)), then normalise","Final classifier:  H(x) = sign( Σₜ αₜ hₜ(x) )"]),
("p","Symbols: hₜ = weak learner in round t, wᵢ = weight of example i, αₜ = learner's vote strength."),
("h","3. Example (spam filter)"),
("b",["Round 1: stump “contains ‘free’” has ε = 0.3 → α₁ = ½ ln(0.7/0.3) = **0.42**.","Mis-classified e-mails get larger weights; Round 2 stump “many links” has ε = 0.25 → α₂ = 0.55.","Final H(x) = sign(0.42·h₁ + 0.55·h₂ + …) → accuracy higher than either stump alone.","**Quantum role:** the step ‘find the weak learner with lowest error among many’ is done with Grover-type search → fewer evaluations."]),
("h","4. Advantages / limitations"),
("b",["Potential speed-up in selecting learners and handling large feature sets; hybrid (quantum + classical).","Needs data loading (QRAM), noise-free qubits; mostly theoretical today."]),
("concl","Quantum boosting speeds up the weak-learner search and weighting of boosting using quantum parallelism, yielding a stronger classifier."),
("tip","**“Weak → Weigh → Combine → Repeat.”**"),
])
# ---------- 2.8 LINEAR ALGEBRA ----------
A['2.8']=dict(src="QAI-ii.pdf p.23–24 (4.3 Quantum algorithms for linear algebra: HHL algorithm, steps 1–6, complexity, quantum matrix multiplication)",blocks=[
("def","**Quantum algorithms for linear algebra** solve matrix–vector problems (linear systems, matrix multiplication, eigenvalues) faster than classical ones in certain cases. The most important is the **HHL algorithm** (Harrow–Hassidim–Lloyd, 2009) for solving **A x = b** (QAI-ii.pdf p.23)."),
("h","1. HHL algorithm"),
("b",["Problem: A is a Hermitian (sparse, well-conditioned) N×N matrix, b a vector; find x = A⁻¹b.","Provides **exponential speed-up** when A is sparse, has small condition number κ, and we only need a measurement result about x (not x itself)."]),
("h","2. Steps of HHL (book p.23–24)"),
("n",["**Amplitude encoding:** prepare |b⟩ whose amplitudes are the entries of b.","**Hamiltonian simulation:** construct e^(iAt) from A.","**Quantum Phase Estimation (QPE):** estimate eigenvalues λⱼ of A (eigen-decomposition |b⟩ = Σ βⱼ|uⱼ⟩).","**Ancilla rotation:** rotate an ancilla qubit by angle ∝ 1/λⱼ (conditioned on eigenvalue register).","**Inverse QPE:** un-compute the eigenvalue register.","**Measure** ancilla (post-select 1) → state |x⟩ ∝ Σ βⱼ λⱼ⁻¹ |uⱼ⟩ ; measure it to get properties of x."]),
("d",dg('a[label="|b⟩ encode\\n(amplitude encoding)"]; b[label="Hamiltonian\\ne^{iAt}"]; c[label="QPE\\n(eigenvalues λⱼ)",fillcolor="#E2EFDA"]; d[label="Ancilla rotation\\n∝ 1/λⱼ",fillcolor="#FFF2CC"]; e[label="Inverse QPE"]; f[label="Measure → |x⟩ = A⁻¹|b⟩",shape=oval]; a->b->c->d->e->f;',"LR"),"HHL algorithm block diagram",6.3),
("h","3. Complexity"),
("t",["Method","Complexity"],[["Classical (e.g. conjugate gradient)","O(N · κ)"],["HHL quantum","O(log N · κ²)  (polylog in N)"]],[3.0,3.0]),
("h","4. Other quantum linear-algebra algorithms"),
("b",["**Quantum matrix multiplication / inversion** – parallelism gives speed-up in special cases.","**Quantum PCA / SVD / eigenvalue estimation** – built on QPE (QAI-ii.pdf p.24).","**Used in ML:** regression, SVM training, recommendation, least squares."]),
("h","5. Limitations"),
("b",["Needs fast state preparation (QRAM) and read-out; answer is a quantum state (only samples/properties).","Dependence on κ and sparsity; large depth → needs fault tolerance."]),
("concl","HHL and related algorithms use QPE and amplitude encoding to solve linear systems in time polylogarithmic in size, enabling quantum machine learning."),
("tip","**“Encode – Simulate – Phase-estimate – Rotate – Un-estimate – Measure.”**"),
])
# ---------- 2.2 CLASSICAL vs QUANTUM SVM ----------
A['2.2']=dict(src="QAI-ii.pdf p.22 (QSVM overview), p.31–35 (QSVM: quantum states, U(θ), measurement, Qiskit example); classical SVM comparison from standard knowledge",
flag="Partly ⚠ not found: your book describes QSVM only; the point-by-point classical SVM comparison and complexity statements are from standard textbook knowledge.",blocks=[
("def","**Classical SVM** finds the maximum-margin hyperplane separating classes using (kernel) computations on a classical computer. **Quantum SVM (QSVM)** encodes data into quantum states (**quantum feature map**) and uses quantum operations/kernels to find the separating hyperplane (QAI-ii.pdf p.22, 31)."),
("t",["Point","Classical SVM","Quantum SVM"],[
["Data representation","Real vectors in R^d","Quantum states |φ(x)⟩ in Hilbert space (qubits)"],
["Feature space","Implicit via kernels (polynomial, RBF); limited dimension","**Exponentially large** Hilbert space via quantum feature maps (e.g. ZZ feature map)"],
["Kernel evaluation","Classical K(x,y), cost grows with data/dimension","Quantum kernel K = |⟨φ(x)|φ(y)⟩|² measured on a quantum circuit"],
["Training cost","≈ O(N²)–O(N³) for N samples","Proposed polylog(N·d) (least-squares QSVM via HHL) under assumptions"],
["Handling complex/non-linear data","Needs well-chosen kernel","Can use kernels hard to compute classically → potential better separation"],
["Hardware","Ordinary CPU/GPU, mature, stable","NISQ devices, noisy, few qubits"],
["Optimisation","Convex quadratic programming (global optimum)","Quantum circuit parameters U(θ) tuned (hybrid), or classical SVM on quantum kernel"],
["Accuracy / reliability","Deterministic, well understood","Probabilistic (shots), affected by noise"],
["Main advantage","Mature, scalable, interpretable","Potential speed-up and richer feature spaces"],
["Main limitation","Slow for huge data / expensive kernels","Data-loading cost, noise, speed-up unproven in practice"]],[1.5,2.6,2.7]),
("h","Advantages in brief"),
("b",["**Classical:** robust, convex, works today, interpretable.","**Quantum:** exponentially large feature space, possible exponential speed-up in training/kernel evaluation, quantum parallelism."]),
("concl","Classical SVM is practical and reliable today; QSVM promises speed-up and richer feature maps but is limited by noisy hardware and data loading."),
("tip","**“Classical = kernel trick; Quantum = quantum feature map in Hilbert space.”**"),
])
# ---------- 2.1 QSVM ----------
A['2.1']=dict(src="QAI-ii.pdf p.22 (overview), p.31–35 (QSVM: quantum states, margin, U(θ), measurement, Qiskit code and result on circle data)",blocks=[
("def","A **Quantum Support Vector Machine (QSVM)** is the quantum version of the SVM classifier: data points are represented as **quantum states (qubits)** and **quantum operations/kernels** are used to find the optimal **hyperplane** that separates classes with maximum margin (QAI-ii.pdf p.31)."),
("h","1. Working (book p.31–33)"),
("n",["**Data encoding:** map data x into a quantum state |ψ_in⟩ = |φ(x)⟩ with a **quantum feature map** (e.g. second-order expansion).","**Quantum operations:** apply a parameterised unitary |ψ_out⟩ = U(θ)|ψ_in⟩; parameters θ are optimised to **maximise the margin** between classes.","**Measurement and classification:** measure |ψ_out⟩ with operator M to get outcomes z; use z to classify new points.","**Classical optimiser** updates θ (or the quantum kernel is passed to a classical SVM solver)."]),
("d",dg('a[label="Classical data x"]; b[label="Quantum feature map\\n|φ(x)⟩"]; c[label="U(θ)\\n(parameterised circuit)",fillcolor="#E2EFDA"]; d[label="Measurement M\\n→ outcome z"]; e[label="Class label\\n(+1 / −1)",shape=oval]; f[label="Classical optimiser\\n(updates θ / margin)",fillcolor="#FFF2CC"]; a->b->c->d->e; d->f->c[constraint=false];',"LR"),"QSVM pipeline",6.3),
("h","2. Formulas"),
("f",["Hyperplane: w·φ(x) + b = 0 ;  margin = 2/‖w‖ (maximise)","Quantum kernel: K(x, y) = |⟨φ(x)|φ(y)⟩|²","Decision: ŷ = sign( Σᵢ αᵢ yᵢ K(xᵢ, x) + b )"]),
("p","Symbols: φ = feature map, w = normal of hyperplane, αᵢ = support-vector weights, yᵢ = true label."),
("h","3. Example (book p.32–34)"),
("b",["2-D points; class +1 if inside circle x² + y² < 0.5, else −1 (non-linearly separable).","Qiskit QSVM with a second-order feature map (depth 2), trained on 10 points, tested on the rest → predicted labels equal true labels, **accuracy 100 %** (book, simulator)."]),
("h","4. Advantages / limitations"),
("b",["Handles complex non-linear data via exponentially large feature space; potential speed-up.","Needs data loading, many shots; noise limits accuracy on today's devices."]),
("concl","QSVM maps data to quantum states, learns a maximum-margin separator with quantum circuits/kernels, and classifies by measurement."),
("tip","**“Encode – Rotate U(θ) – Measure – Classify.”**"),
])
# ---------- 2.5 VQA ----------
A['2.5']=dict(src="QAI-ii.pdf p.35–37 (variational quantum algorithms: parameterised circuit, classical optimiser, steps), p.15–16 (VQA case studies: job-shop scheduling, QAOA), p.20–21 (VQE, QAOA)",blocks=[
("def","**Variational Quantum Algorithms (VQAs)** are **hybrid quantum–classical** algorithms: a **parameterised quantum circuit (ansatz) U(θ)** prepares a state, a cost function is measured, and a **classical optimiser** updates θ iteratively to minimise the cost (QAI-ii.pdf p.35)."),
("h","1. Steps"),
("n",["**Choose an ansatz** – a parameterised circuit with parameters θ.","**Prepare the state** |ψ(θ)⟩ = U(θ)|0⟩ on the quantum computer.","**Measure** the expectation of the cost/objective: C(θ) = ⟨ψ(θ)|H|ψ(θ)⟩.","**Classical optimiser** (gradient descent, SPSA, COBYLA) proposes new θ.","**Repeat** until C(θ) converges; output best θ / solution."]),
("d",dg('a[label="Initial θ"]; b[label="Quantum computer:\\nprepare |ψ(θ)⟩=U(θ)|0⟩",fillcolor="#E2EFDA"]; c[label="Measure cost\\nC(θ)=⟨H⟩"]; d[label="Classical optimiser\\nupdate θ",fillcolor="#FFF2CC"]; e[label="Converged?\\nOutput solution",shape=diamond]; a->b->c->d->e; e->b[label="no"];',"LR"),"Hybrid loop of a variational quantum algorithm",6.3),
("h","2. Examples"),
("t",["Algorithm","Used for"],[["**VQE** (Variational Quantum Eigensolver)","Ground-state energy in chemistry"],["**QAOA** (Quantum Approximate Optimisation Algorithm)","Combinatorial optimisation: Max-Cut, graph partitioning, TSP, job-shop scheduling (book p.15–16)"],["**VQC** (Variational Quantum Classifier)","Classification / quantum neural networks"]],[2.8,4.0]),
("h","3. Advantages / challenges"),
("b",["Short circuits → suitable for noisy **NISQ** devices; flexible; classical part handles optimisation.","Challenges: **barren plateaus**, local minima, noise, many measurements."]),
("p","**Case study (book p.15–16):** QAOA applied to job-shop scheduling found solutions up to ~10 % better than classical heuristics with few qubits."),
("concl","VQAs split the work: quantum circuit evaluates the cost, classical optimiser tunes parameters – the leading approach on near-term quantum hardware."),
("tip","**“Ansatz – Measure – Optimise – Repeat.”**"),
])
# ---------- 2.6 QNN ----------
A['2.6']=dict(src="QAI-ii.pdf p.34–35 (quantum neural networks: encoding, quantum neurons, operations, measurement & learning; XOR example with Qiskit), p.20–23 (QNN overview)",blocks=[
("def","**Quantum Neural Networks (QNNs)** combine neural networks with quantum computing: data are **encoded in qubits**, **parameterised quantum gates act as neurons/weights**, and the network is trained by adjusting gate parameters (QAI-ii.pdf p.34)."),
("h","1. Components"),
("t",["Component","Role (classical analogue)"],[["Quantum encoding","Input vector → quantum state |ψ⟩ (input layer)"],["Quantum neurons","Quantum gates/circuits perform linear transformations (weighted sum)"],["Quantum operations","Layers of parameterised gates; parameters = weights"],["Measurement","Reads output as classical data (output layer, activation via measurement)"],["Learning","Classical optimiser (SPSA etc.) adjusts gate parameters to minimise loss"]],[1.8,5.0]),
("d",dg('a[label="Input x"]; b[label="Feature map\\n(encoding)"]; c[label="Variational layers\\nW(θ)",fillcolor="#E2EFDA"]; d[label="Measurement"]; e[label="Output ŷ"]; f[label="Loss + optimiser\\nupdate θ",fillcolor="#FFF2CC"]; a->b->c->d->e->f; f->c[label="θ",constraint=false];',"LR"),"Architecture of a quantum neural network (variational classifier)",6.3),
("h","2. Training steps"),
("n",["Encode data with a **feature map** (e.g. ZZFeatureMap).","Apply **ansatz** (RealAmplitudes) with parameters θ.","**Measure**, compute loss (squared error).","Optimiser updates θ; repeat until loss is minimal."]),
("h","3. Small example – XOR (book p.35)"),
("t",["x₁ x₂","00","01","10","11"],[["Target y","0","1","1","0"],["QNN output (after training)","0","1","1","0"]],[2.0,1.2,1.2,1.2,1.2]),
("p","The XOR problem is not linearly separable; the Qiskit QNN (ZZFeatureMap + RealAmplitudes + SPSA, 100 iterations) predicted all four labels correctly – **accuracy 100 %** on the training data."),
("h","4. Advantages / limitations"),
("b",["Exploits superposition/entanglement for rich, compact models; fewer parameters for some tasks.","Training is hard (barren plateaus), noise, limited qubits."]),
("concl","A QNN is a parameterised quantum circuit trained like a neural network, using qubits for data encoding and quantum gates as trainable layers."),
("tip","**“Encode – Entangle (layers) – Measure – Optimise.”**"),
])
# ---------- 2.7 CLASSIFICATION ----------
A['2.7']=dict(src="QAI-ii.pdf p.31–32 (quantum algorithms for classification: QSVM, QNN), p.22–23 (types of quantum-enhanced ML), p.34–35 (examples)",blocks=[
("def","**Classification** assigns labels to data from patterns learnt on labelled examples (spam / not spam, digit recognition). **Quantum ML classification** uses quantum states and circuits to do this potentially faster or with richer feature spaces (QAI-ii.pdf p.31)."),
("h","1. Quantum classification algorithms"),
("t",["Algorithm","Idea","Example"],[["**QSVM**","Quantum feature map + maximum-margin hyperplane","Circle data: inside = +1, outside = −1 (100 % in book example)"],["**QNN / VQC**","Parameterised circuit trained like a neural network","XOR problem, handwritten digits"],["**Quantum k-NN**","Grover/amplitude estimation to find nearest neighbours","Image/pattern matching"],["**Quantum boosting**","Combine weak quantum learners","Spam filtering"]],[1.4,3.0,2.4]),
("h","2. General workflow"),
("n",["**Encode** classical data into quantum states (basis / amplitude / feature-map encoding).","Apply **quantum circuit** (feature map + variational classifier or kernel).","**Measure** the output qubit(s).","**Classical post-processing / optimiser:** compare with labels, update parameters.","**Predict** labels for test data."]),
("d",dg('a[label="Labelled data"]; b[label="Quantum encoding"]; c[label="Quantum classifier\\n(QSVM / QNN circuit)",fillcolor="#E2EFDA"]; d[label="Measure"]; e[label="Predicted class"]; f[label="Compare with labels\\n→ update parameters",fillcolor="#FFF2CC"]; a->b->c->d->e; e->f->c[constraint=false];',"LR"),"Workflow of quantum classification",6.3),
("h","3. Examples"),
("b",["**Spam filtering:** e-mail features encoded in qubits; quantum classifier outputs spam / not spam.","**XOR:** QNN with ZZFeatureMap + RealAmplitudes classifies all 4 inputs correctly.","**Circle data:** QSVM separates inside / outside points of radius 0.5."]),
("h","4. Advantages / challenges"),
("b",["Large feature space, parallelism, potential speed-up.","Challenges: data loading, noise, limited qubits, hybrid workflows."]),
("concl","Quantum classification maps data into quantum states and uses quantum circuits (QSVM, QNN) to separate classes, with promised gains in speed and expressiveness."),
("tip","**“Encode – Circuit – Measure – Label.”** Always give one example (spam / XOR)."),
])
# ---------- 2.9 REGRESSION ----------
A['2.9']=dict(src="QAI-ii.pdf p.24–25 (quantum algorithms for regression: quantum linear regression steps, QSVR, QNN, kernel and variational regression)",blocks=[
("def","**Regression** predicts a continuous output y from inputs X by fitting a model (e.g. y = w·x + b). **Quantum regression** algorithms estimate the model parameters using quantum states and circuits, aiming at speed-up for large data (QAI-ii.pdf p.24)."),
("h","1. Quantum linear regression algorithm (book p.24–25)"),
("n",["**Data encoding:** encode data matrix X and target vector y into quantum states (amplitude encoding).","**Quantum feature map:** map data to a higher-dimensional quantum feature space.","**Quantum operations** (e.g. HHL-type linear-system solving) to estimate the weight vector w.","**Measurement** of the quantum state → estimate of w.","**Post-processing:** convert the results to classical weights ŵ."]),
("f",["Least squares:  w = (XᵀX)⁻¹ Xᵀ y   (quantum computer performs the matrix inversion)","Loss:  L(w) = Σ (yᵢ − w·xᵢ)²"]),
("p","Symbols: X = data matrix, y = target vector, w = weights, L = squared-error loss."),
("h","2. Example"),
("p","Data (x, y) = (1,2), (2,4), (3,6): Σxy = 28, Σx² = 14 → **w = 28/14 = 2**, so y = 2x; predict y(4) = 8. A quantum algorithm gives the same w but with the inversion step in polylog(N) time for very large data."),
("h","3. Types of quantum regression (book p.25)"),
("t",["Type","Idea"],[["Quantum Support Vector Regression","Quantum version of SVR – fits a function within an error tolerance, good for high-dimensional data"],["Quantum Neural Network regression","Parameterised circuits approximate complex functions"],["Quantum Kernel regression","Quantum circuits compute kernel functions for non-linear regression"],["Variational (hybrid) regression","Optimise model parameters with a classical optimiser; robust to noisy data"]],[2.4,4.4]),
("concl","Quantum regression encodes data in quantum states and estimates the weights with quantum linear-algebra routines, promising speed-up for large data sets."),
("tip","**“Encode – Feature-map – Invert (quantum) – Measure w.”**"),
])
REVISION=[
("h","Key definitions"),
("b",["**QML:** use of quantum states/circuits to speed up or enrich machine learning (hybrid quantum–classical).","**QSVM:** quantum feature map + maximum-margin hyperplane; kernel K = |⟨φ(x)|φ(y)⟩|².","**Quantum NNS:** Grover amplification over distances → O(√N).","**Quantum boosting:** weak learners + weights α = ½ ln((1−ε)/ε); quantum search picks learners.","**VQA:** ansatz U(θ) + measure cost + classical optimiser (VQE, QAOA, VQC).","**QNN:** encode → parameterised layers → measure → optimise.","**HHL:** solves Ax = b in O(log N κ²) vs classical O(Nκ).","**Regression:** w = (XᵀX)⁻¹Xᵀy with quantum matrix inversion."]),
("h","Formulas"),
("f",["Margin = 2/‖w‖ ; K(x,y) = |⟨φ(x)|φ(y)⟩|²","αₜ = ½ ln((1−ε)/ε) ; H(x) = sign(Σαₜhₜ(x))","C(θ) = ⟨ψ(θ)|H|ψ(θ)⟩","Grover: k ≈ (π/4)√N ; HHL: O(log N · κ²)"]),
("h","Memory tricks"),
("b",["**VQA = Ansatz-Measure-Optimise-Repeat.**","**HHL = Encode, Simulate, QPE, Rotate, un-QPE, Measure.**","NNS = **Encode-Distance-Mark-Amplify-Measure**.","Hybrid = quantum does the hard evaluation, **classical does the optimising**."]),
]
ASSUMPTIONS=[
"Unit 2 = Q3/Q4 of 2023–2025 (Quantum Machine Learning). Unit title is my label; syllabus not provided.",
"No lecture notes in the repo – book terminology (QAI-ii.pdf, scanned, read by OCR) was followed. Chapter 4 is a summary-style text; the Qiskit codes in the book use the old qiskit.aqua API, so only their ideas/results are quoted.",
"Q2.2 (Classical vs Quantum SVM) is only partly covered by your book (book describes QSVM only) – flagged ⚠; the classical-SVM side and complexity claims are from standard knowledge and are stated as ‘proposed/under assumptions’.",
"Quantum boosting formulas (AdaBoost weights) and the Dürr–Høyer minimum-finding step are standard background not stated in the book; the book's steps (p.30–31) are followed for the algorithm outline.",
"2.1 QSVM and 2.2 Classical-vs-Quantum SVM were kept separate (different wording/task) though the topic overlaps; learn 2.1 first.",
"Answer lengths follow (max marks + 2): NNS, Boosting, Linear algebra, SVM comparison = 11 marks; others = 8 marks.",
]
ANSWERS=A
