from blib import dg
A={}
NF="⚠ Not found in your materials. Standard textbook answer."
# ---------- 3.1 TELEPORTATION ----------
A['3.1']=dict(src="QAI.pdf p.9–12 (quantum teleportation: Bell pair, Bell measurement, two classical bits, correction gates, Bell states p.10)",blocks=[
("def","**Quantum teleportation** is a protocol that transfers the **unknown state of one qubit** to another qubit at a distant place, **without physically sending the qubit**, using a shared **entangled (Bell) pair** and **two classical bits** (QAI.pdf p.10)."),
("h","1. Requirements"),
("b",["Sender Mahesh (Alice) holds qubit A = |ψ⟩ = α|0⟩ + β|1⟩ (unknown), receiver Ramesh (Bob) is far away.","A shared Bell pair |Φ⁺⟩ = (|00⟩ + |11⟩)/√2: one half with Alice, the other half with Bob.","A classical channel to send 2 bits."]),
("h","2. Steps"),
("n",["**Entanglement generation:** create the Bell pair (H + CNOT) and distribute one qubit to each party.","**Bell measurement (Alice):** apply **CNOT** (control = |ψ⟩, target = her Bell qubit), then **Hadamard** on |ψ⟩.","**Measure** both of Alice's qubits → two classical bits (m₁, m₂).","**Classical communication:** Alice sends m₁m₂ to Bob.","**Correction (Bob):** apply X^(m₂) then Z^(m₁) to his qubit → Bob's qubit becomes exactly α|0⟩ + β|1⟩."]),
("c",["|ψ⟩ (Alice)","|0⟩ (Alice)","|0⟩ (Bob)"],[("H",1,"H",0),("CX",1,2,1),("BAR","",2),("CX",0,1,3),("H",0,"H",4),("M",0,5),("M",1,5),("X",2,"X$^{m_2}$",6),("Z",2,"Z$^{m_1}$",7)],"Teleportation circuit: Bell pair (cols 1–2), Bell measurement (cols 3–5), classical-controlled corrections on Bob's qubit",["m₁","m₂","|ψ⟩"],6.4),
("p","**Components:** H + CNOT on the middle/bottom wires make the Bell pair; CNOT + H + measurement on the top two wires is the Bell measurement; X and Z boxes are applied by Bob only if the received bits are 1."),
("h","3. Mathematics"),
("f",["|ψ⟩|Φ⁺⟩ = (α|0⟩+β|1⟩)(|00⟩+|11⟩)/√2","After CNOT and H: ½ [ |00⟩(α|0⟩+β|1⟩) + |01⟩(α|1⟩+β|0⟩) + |10⟩(α|0⟩−β|1⟩) + |11⟩(α|1⟩−β|0⟩) ]"]),
("t",["Alice's bits (m₁ m₂)","Bob's qubit before correction","Correction by Bob"],[["00","α|0⟩ + β|1⟩","None (I)"],["01","α|1⟩ + β|0⟩","X"],["10","α|0⟩ − β|1⟩","Z"],["11","α|1⟩ − β|0⟩","X then Z (ZX)"]],[1.6,2.6,2.2]),
("h","4. Example"),
("p","Let |ψ⟩ = 0.6|0⟩ + 0.8|1⟩. Each of the four outcomes occurs with probability ¼. If Alice gets 10, Bob holds 0.6|0⟩ − 0.8|1⟩; applying Z gives 0.6|0⟩ + 0.8|1⟩ = |ψ⟩. Bob gets the same state in every case."),
("h","5. Important points / significance"),
("b",["**No cloning:** Alice's original qubit is destroyed by the measurement – the state is *moved*, not copied.","**No faster-than-light signalling:** Bob's state is useless until the 2 classical bits arrive.","Uses: **quantum communication / quantum internet, quantum repeaters, distributed quantum computing, gate teleportation, fault-tolerant computing**.","Transfers 1 qubit using 1 ebit + 2 classical bits."]),
("concl","Teleportation moves an unknown qubit state using entanglement plus two classical bits; it is the basic building block of quantum communication."),
("tip","**“Entangle – Bell-measure – Call (2 bits) – Correct (X, Z).”** Remember: *no copying, no faster-than-light.*"),
])
# ---------- 3.2 DENSE CODING ----------
A['3.2']=dict(src="Not in your materials",flag=NF+" (Related background: Bell states and CNOT/Hadamard, QAI.pdf p.10; teleportation, p.10–12.)",blocks=[
("def","**Quantum dense (superdense) coding** is a protocol that lets Alice send **two classical bits** to Bob by transmitting **only one qubit**, using a previously shared **entangled pair**. It is the ‘reverse’ of teleportation (teleportation: 1 qubit ← 2 bits)."),
("h","1. Steps"),
("n",["**Entanglement:** a source creates |Φ⁺⟩ = (|00⟩ + |11⟩)/√2; first qubit goes to Alice, second to Bob.","**Encoding (Alice):** to send bits b₁b₂ she applies a gate to **her qubit only** (table below).","**Transmission:** Alice sends her single qubit to Bob.","**Decoding (Bob):** apply CNOT (control = Alice's qubit, target = his qubit), then Hadamard on Alice's qubit.","**Measurement:** Bob measures both qubits and obtains b₁b₂ exactly."]),
("c",["Alice q₀","Bob q₁"],[("H",0,"H",0),("CX",0,1,1),("BAR","Alice encodes",2),("U",0,"σ",3),("BAR","Bob decodes",4),("CX",0,1,5),("H",0,"H",6),("M",0,7),("M",1,7)],"Dense-coding circuit (σ = I, X, Z or ZX chosen by the 2 message bits)",["b₁","b₂"],6.0),
("t",["Message b₁b₂","Alice's gate","State sent / received","Bob's result after CNOT + H"],[["00","I","(|00⟩+|11⟩)/√2 = Φ⁺","00"],["01","X","(|01⟩+|10⟩)/√2 = Ψ⁺","01"],["10","Z","(|00⟩−|11⟩)/√2 = Φ⁻","10"],["11","ZX (iY)","(|01⟩−|10⟩)/√2 = Ψ⁻","11"]],[1.1,1.1,2.6,1.6]),
("p","**Explanation:** the four Bell states are mutually orthogonal, so Bob can distinguish them perfectly; Alice's local gate selects one of the four. A single qubit can therefore carry 2 bits *because* of the entanglement it shares."),
("h","2. Important points"),
("b",["Classical capacity doubles: 2 bits per qubit sent (cost: 1 shared ebit).","Without entanglement, 1 qubit can carry only 1 classical bit (Holevo bound).","Eavesdropper intercepting Alice's qubit alone learns nothing (the qubit alone is maximally mixed) – useful for secure communication.","Experimentally demonstrated with photons."]),
("t",["Point","Teleportation","Dense coding"],[["Sends","1 qubit state","2 classical bits"],["Uses","1 ebit + 2 classical bits","1 ebit + 1 qubit"]],[1.5,2.6,2.6]),
("concl","Dense coding doubles the classical information per transmitted qubit by exploiting shared entanglement."),
("tip","**“2 bits in 1 qubit: I, X, Z, ZX → 00, 01, 10, 11.”** Decode = CNOT then H."),
])
# ---------- 3.3 QUANTUM CRYPTOGRAPHY ----------
A['3.3']=dict(src="Not in your materials (only one-line mentions: QAI-ii.pdf p.2 – quantum key distribution as a cryptographic application; QAI.pdf p.22, p.28 – cryptography as an application of entanglement; QAI.pdf p.32, QAI-ii.pdf p.13 – Shor threat to RSA)",flag=NF,blocks=[
("def","**Quantum cryptography** uses the laws of quantum mechanics (superposition, measurement disturbance, no-cloning) to secure communication. Its best-known application is **Quantum Key Distribution (QKD)**, which lets two parties share a secret key whose secrecy is guaranteed by physics, not by computational difficulty."),
("h","1. Why needed"),
("b",["Classical public-key cryptography (RSA, ECC) is based on hard maths problems and is **broken by Shor's algorithm** (QAI.pdf p.32).","Quantum cryptography remains secure even against quantum computers."]),
("h","2. Principles that give security"),
("b",["**Measurement disturbs the state:** reading a qubit in the wrong basis changes it → eavesdropping is detectable.","**No-cloning theorem:** an eavesdropper cannot copy unknown qubits.","**Heisenberg uncertainty:** non-orthogonal states cannot be perfectly distinguished.","**Entanglement correlations** (E91) provide shared random bits."]),
("d",dg('a[label="Alice\\n(sender)"]; b[label="Bob\\n(receiver)"]; e[label="Eve (eavesdropper)\\nmeasuring disturbs the qubits\\n⇒ errors reveal her",fillcolor="#F8CBAD"]; a->b[label="quantum channel (photons)",color="#2E74B5"]; b->a[label="public classical channel\\n(basis comparison, error check)",style=dashed]; a->e[style=dotted,arrowhead=none]; e->b[style=dotted];',"LR"),"Setup of quantum key distribution",5.8),
("h","3. Main techniques"),
("t",["Technique","Idea"],[["**BB84 (QKD)**","Random bits in random bases; sifting; error check; privacy amplification"],["**E91**","Uses entangled pairs; Bell-inequality test detects eavesdropping"],["**B92**","Two non-orthogonal states only"],["**Secure communication**","Key from QKD used in a **one-time pad** (perfectly secret) or AES"],["**Quantum random numbers, digital signatures, quantum secure direct communication**","Other applications"]],[2.6,4.2]),
("h","4. Secure communication with QKD"),
("n",["Alice and Bob run QKD → identical secret key K (length ≥ message).","Alice computes ciphertext C = M ⊕ K (**one-time pad**) and sends it over any channel.","Bob recovers M = C ⊕ K. If Eve was present, the error rate in QKD exceeds threshold and the key is discarded."]),
("h","5. Classical vs quantum cryptography"),
("t",["Point","Classical (RSA)","Quantum (QKD)"],[["Security basis","Computational hardness","Laws of physics"],["Quantum-computer safe?","No (Shor)","Yes"],["Eavesdropping","Undetectable","Detectable (disturbance)"],["Needs","Computers","Single-photon source/detectors, fibre / free-space link"],["Limits","—","Distance (photon loss), cost, key rate, trusted nodes"]],[1.7,2.5,2.6]),
("concl","Quantum cryptography uses quantum principles (no-cloning, measurement disturbance) to detect eavesdropping and generate unconditionally secure keys."),
("tip","**“BB84 + One-Time-Pad = unbreakable.”** Don't confuse QKD (key exchange) with encrypting the message."),
])
# ---------- 3.4 QKD ----------
A['3.4']=dict(src="Not in your materials",flag=NF,blocks=[
("def","**Quantum Key Distribution (QKD)** is a method in which two parties (Alice, Bob) generate a **shared random secret key** using qubits sent over a quantum channel; any eavesdropping disturbs the qubits and is detected. The first protocol is **BB84** (Bennett–Brassard, 1984)."),
("h","1. BB84 process (steps)"),
("n",["**Random bits & bases:** Alice picks random bits and, for each, a random basis: rectilinear (+) {|0⟩,|1⟩} or diagonal (×) {|+⟩,|−⟩}.","**Encode & send:** she sends the qubit (photon) to Bob through the quantum channel (+: 0→|0⟩, 1→|1⟩; ×: 0→|+⟩, 1→|−⟩).","**Measure:** Bob measures each qubit in a randomly chosen basis.","**Sifting:** over a public classical channel they announce **bases (not bits)** and keep only the positions where the bases match (~50 %).","**Error estimation:** they compare a random sample of the sifted key; a high **QBER** (> ~11 %) means eavesdropping → abort.","**Reconciliation & privacy amplification:** correct remaining errors and shorten the key so Eve's information is negligible → final **secret key**."]),
("d",dg('a[label="Alice: random bits\\n+ random bases"]; b[label="Quantum channel:\\nsend qubits",fillcolor="#E2EFDA"]; c[label="Bob: measure in\\nrandom bases"]; d[label="Public channel:\\ncompare bases (sifting)"]; e[label="Error check (QBER)\\nEve detected?",shape=diamond,fillcolor="#FFF2CC"]; f[label="Error correction +\\nprivacy amplification"]; g[label="Shared secret key",shape=oval]; a->b->c->d->e; e->f[label="no"]; f->g; e->a[label="yes: abort",constraint=false];',"LR"),"BB84 quantum key distribution process",6.4),
("h","2. Example"),
("t",["Qubit no.","1","2","3","4","5","6","7","8"],[["Alice bit","0","1","1","0","1","0","0","1"],["Alice basis","+","+","×","+","×","×","+","×"],["Bob basis","+","×","×","×","×","+","+","+"],["Bases match?","✔","✘","✔","✘","✔","✘","✔","✘"],["Key bit","0","–","1","–","1","–","0","–"]],[1.3,0.65,0.65,0.65,0.65,0.65,0.65,0.65,0.65]),
("p","Sifted key = **0110**. If Eve intercepts and resends in random bases, she picks the wrong basis half the time and then causes an error in 50 % of those → **25 % error** in the sifted key, which Alice and Bob detect."),
("h","3. Why secure"),
("b",["No-cloning: Eve cannot copy; measurement disturbs; basis is revealed only *after* Bob has measured."]),
("concl","QKD (BB84) produces a shared secret key; the presence of an eavesdropper is revealed by an increased error rate."),
("tip","**“Send – Measure – Sift – Check – Distil.”** Only *bases* are announced publicly, never bit values."),
])
# ---------- 3.5 CLASSICAL THREE-BIT CODE ----------
A['3.5']=dict(src="Not in your materials",flag=NF,blocks=[
("def","The **classical three-bit (repetition) code** protects one bit against a single bit-flip error by sending it **three times**: 0 → 000 and 1 → 111. The receiver decodes by **majority voting**. It is the starting point for quantum error correction."),
("h","1. Encoding and decoding"),
("t",["Logical bit","Codeword sent","Received (1 error)","Majority decoding"],[["0","000","100, 010, 001","0 ✔"],["1","111","011, 101, 110","1 ✔"],["0","000","110, 101, 011 (2 errors)","1 ✘ (fails)"]],[1.2,1.4,2.3,1.9]),
("d",dg('a[label="Bit b"]; b[label="Encoder\\nb → bbb"]; c[label="Noisy channel\\n(bit flips, prob p)",fillcolor="#F8CBAD"]; d[label="Majority vote\\ndecoder",fillcolor="#E2EFDA"]; e[label="Bit b̂"]; a->b->c->d->e;',"LR"),"Three-bit repetition code",5.4),
("h","2. Error probability"),
("f",["P(no decoding error) = (1−p)³ + 3p(1−p)²","P(error after decoding) = 3p²(1−p) + p³ ≈ 3p²   (better than p if p < ½)"]),
("p","Symbols: p = probability that a single bit flips. Example: p = 0.1 → error after decoding = 3(0.01)(0.9) + 0.001 = **0.028 < 0.1**."),
("h","3. Relation to quantum codes"),
("b",["Quantum states **cannot be copied** (no-cloning), so the quantum version encodes α|0⟩+β|1⟩ → α|000⟩+β|111⟩ using two CNOTs (entanglement, not copying).","Errors are found by measuring **parity (syndrome) operators Z₁Z₂ and Z₂Z₃** without measuring the data, then corrected with X – this corrects one bit-flip. Phase flips need a similar Hadamard-rotated code (Shor's 9-qubit code combines both)."]),
("c",["|ψ⟩","|0⟩","|0⟩"],[("CX",0,1,0),("CX",0,2,1)],"Quantum 3-qubit bit-flip encoder: α|0⟩+β|1⟩ → α|000⟩+β|111⟩",["","",""],3.0),
("h","4. Limitations"),
("b",["Corrects only **one** error; fails for two or more flips; costs 3× bandwidth (rate 1/3)."]),
("concl","The three-bit code reduces error from p to ≈3p² by redundancy and majority vote; its idea (redundancy + syndrome) underlies quantum error correction."),
("tip","**“Repeat ×3, vote majority: fixes 1 flip, fails on 2.”**"),
])
# ---------- 3.6 FAULT TOLERANCE ----------
A['3.6']=dict(src="Only passing mention: QAI.pdf p.21 (QEC layer in architecture), QAI-ii.pdf p.4 (large-scale fault-tolerant quantum computers are challenging)",flag=NF,blocks=[
("def","**Fault-tolerant quantum computation** is the design of quantum circuits so that **errors in gates, state preparation, measurement and storage do not spread uncontrollably**; a computation of any length can be made reliable if the physical error rate is below a **threshold**."),
("h","1. Why needed"),
("b",["Qubits suffer **decoherence** and gate errors (~10⁻³ now); algorithms like Shor need ~10⁹ operations → errors must be actively corrected.","Quantum error correction (QEC) itself uses faulty gates – so the *correction circuits must be fault tolerant*."]),
("h","2. Key techniques"),
("n",["**QEC codes:** encode a logical qubit in many physical qubits (Shor 9-qubit, Steane 7-qubit, **surface code**).","**Transversal gates:** gate applied qubit-by-qubit across code blocks so an error cannot spread within a block.","**Fault-tolerant syndrome extraction** with verified ancilla qubits; repeat syndrome measurement.","**Concatenation / code scaling:** codes within codes lower the logical error rate doubly-exponentially.","**Magic-state distillation:** to build non-transversal gates such as T for universality."]),
("d",dg('a[label="Logical qubit\\nencoded in many\\nphysical qubits"]; b[label="Noisy fault-tolerant\\ngate (transversal)"]; c[label="Syndrome measurement\\n(ancilla qubits)",fillcolor="#FFF2CC"]; d[label="Decoder +\\nrecovery operation",fillcolor="#E2EFDA"]; a->b->c->d; d->b[label="repeat each cycle",constraint=false];',"LR"),"Fault-tolerant computation cycle",6.0),
("h","3. Threshold theorem"),
("f",["If physical error rate p < p_threshold (≈ 10⁻² for surface code),","logical error after one level of concatenation  p_L ≈ c·p²  → arbitrarily long computation with polylog overhead."]),
("h","4. Challenges"),
("b",["Huge **overhead** (hundreds–thousands of physical qubits per logical qubit), fast decoders, high-fidelity gates, qubit connectivity."]),
("concl","Fault tolerance combines error-correcting codes with carefully designed gates so that reliable large quantum computations are possible below the error threshold."),
("tip","**“Encode – Compute transversally – Check syndrome – Correct – Stay below threshold.”**"),
])
# ---------- 3.7 NOISE AND ERROR MODELS ----------
A['3.7']=dict(src="QAI.pdf p.3 (decoherence), p.20 and p.24–26 (open systems, noise, general quantum operations / CPTP maps, Kraus operators)",flag="Partly ⚠ not found: your book only introduces noise/decoherence and quantum operations; the specific named error models below (bit-flip, phase-flip, depolarising, amplitude/phase damping) are standard textbook knowledge.",blocks=[
("def","**Noise** is any unwanted interaction (with the environment or imperfect control) that disturbs a quantum state; **decoherence** is loss of superposition/entanglement. **Error models** describe this mathematically as a **quantum operation (channel)** ℰ(ρ) = Σ Eₖ ρ Eₖ† with Σ Eₖ†Eₖ = I (CPTP map, Kraus operators – QAI.pdf p.26)."),
("h","1. Sources of noise"),
("b",["Decoherence (T₁ relaxation, T₂ dephasing), imperfect gates, state-preparation and **measurement (readout) errors**, crosstalk, leakage out of the qubit subspace."]),
("h","2. Common error models"),
("t",["Model","Effect on qubit","Kraus operators (p = error prob.)"],[
["**Bit-flip**","|0⟩ ↔ |1⟩ (X error) with prob. p","√(1−p) I,  √p X"],
["**Phase-flip**","|1⟩ → −|1⟩ (Z error)","√(1−p) I,  √p Z"],
["**Bit-phase flip**","Y error","√(1−p) I,  √p Y"],
["**Depolarising**","State replaced by maximally mixed state I/2 with prob. p","√(1−3p/4) I, √(p/4) X, Y, Z"],
["**Amplitude damping** (T₁)","Energy loss |1⟩ → |0⟩ with prob. γ","E₀ = [[1,0],[0,√(1−γ)]],  E₁ = [[0,√γ],[0,0]]"],
["**Phase damping / dephasing** (T₂)","Loss of phase coherence, populations unchanged","E₀ = [[1,0],[0,√(1−λ)]],  E₁ = [[0,0],[0,√λ]]"]],[1.5,2.6,2.7]),
("d",dg('a[label="Qubit state ρ"]; b[label="Environment\\n(noise, heat, fields)",fillcolor="#F8CBAD"]; c[label="Interaction\\n(decoherence)"]; d[label="Noisy state\\nℰ(ρ) = Σ Eₖ ρ Eₖ†",fillcolor="#FFF2CC"]; a->c; b->c; c->d;',"LR"),"Noise as interaction with the environment (open system)",5.4),
("h","3. Remarks"),
("b",["Pauli (bit/phase-flip, depolarising) errors are **discrete**, so error-correcting codes can handle them; any single-qubit error is a combination of I, X, Y, Z.","Coherence times and gate fidelities (error rates ~10⁻³) decide how deep a circuit can run on NISQ devices.","Used to **simulate noisy circuits** (e.g. Qiskit noise models) and to design codes."]),
("concl","Noise is modelled by completely-positive trace-preserving maps; the bit-flip, phase-flip, depolarising and damping channels capture the main error types."),
("tip","**“Bit = X, Phase = Z, Depolarising = all, T₁ = energy loss, T₂ = phase loss.”**"),
])
# ---------- 3.8 ERROR MODEL ENCODING CHALLENGES ----------
A['3.8']=dict(src="Not in your materials",flag=NF+" (Interpretation: the question is read as the practical challenges/limits of **encoding qubits into error-correcting codes against an error model**.)",blocks=[
("def","**Error model encoding** means encoding logical qubit(s) into a larger number of physical qubits (a quantum error-correcting code) designed for an assumed **error model** (e.g. independent bit/phase flips), so that errors can be detected and corrected. Practically this faces several challenges."),
("h","Practical challenges and limitations"),
("t",["Challenge","Explanation"],[
["**No-cloning**","The qubit cannot simply be copied (unlike classical repetition); encoding must use entangling gates (CNOT networks)"],
["**Qubit overhead**","A logical qubit needs 5–1000+ physical qubits (Steane: 7, Shor: 9, surface code: hundreds) – current devices have too few"],
["**Errors in the encoder itself**","Encoding/syndrome circuits are made of noisy gates and may introduce new errors (need fault-tolerant design)"],
["**Measurement without disturbance**","Syndrome must be measured without reading the data; needs extra ancilla qubits and repeated measurement"],
["**Continuous & unknown errors**","Real errors are continuous and correlated, not just independent X/Z flips; the assumed model may not match the hardware"],
["**Correlated noise, leakage, crosstalk**","Break the independence assumption on which codes work"],
["**Threshold requirement**","Physical error rate must be below the threshold (~10⁻²–10⁻³) or encoding makes things worse"],
["**Decoding speed & connectivity**","Fast classical decoders and nearest-neighbour qubit layouts are needed; latency limits operation"],
["**Cost of universal gates**","Non-transversal T gates need costly magic-state distillation"]],[2.0,4.8]),
("concl","Error-model encoding is powerful but limited by no-cloning, huge qubit overhead, imperfect encoders and mismatch between assumed and real noise."),
("tip","**“No-clone, Overhead, Imperfect gates, Threshold.”**"),
])
# ---------- 3.9 MIXED STATES / OPERATIONS ----------
A['3.9']=dict(src="QAI.pdf p.25–26 (mixed states, density operator, partial trace, general quantum operations, CPTP maps, Kraus operators)",blocks=[
("def","A **pure state** is described by a single ket |ψ⟩. A **mixed state** is a **statistical ensemble of pure states** (system is in |ψᵢ⟩ with probability pᵢ) and is described by a **density operator** ρ (QAI.pdf p.25). **General quantum operations** (quantum channels) describe how states change under noise, measurement and interaction with the environment."),
("h","1. Mixed states"),
("f",["Pure: ρ = |ψ⟩⟨ψ|  (Tr ρ² = 1)","Mixed: ρ = Σᵢ pᵢ |ψᵢ⟩⟨ψᵢ|,   Σ pᵢ = 1  (Tr ρ² < 1)","Properties: ρ Hermitian, positive semi-definite, Tr ρ = 1"]),
("b",["**Example:** ρ = ½|0⟩⟨0| + ½|1⟩⟨1| = I/2 (maximally mixed) – different from the pure state |+⟩ although both give 50/50 in the Z basis.","**Partial trace:** for a composite system AB, ρ_A = Tr_B(ρ_AB) describes subsystem A alone. For the Bell state, ρ_A = I/2 – **entangled parts look mixed**."]),
("h","2. General quantum operations"),
("f",["ℰ(ρ) = Σₖ Eₖ ρ Eₖ†,   Σₖ Eₖ† Eₖ = I   (Kraus operators Eₖ)"]),
("b",["Represented as **completely positive, trace-preserving (CPTP) maps** – outcomes' probabilities stay valid (QAI.pdf p.26).","Describe **open systems**, measurement, noise and decoherence (unitary evolution is the special case ℰ(ρ) = UρU†).","Example – bit-flip channel: ℰ(ρ) = (1−p)ρ + p XρX."]),
("d",dg('a[label="Input ρ"]; b[label="Add environment\\n|0⟩⟨0|_E"]; c[label="Joint unitary U",fillcolor="#E2EFDA"]; d[label="Trace out\\nenvironment"]; e[label="Output ℰ(ρ)"]; a->b->c->d->e;',"LR"),"A general quantum operation as unitary + partial trace",5.6),
("table_note",""),
])
A['3.9']['blocks']=[b for b in A['3.9']['blocks'] if b[0]!="table_note"]+[
("t",["Pure state","Mixed state"],[["Single ket |ψ⟩","Ensemble {pᵢ, |ψᵢ⟩}"],["Complete knowledge","Incomplete knowledge / entanglement with environment"],["Tr ρ² = 1","Tr ρ² < 1"],["Unitary evolution","Quantum operations (CPTP)"]],[3.0,3.8]),
("concl","Mixed states (density operators) describe incomplete knowledge or open systems, and general quantum operations (CPTP maps) describe how they evolve."),
("tip","**“Pure = ket, Mixed = density matrix, Channel = Kraus sum.”**"),
]
REVISION=[
("h","Key definitions"),
("b",["**Teleportation:** 1 unknown qubit moved with 1 Bell pair + 2 classical bits; corrections X^m₂ Z^m₁.","**Dense coding:** 2 classical bits sent with 1 qubit + 1 Bell pair; Alice applies I/X/Z/ZX; Bob CNOT + H.","**Quantum cryptography / QKD (BB84):** random bits & bases → sift → check QBER → privacy amplification; Eve gives 25 % errors.","**Three-bit code:** 0→000, 1→111, majority vote; error ≈ 3p².","**Fault tolerance:** QEC + transversal gates; works below threshold.","**Noise models:** bit-flip X, phase-flip Z, depolarising, amplitude damping (T₁), phase damping (T₂).","**Mixed state:** ρ = Σ pᵢ|ψᵢ⟩⟨ψᵢ|; **channel:** ℰ(ρ) = Σ EₖρEₖ†."]),
("h","Formulas"),
("f",["|Φ⁺⟩ = (|00⟩ + |11⟩)/√2 ; bits → correction: 00 I, 01 X, 10 Z, 11 ZX","P(error, 3-bit code) = 3p²(1 − p) + p³","Tr ρ = 1 ; Tr ρ² = 1 (pure) ; Σ Eₖ†Eₖ = I","QBER with intercept-resend Eve = 25 %"]),
("h","Memory tricks"),
("b",["Teleportation: **Entangle – Bell-measure – Call – Correct**.","Dense coding: **2 bits in 1 qubit**; teleportation: **1 qubit with 2 bits** (opposite).","BB84: **Send – Measure – Sift – Check – Distil**.","Never say teleportation is faster than light; never say state is copied."]),
]
ASSUMPTIONS=[
"Unit 3 = Q5/Q6 of 2023–2025 (quantum communication, cryptography, error correction), plus teleportation (2022 in-sem Q1c) and mixed states/quantum operations (2022 in-sem Q3c) mapped here by topic.",
"**Your materials cover only:** teleportation (QAI.pdf p.9–12) and mixed states / general quantum operations (QAI.pdf p.25–26), plus passing mentions of decoherence/QEC. **Everything else in this unit is marked ⚠ and written from standard knowledge** (dense coding, quantum cryptography, QKD, classical three-bit code, fault tolerance, error-model encoding challenges); no citation to your files is claimed for them.",
"Q3.7 (noise & error models) is only partly covered (decoherence and Kraus operators in the book; named models from standard knowledge).",
"Q3.8 wording is ambiguous: interpreted as challenges of encoding qubits in error-correcting codes against an assumed error model.",
"Teleportation notation: the book names qubits A, B, C inconsistently (p.10–11); standard notation (q₀ message, q₁ Alice's half, q₂ Bob's half; corrections X^m₂ Z^m₁) is used.",
"Answer lengths follow (max marks + 2): Teleportation, Dense coding = 11; Cryptography, Noise models = 10; QKD, Error-encoding = 8; Three-bit code, Fault tolerance, Mixed states = 7.",
]
def _ins(cid,blocks):
    bl=A[cid]['blocks']; i=[k for k,b in enumerate(bl) if b[0]=="concl"][0]; A[cid]['blocks']=bl[:i]+blocks+bl[i:]
_ins('3.1',[("h","6. Significance in quantum communication"),("t",["Application","Role of teleportation"],[["Quantum internet","Moves qubits between network nodes without sending fragile photons over long lossy links"],["Quantum repeaters","**Entanglement swapping** (teleporting entanglement) extends Bell pairs over long distances"],["Distributed quantum computing","Teleports qubits/gates between separate processors (modular machines)"],["Secure communication","The quantum state never travels through the channel, so it cannot be intercepted"],["Experiments","Ground-to-satellite teleportation over ~1400 km (Micius satellite, 2017)"]],[1.9,4.9]),
("p","**Resource equation:** 1 ebit (shared Bell pair) + 2 classical bits ⇒ 1 qubit transferred.")])
_ins('3.2',[("h","3. Derivation for message 10"),("n",["Shared state |Φ⁺⟩ = (|00⟩ + |11⟩)/√2.","Alice applies Z to her qubit: (|00⟩ − |11⟩)/√2 = |Φ⁻⟩; she sends her qubit to Bob.","Bob applies CNOT: |00⟩ → |00⟩, |11⟩ → |10⟩ ⇒ (|00⟩ − |10⟩)/√2 = |−⟩|0⟩.","Bob applies H to the first qubit: H|−⟩ = |1⟩ ⇒ state |10⟩.","Measurement gives **10** – exactly Alice's message."]),
("h","4. Applications and limitations"),("b",["Proposed by **Bennett and Wiesner (1992)**; first demonstrated with entangled photons (1996).","**Applications:** doubling channel capacity, secure transmission (one intercepted qubit reveals nothing), building block for quantum networks.","**Limitations:** entanglement must be distributed in advance (it ‘pre-pays’ one qubit); entangled pairs decohere in storage; the four Bell states must be measured perfectly."])])
_ins('3.3',[("h","6. Attacks and counter-measures"),("t",["Attack","Counter-measure"],[["Intercept–resend","Detected by raised error rate (≈ 25 % in BB84)"],["Photon-number splitting (multi-photon pulses)","Decoy-state protocol"],["Detector / side-channel attacks","Measurement-device-independent QKD, device certification"],["Man-in-the-middle","Authenticated classical channel (pre-shared key)"]],[2.6,4.2]),
("h","7. Real-world use"),("b",["Swiss election results protected by QKD (2007); Beijing–Shanghai QKD backbone (~2000 km, trusted nodes); satellite QKD with Micius (China, 2017); commercial systems (ID Quantique, Toshiba)."])])
_ins('3.4',[("h","4. Other QKD protocols"),("b",["**E91 (Ekert 1991):** source sends entangled pairs to Alice and Bob; they measure in random bases; matching bases give correlated key bits; a **Bell-inequality test** on the rest reveals any eavesdropper.","**B92:** uses only two non-orthogonal states.","**Practical limits:** key rate falls with fibre distance (≈ 100–200 km without repeaters) because photons are lost."])])
_ins('3.5',[("h","5. Syndrome table (quantum 3-qubit bit-flip code)"),("t",["Error","Z₁Z₂","Z₂Z₃","Correction"],[["None","+1","+1","I"],["Flip on qubit 1","−1","+1","X₁"],["Flip on qubit 2","−1","−1","X₂"],["Flip on qubit 3","+1","−1","X₃"]],[1.8,1.2,1.2,1.6]),("p","The parities tell **which** qubit flipped without revealing α or β, so the superposition is preserved – the quantum version of majority voting.")])
_ins('3.6',[("h","5. Examples of fault-tolerant codes"),("b",["**Steane [[7,1,3]] code:** 7 physical qubits per logical qubit, corrects any single-qubit error; CNOT, H and S are transversal.","**Surface code:** qubits on a 2-D grid with only nearest-neighbour checks; threshold ≈ 1 %; used by Google and IBM experiments (logical error falls as the code grows).","**Concatenated codes:** level-k encoding gives p_L ≈ p_th (p/p_th)^(2^k)."])])
_ins('3.7',[("h","4. Effect on the Bloch sphere"),("t",["Channel","Geometric effect"],[["Bit-flip","Shrinks the y and z components; x-axis preserved"],["Phase-flip / dephasing (T₂)","Shrinks x, y components → state moves towards z-axis (superposition lost)"],["Depolarising","Shrinks the whole sphere uniformly towards the centre (I/2)"],["Amplitude damping (T₁)","Pulls every state towards the north pole |0⟩ (energy loss)"]],[2.2,4.6]),
("h","5. Formulas and example"),("f",["Depolarising: ℰ(ρ) = (1 − p) ρ + p · I/2","Bit-flip: ℰ(ρ) = (1 − p) ρ + p XρX","Coherence decays as e^(−t/T₂); excited population decays as e^(−t/T₁)"]),
("p","**Example:** |+⟩ under phase-flip with p = 0.5 becomes ½|+⟩⟨+| + ½|−⟩⟨−| = I/2 – completely mixed, all phase information lost. Typical superconducting qubits have T₁, T₂ ≈ 50–300 µs and two-qubit gate errors ≈ 0.5–1 %, which limits circuit depth."),
("h","6. Handling noise"),("b",["**Error correction** (codes + fault tolerance), **error mitigation** (zero-noise extrapolation, readout calibration), dynamical decoupling, better materials and isolation."])])
_ins('3.8',[("h","Example – why the error model matters"),("p","The 3-qubit bit-flip code α|000⟩ + β|111⟩ corrects any single X error, but a single **Z (phase) error** gives α|000⟩ − β|111⟩, which has the same syndrome as ‘no error’ – the code silently fails. Real hardware has both errors, so larger codes (Shor 9-qubit, Steane 7-qubit, surface code) are needed – increasing overhead."),
("h","Mitigation strategies"),("b",["Characterise the hardware noise first (tomography / benchmarking) and choose codes matching it (e.g. biased-noise codes).","Fault-tolerant syndrome extraction, repeated measurements, fast decoders (machine-learning decoders).","Error mitigation on NISQ devices when full encoding is too expensive."])])
_ins('3.9',[("h","3. Worked example – partial trace of a Bell state"),("p","ρ_AB = |Φ⁺⟩⟨Φ⁺| with |Φ⁺⟩ = (|00⟩ + |11⟩)/√2. Tracing out B: ρ_A = ½(|0⟩⟨0| + |1⟩⟨1|) = I/2. So although the pair is in a **pure** state, each qubit alone is **maximally mixed** (Tr ρ_A² = ½) – entanglement appears as mixedness of the parts.")])
_ins('3.2',[("h","5. Why it is possible"),("p","Without entanglement one qubit can carry at most **one** classical bit (Holevo bound). The shared Bell pair supplies the second bit in advance: Alice's local gate rotates the *joint* two-qubit state among four orthogonal Bell states, and orthogonal states can be distinguished perfectly by Bob's Bell measurement.")])
_ins('3.3',[("h","8. Quantum cryptography vs post-quantum cryptography"),("t",["Point","Quantum cryptography (QKD)","Post-quantum cryptography (PQC)"],[["Basis","Physics (no-cloning, disturbance)","New hard maths problems (lattices, codes, hashes)"],["Hardware","Photon sources, detectors, fibre/satellite","Ordinary computers – software upgrade"],["Security","Information-theoretic (unconditional) for key exchange","Computational – believed secure against quantum attacks"],["Range","Limited distance, needs special links","Works over the existing Internet"]],[1.3,2.7,2.8])])
_ins('3.7',[("h","7. Other practical error models"),("b",["**Readout (measurement) error:** a |1⟩ is recorded as 0 with probability p₁₀ (and vice versa) – modelled by a confusion matrix.","**Crosstalk / correlated errors:** a gate on one qubit disturbs neighbours.","**Leakage:** the system leaves the {|0⟩, |1⟩} subspace (e.g. to |2⟩ in transmons)."])])
ANSWERS=A
