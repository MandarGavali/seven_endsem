from blib import dg
SCR="/tmp/claude-0/-home-user-seven-endsem/44ff7970-fe2a-534e-b1bc-198b0b780dca/scratchpad"
A={}
NF="⚠ Not found in your materials. Standard textbook answer."
# ---------- 4.1 QUANTUM WALK ----------
A['4.1']=dict(src="Not in your materials (quantum walk appears only inside a question list, QAI-ii.pdf p.37)",
flag=NF+" Interpretation: ‘Random Insect’ (2024 Q8a) is read as the classical random walk of an insect/drunkard on a line, compared with its quantum version.",blocks=[
("def","A **quantum walk** is the quantum analogue of a classical **random walk**: instead of a particle moving left/right by a coin toss, the walker has a **quantum coin** and is in a **superposition of positions**, so different paths **interfere**. This makes it spread **quadratically faster** and is a tool for building quantum algorithms."),
("h","1. Classical random walk (the ‘insect’)"),
("b",["An insect on a line tosses a coin each step: heads → right, tails → left.","After t steps position spread σ ≈ **√t** (diffusive); distribution is a bell curve centred at the start."]),
("h","2. Discrete-time quantum walk (coined walk)"),
("n",["**State space:** position |x⟩ ⊗ coin |c⟩ with c ∈ {0 (left), 1 (right)}.","**Coin operation C:** apply a Hadamard to the coin qubit → coin in superposition of ‘left’ and ‘right’.","**Shift operation S:** move right if coin = 1, left if coin = 0 (conditional on coin): S|x,c⟩ = |x ± 1, c⟩.","**One step:** U = S·(C ⊗ I). Repeat **t** times (no measurement in between, so paths interfere).","**Measure** position at the end → probability distribution."]),
("c",["coin |c⟩","position |x⟩"],[("H",0,"C = H",0),("U2",0,1,"S\nshift",1),("BAR","repeat t times",2),("M",1,3)],"One step of a discrete quantum walk: coin flip (Hadamard) then conditional shift; repeated t times",["","x"],4.6),
("i",SCR+"/diagrams/walk.png","Probability after 60 steps: classical walk (blue, narrow bell) vs quantum Hadamard walk (orange, spread out with peaks near the ends)",5.2),
("h","3. Continuous-time quantum walk"),
("b",["No coin; evolution U(t) = e^(−iHt) where H = adjacency matrix (or Laplacian) of the graph; state spreads over graph nodes by Schrödinger evolution."]),
("h","4. Comparison"),
("t",["Point","Classical random walk","Quantum walk"],[["Randomness","Coin toss, one path at a time","Superposition of all paths + interference"],["Spread σ after t steps","≈ √t","≈ **t** (ballistic, ≈ 0.54 t for Hadamard coin)"],["Distribution","Bell curve (binomial) centred at start","Two peaks near ±t/√2, flat middle"],["Evolution","Stochastic (probabilities)","Unitary (amplitudes), reversible"],["Hitting time on graph","Polynomial","Can be exponentially faster on some graphs"]],[1.5,2.5,2.8]),
("h","5. Applications"),
("b",["**Quantum search on graphs/grids** (spatial search – matches Grover's √N), element distinctness, triangle finding, evaluating game trees (quantum tree search), graph isomorphism heuristics.","Universal model of quantum computation; basis for quantum Monte-Carlo / PageRank and for quantum transport in photosynthesis."]),
("concl","A quantum walk replaces the random coin by a quantum coin, so superposition and interference make the walker spread quadratically faster – the basis of many quantum search algorithms."),
("tip","**“Coin – Shift – Repeat – Measure; spread t (quantum) vs √t (classical).”**"),
])
# ---------- 4.4 CHALLENGES IN DATA SCIENCE ----------
A['4.4']=dict(src="QAI-ii.pdf p.22 (4.2.3 Challenges of quantum-enhanced machine learning: hardware limitations, error correction, hybrid integration, scalability), p.2–4 (QC overview, noise and decoherence)",
flag="Partly ⚠ not found: your book lists general challenges of quantum-enhanced ML (p.22); the data-science-specific points (data loading, dequantization, readout, benchmarks) are from standard knowledge.",blocks=[
("def","**Data science** needs to load, store and analyse very large classical data. **Quantum computing** promises speed-ups for linear algebra, optimisation and ML, but it faces many technical and practical **challenges and limitations** before it can be used in data science."),
("t",["Challenge / limitation","Explanation","Possible remedy"],[
["**Quantum hardware limits**","Few qubits, short coherence, noisy gates (NISQ) – QAI-ii.pdf p.22","Better hardware, error mitigation"],
["**Noise & error correction**","Qubits are fragile; QEC needs 100s–1000s of physical qubits per logical qubit (p.22)","Fault-tolerant codes, VQAs"],
["**Data loading (QRAM)**","Classical big data must be encoded into qubits (amplitude encoding); loading can cost O(N) and kill the speed-up","QRAM, efficient state preparation"],
["**Readout bottleneck**","Measurement gives only samples, not the full result vector (e.g. HHL gives |x⟩, not x)","Ask for aggregate properties"],
["**Assumption-dependent speed-ups**","HHL needs sparse, well-conditioned matrices; ‘dequantized’ classical algorithms often match QML","Honest benchmarking"],
["**Hybrid integration**","Combining classical and quantum workflows efficiently is non-trivial (p.22)","Frameworks: Qiskit, PennyLane"],
["**Scalability**","Algorithms must scale to real datasets; qubit count and circuit depth limited (p.22)","Modular / networked QC"],
["**Training difficulties**","Barren plateaus, many measurement shots, noisy gradients","Better ansatz, initialisation"],
["**Skills, tools, cost**","Shortage of quantum-ML experts; expensive access; immature software, no standards","Education, cloud access"],
["**Interpretability & benchmarking**","Hard to compare with strong classical baselines; results are probabilistic","Standard benchmarks"],
["**Security**","Quantum computers threaten current encryption of data (Shor)","Post-quantum cryptography"]],[1.7,3.2,1.9]),
("p","**Overall:** quantum computing is promising for data science but today works best for small, structured problems; realistic gains need fault-tolerant hardware and efficient data loading."),
("concl","Limited, noisy hardware, expensive data loading/readout and assumption-heavy speed-ups are the main barriers to using quantum computing in data science."),
("tip","**“Hardware, Noise, Loading, Readout, Hybrid, Scale.”** Give at least 6 points with one-line explanations."),
])
# ---------- 4.2 QUANTUM NEURAL COMPUTATION ----------
A['4.2']=dict(src="QAI-ii.pdf p.20–23 (QNN in quantum-enhanced ML), p.34–35 (QNN: encoding, quantum neurons, operations, measurement and learning; XOR example)",
flag="Partly ⚠ not found: your book explains Quantum Neural Networks, but not ‘quantum neural computation’ as a topic; the answer builds on the QNN pages and adds standard background (quantum perceptron, associative memory).",blocks=[
("def","**Quantum neural computation** is information processing with **neural-network models implemented on quantum systems**: inputs are encoded in qubits, **quantum gates act as neurons/weights**, and learning adjusts gate parameters (QAI-ii.pdf p.34). It merges the parallelism of quantum computing with the learning ability of neural networks."),
("h","1. Elements (book p.34)"),
("t",["Element","Classical neural net","Quantum neural computation"],[["Input","Vector x","Quantum state |ψ_x⟩ (quantum encoding)"],["Neuron","y = f(Σ wᵢxᵢ)","Quantum gates / circuits (quantum perceptron U(θ))"],["Weights","Real numbers","Gate parameters θ (rotation angles)"],["Output","Activation value","Measurement result (probabilistic)"],["Learning","Back-propagation","Classical optimiser adjusts θ (hybrid)"]],[1.2,2.3,3.3]),
("d",dg('a[label="Classical data x"]; b[label="Quantum encoding\\n|ψ_x⟩"]; c[label="Quantum neurons\\nparameterised gates U(θ)",fillcolor="#E2EFDA"]; d[label="Measurement"]; e[label="Output / loss"]; f[label="Optimiser\\nupdates θ",fillcolor="#FFF2CC"]; a->b->c->d->e->f; f->c[constraint=false];',"LR"),"Quantum neural computation (hybrid training loop)",6.3),
("h","2. Significance (why it matters)"),
("b",["**Exponentially large state space:** n qubits represent 2ⁿ amplitudes → compact models.","**Superposition & entanglement** give parallelism and rich correlations.","**Quantum associative memory:** stores ~2ⁿ patterns in n qubits (classical Hopfield stores ≈ 0.14·n).","Potentially faster training / fewer parameters; applications in pattern recognition, classification, optimisation, quantum-data analysis (QAI-ii.pdf p.20–23)."]),
("h","3. Example (book p.35)"),
("p","XOR problem solved by a QNN with ZZ-feature-map encoding and RealAmplitudes layers, trained with SPSA: predicted labels [0 1 1 0] = true labels (100 % accuracy)."),
("h","4. Limitations"),
("b",["Noise, few qubits, barren plateaus, data-loading cost; measurement is probabilistic."]),
("concl","Quantum neural computation implements neurons as parameterised quantum circuits and trains them hybrid-style, offering large representational capacity and possible speed-ups."),
("tip","**“Neuron = quantum gate, weight = angle, activation = measurement.”**"),
])
# ---------- 4.3 QUANTUM TREE SEARCH ----------
A['4.3']=dict(src="Not in your materials (only Grover's algorithm, QAI-ii.pdf p.13–15, is the related tool)",flag=NF,blocks=[
("def","**Quantum tree search** applies quantum algorithms (**Grover search** and **quantum walks**) to search a **tree** (state-space of a puzzle, game or constraint problem) for a goal node/leaf, giving a **quadratic speed-up**: about √T steps for a tree with T nodes instead of T."),
("h","1. Classical tree search"),
("b",["Depth-first / breadth-first / backtracking explore nodes one by one: tree with branching factor b and depth d has about **bᵈ** nodes → time **O(bᵈ)**."]),
("h","2. Quantum approach"),
("n",["**Represent paths** from the root as basis states: each path (sequence of rule/branch choices) is a binary string |p⟩.","**Superposition:** Hadamards create all paths of depth d simultaneously.","**Oracle:** checks (reversibly) whether the path ends in a goal state and marks it with a −1 phase.","**Amplitude amplification (Grover):** ≈ (π/4)√(bᵈ) = O(b^(d/2)) iterations.","**Measure** → the path to a goal; verify classically.","(Alternative: **quantum backtracking** – a quantum walk on the tree finds a marked node in ≈ √T·poly(d) steps.)"]),
("d",dg('r[label="root"]; a[label="A"]; b[label="B"]; c[label="C"]; d[label="D"]; e[label="E"]; f[label="F"]; g[label="G ★ goal",fillcolor="#E2EFDA"]; h[label="H"]; r->a; r->b; a->c; a->d; b->e; b->f; f->g; f->h;',"TB"),"Tree with one goal leaf (G): Grover searches all root-to-leaf paths in superposition",4.0),
("p","**Example:** binary tree of depth 3 → 8 leaf paths (3 qubits). Classical search needs up to 8 (≈ 4 on average) goal tests; Grover needs ≈ (π/4)√8 ≈ **2** iterations."),
("t",["Point","Classical","Quantum"],[["Nodes examined","≈ T (or bᵈ)","≈ √T (b^(d/2))"],["Idea","Sequential visiting","Superposition of paths + amplitude amplification / quantum walk"],["Result","Deterministic","Probabilistic, verified"]],[1.5,2.5,2.8]),
("h","3. Uses"),
("b",["Constraint satisfaction, SAT, puzzles, game-tree evaluation, planning in AI (links to quantum production systems)."]),
("concl","Quantum tree search speeds up exhaustive tree exploration quadratically by searching all paths in superposition with Grover/quantum-walk techniques."),
("tip","**“bᵈ → b^(d/2).”**"),
])
# ---------- 4.5 QUANTUM PRODUCTION SYSTEM ----------
A['4.5']=dict(src="Not in your materials",flag=NF+" Details of Tarrataca's model below are recalled from general knowledge of the literature (L. Tarrataca & A. Wichert, tree search with Grover's algorithm) – verify the exact formulation against your class notes.",blocks=[
("def","A **production system** (classical AI) solves problems by repeatedly applying **production rules** (IF condition THEN action) to a **current state** until a goal is reached; the possible states form a **search tree**. A **quantum production system** (as proposed by Tarrataca) represents states and rules with qubits and uses **quantum superposition and Grover's algorithm** to search this tree faster."),
("h","1. Classical production system – three parts"),
("b",["**Rule base** (productions: condition → action).","**Working memory / database:** the current state.","**Control strategy (inference engine):** chooses which applicable rule to fire (DFS, BFS, heuristic)."]),
("h","2. Quantum production system"),
("n",["**State register:** qubits storing the current state (initial state in |s₀⟩).","**Rule/choice register:** in a uniform superposition of all rule choices at each depth level.","**Reversible rule application:** each production is implemented as a unitary operator so that all rule sequences are applied in superposition: Σ |r₁…r_d⟩|s₀⟩ → Σ |r₁…r_d⟩|s_(r₁…r_d)⟩.","**Goal test oracle:** marks (phase −1) all sequences whose final state satisfies the goal.","**Grover amplitude amplification** on the rule-sequence register (≈ √(bᵈ) iterations).","**Measure** the rule register → sequence of rules (solution path)."]),
("d",dg('a[label="Initial state |s₀⟩"]; b[label="Rule-choice register\\nΣ|r₁…r_d⟩ (Hadamards)"]; c[label="Apply productions\\n(reversible unitaries)",fillcolor="#E2EFDA"]; d[label="Goal-test oracle\\n(marks solutions)",fillcolor="#FFF2CC"]; e[label="Amplitude amplification\\n(Grover, ≈ √bᵈ)"]; f[label="Measure → rule sequence\\n(solution path)",shape=oval]; a->c; b->c; c->d->e->f; e->c[label="repeat",constraint=false];',"LR"),"Block diagram of a quantum production system",6.3),
("p","**Components:** the *rule-choice register* encodes every possible sequence of rules; the *productions* act as reversible gates; the *oracle* tells goal from non-goal; *Grover* boosts the goal paths."),
("t",["Point","Classical production system","Quantum production system"],[["States","One current state","Superposition of all reachable states"],["Search","Sequential, O(bᵈ)","Amplitude amplification, O(b^(d/2))"],["Rules","Arbitrary functions","Must be **reversible (unitary)**"],["Result","Deterministic path","Probabilistic, verified path"]],[1.4,2.6,2.8]),
("h","3. Limitations"),
("b",["Needs reversible rules and enough qubits (grows with depth); only quadratic speed-up; noise on current hardware."]),
("concl","A quantum production system encodes the production-rule search tree in qubits and uses Grover's algorithm to find a goal path in about √(bᵈ) steps."),
("tip","**“Rules as unitaries + Superposed paths + Goal oracle + Grover.”**"),
])
# ---------- 4.6 HEURISTIC SEARCH ----------
A['4.6']=dict(src="Passing mention only: QAI-ii.pdf p.15 (heuristics as rules of thumb guiding search, job-shop scheduling case study)",flag=NF,blocks=[
("def","**Heuristic search** is a search that uses problem-specific knowledge – a **heuristic function h(n)** estimating the cost from node n to the goal – to explore the most promising nodes first, instead of searching blindly. Heuristics are ‘rules of thumb’ (QAI-ii.pdf p.15)."),
("h","1. A* algorithm (best-first search)"),
("f",["f(n) = g(n) + h(n)","g(n) = actual cost from start to n ;  h(n) = estimated cost from n to goal ;  f(n) = estimated total cost through n"]),
("n",["Put the start node in OPEN with f = h(start).","Remove the node with the **lowest f** from OPEN.","If it is the goal → stop (optimal if h never overestimates, i.e. is *admissible*).","Otherwise expand it, compute f for its successors, add them to OPEN (update if a cheaper path is found).","Repeat."]),
("h","2. Example"),
("d",dg('S[label="S\\nh=5"]; A[label="A\\nh=4"]; B[label="B\\nh=3"]; C[label="C\\nh=3"]; G[label="G (goal)\\nh=0",fillcolor="#E2EFDA"]; S->A[label=1]; S->B[label=3]; A->C[label=2]; A->G[label=6]; B->G[label=4]; C->G[label=3];',"LR"),"Search graph: edge labels = step cost, h = heuristic estimate to G",5.0),
("t",["Step","Expanded node","OPEN list with f = g + h"],[["1","S","A (1+4=5), B (3+3=6)"],["2","A (f=5)","B 6, C (3+3=6), G (7+0=7)"],["3","B (f=6)","C 6, G 7 (via B: 7, no better)"],["4","C (f=6)","G (6+0=6) – improves G"],["5","G (f=6)","Goal reached"]],[0.7,1.8,4.3]),
("p","**Solution:** S → A → C → G with total cost **1 + 2 + 3 = 6** (optimal); blind search would have explored all nodes."),
("h","3. Quantum connection"),
("b",["A good heuristic **prunes** the tree (reduces branching factor b); quantum search (Grover / quantum production system) is then applied to the pruned tree → time ≈ √(b_eff^d), combining both speed-ups.","Variational/heuristic methods like QAOA also act as heuristics for optimisation (book p.15–16)."]),
("t",["Blind search","Heuristic search"],[["No problem knowledge","Uses h(n)"],["Explores many nodes","Explores few promising nodes"],["Always complete, slow","Fast; optimal if h admissible"]],[3.0,3.8]),
("concl","Heuristic search guides exploration with an estimate h(n), reaching the goal with far fewer nodes; quantum search can speed up the remaining search further."),
("tip","**“f = g + h; pick the lowest f; admissible h ⇒ optimal.”**"),
])
# ---------- 4.7 PENNYLANE ----------
A['4.7']=dict(src="Not in your materials",flag=NF,blocks=[
("def","**PennyLane** is an open-source, **cross-platform Python library** (from Xanadu) for **quantum machine learning, quantum computing and quantum chemistry**. Its key feature is **automatic differentiation of quantum circuits**, so hybrid quantum–classical models can be trained like neural networks."),
("h","1. Why cross-platform"),
("d",dg('a[label="ML frameworks\\nPyTorch · TensorFlow · JAX · NumPy"]; b[label="PennyLane\\n(QNodes, auto-differentiation, optimisers)",fillcolor="#E2EFDA"]; c[label="Quantum devices / simulators (plugins)\\nIBM Qiskit · Google Cirq · Amazon Braket · IonQ · Rigetti · lightning",fillcolor="#FFF2CC"]; a->b->c;',"TB"),"PennyLane sits between ML libraries and quantum hardware/simulators",5.4),
("h","2. Features"),
("b",["**QNode:** a quantum function bound to a device, callable like a normal Python function.","**Hardware-agnostic:** same code runs on many simulators/hardware (change the device name).","**Automatic differentiation:** gradients via *parameter-shift rule*, back-propagation (simulators).","**Built-in optimisers** (GradientDescent, Adam), **templates** (AngleEmbedding, StronglyEntanglingLayers) and chemistry tools.","Integrates with PyTorch/TensorFlow/JAX for hybrid models."]),
("h","3. Example"),
("code",["import pennylane as qml","from pennylane import numpy as np","dev = qml.device('default.qubit', wires=2)","","@qml.qnode(dev)","def circuit(params):","    qml.RX(params[0], wires=0)","    qml.CNOT(wires=[0, 1])","    qml.RY(params[1], wires=1)","    return qml.expval(qml.PauliZ(1))   # cost","","params = np.array([0.5, 0.2], requires_grad=True)","opt = qml.GradientDescentOptimizer(0.1)","for _ in range(50):","    params = opt.step(circuit, params)  # minimise <Z>"]),
("p","The circuit is evaluated on the device; PennyLane differentiates it and the classical optimiser updates `params` – a variational quantum algorithm in a few lines."),
("h","4. Applications / comparison"),
("b",["Variational classifiers, QNNs, VQE for molecules, QAOA, quantum kernels.","Unlike Qiskit (IBM-centric circuits), PennyLane's focus is **differentiable programming** across platforms."]),
("concl","PennyLane is a hardware-agnostic Python library that makes quantum circuits differentiable and trainable, enabling hybrid quantum machine learning."),
("tip","**“PennyLane = Python + Autodiff + Any device.”**"),
])
# ---------- 4.8 QUANTUM SEARCH ----------
A['4.8']=dict(src="QAI-ii.pdf p.13–15 (Grover's algorithm, steps, 8-element example), p.20–22 (quantum search algorithms in quantum-enhanced ML), p.29 (Grover for nearest-neighbour search)",blocks=[
("def","**Quantum search** is the use of quantum algorithms – mainly **Grover's algorithm** – to find a marked item in an **unsorted** collection of N items in about **√N** steps, a **quadratic speed-up** over classical O(N) search (QAI-ii.pdf p.13)."),
("t",["Point","Classical search","Quantum search (Grover)"],[["Queries (N items)","O(N)","**O(√N)**"],["Method","Check items one by one","Superposition + oracle + amplitude amplification"],["Success","Certain after N checks","≈ 1 after (π/4)√N iterations"],["Optimality","–","Proven optimal: no quantum algorithm beats Ω(√N)"]],[1.5,2.5,2.8]),
("c",["|0⟩ⁿ"],[("H",0,"$H^{\\otimes n}$",0),("U2",0,0,"Oracle",1),("U2",0,0,"Diffusion",2),("BAR","repeat ≈ (π/4)√N",3),("M",0,3)],"Quantum search circuit (Grover)",[""],4.6),
("h","Steps (short)"),
("n",["Prepare equal superposition of all N items (Hadamards).","Oracle marks the target with a −1 phase.","Diffusion (inversion about the mean) increases the target's amplitude.","Repeat about (π/4)√N times; measure."]),
("h","Variants and uses"),
("b",["**Amplitude amplification** (generalised), **quantum counting** (number of solutions), search with unknown number of solutions.","**Quantum walk search** on graphs, **tree search**, nearest-neighbour search (QAI-ii.pdf p.29), SAT/optimisation, key search."]),
("p","**Example:** N = 8 → ≈ 2 iterations give success probability ≈ 94.5 % (see Q1.2)."),
("concl","Quantum search finds a marked item among N in O(√N) queries and is provably optimal, forming the basis of many quantum AI algorithms."),
("tip","**“Quantum search = Grover = √N (not exponential).”**"),
])
REVISION=[
("h","Key definitions"),
("b",["**Quantum walk:** coin + shift, superposition of paths; spread ∝ t vs √t classical.","**Challenges in data science:** hardware limits, noise/QEC, data loading (QRAM), readout, hybrid integration, scalability, training, skills.","**Quantum neural computation:** neurons = parameterised quantum gates; measure; hybrid optimiser.","**Quantum tree search:** Grover/quantum walk over tree paths: bᵈ → b^(d/2).","**Quantum production system (Tarrataca):** rules as unitaries + superposed rule sequences + goal oracle + Grover.","**Heuristic search:** A*: f = g + h; admissible h ⇒ optimal.","**PennyLane:** cross-platform Python library, autodiff of quantum circuits, QNodes.","**Quantum search:** Grover, O(√N), optimal."]),
("h","Formulas"),
("f",["U = S·(C ⊗ I) (coined quantum walk) ; σ_quantum ≈ 0.54 t, σ_classical = √t","Grover iterations ≈ (π/4)√N ; tree: O(bᵈ) → O(b^(d/2))","A*: f(n) = g(n) + h(n)"]),
("h","Memory tricks"),
("b",["Walk = **C-S-R-M** (Coin, Shift, Repeat, Measure).","Production system = **Rules + Memory + Control**; quantum adds **superposition + Grover**.","Challenges = **HNLRHS**: Hardware, Noise, Loading, Readout, Hybrid, Scale.","PennyLane = **Python + Autodiff + Any device.**"]),
]
ASSUMPTIONS=[
"Unit 4 = Q7/Q8 of 2023–2025 (quantum search, quantum walks, quantum production systems, heuristic search, quantum AI/data science).",
"**Your materials cover only:** Grover/quantum search (QAI-ii.pdf p.13–15, 20–22, 29), QNN (p.20–23, 34–35) and a general challenges list for quantum-enhanced ML (p.22). **Quantum walk, tree search, production system, heuristic search and PennyLane are not in your materials** and are marked ⚠ (written from standard knowledge; no citations to your files are claimed).",
"2024 Q8a ‘Quantum Walk – Random Insect’ is interpreted as the classical random walk of an insect/drunkard compared with the quantum walk. Please check with your class notes if ‘Random Insect’ refers to something specific.",
"**Tarrataca's quantum production system (Q4.5):** the description is a general account recalled from the literature (rules as reversible operators + Grover over the search tree); I cannot verify the exact formulation from your files – **please check against your lecture notes** before relying on it.",
"Q4.4 and Q4.2 are only partly covered by your book (flagged ⚠ partial).",
"The quantum-walk plot is a computer simulation (Hadamard coin, symmetric initial coin state, 60 steps), not from your book.",
"Answer lengths follow (max marks + 2): Quantum walk, Challenges = 11; Tree search, Heuristic search = 10; Neural computation, Production system, PennyLane = 8; Quantum search = 7.",
]
ANSWERS=A
