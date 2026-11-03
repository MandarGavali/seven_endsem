# Source citations (Phase 2). Page numbers = PDF page numbers; book labels in brackets.
B = "ML Unit 3-6.pdf"
NF = "⚠ Not found in your materials. Standard textbook answer."

SRC = {
    # Unit 1 (book Unit III, PDF p = book 3-p)
    "SRC_KNN": f"{B}, pp. 25–28 (Sec. 3.6 K Nearest Neighbor, book pp. 3-25 to 3-28). Worked numerical: solved here from the 2023 paper data.",
    "SRC_EVAL": f"{B}, pp. 8–16 (Sec. 3.3 Performance Evaluation: confusion matrix, accuracy, precision, recall, F-measure; book pp. 3-8 to 3-16).",
    "SRC_KERNEL": f"{B}, pp. 36–38 (Sec. 3.8 Kernel Functions, 3.8.2 RBF, Gaussian, Polynomial; book pp. 3-36 to 3-38). Note: your textbook writes the polynomial kernel as (x·xᵢ + 1)^d, i.e. γ = 1, c = 1.",
    "SRC_BAL": f"{B}, pp. 3–4 (Sec. 3.1.2 Balanced and Imbalanced Classification Problems; book pp. 3-3, 3-4).",
    "SRC_SVM": f"{B}, pp. 29–33 (Sec. 3.7 Linear Support Vector Machines, 3.7.2 Applications, 3.7.3 Limitations; book pp. 3-29 to 3-33).",
    "SRC_SOFT": f"{B}, pp. 33–35 (Sec. 3.7 Soft Margin SVM; book pp. 3-33 to 3-35). The term 'hard margin' is not used by name in your textbook; the comparison table is standard.",
    "SRC_OVO": f"{B}, pp. 19–23 (Sec. 3.4 Multiclass Classification, 3.4.2 One-vs-One / One-vs-All; book pp. 3-19 to 3-23).",
    "SRC_BINMULTI": f"{B}, p. 3 (Sec. 3.1.1 Binary-vs-Multiclass Classification table; book p. 3-3).",
    "SRC_MULTIEVAL": f"{B}, pp. 17–18 and 23–24 (Sec. 3.4 multiclass confusion matrix, per-class precision/recall; Sec. 3.5 Micro-average method; book pp. 3-17, 3-18, 3-23, 3-24).",
    "SRC_REG": "ML Textbook.pdf, pp. 57–58 (Sec. 2.2 Cost Functions (Evaluation Metrics): Mean Error, MSE, MAE, RMSE, R-squared; book pp. 2-22 to 2-25). SSE is the total of the squared-error column in the textbook tables.",
    "SRC_BLR": "ML Textbook.pdf, pp. 56–57 (Sec. 2.1.13 Bayesian Linear Regression; book pp. 2-21, 2-22).",
    # Unit 2 (book Unit IV, PDF p = book 4-(p-39))
    "SRC_KMEANS": f"{B}, pp. 45 and 52–58 (partitioning/centroid methods; K-Means and K-Medoids; book pp. 4-6, 4-13 to 4-19).",
    "SRC_DBSCAN": f"{B}, pp. 61–62 (density-based clustering, DBSCAN; book pp. 4-22, 4-23).",
    "SRC_GMM": f"{B}, pp. 64–65 (Sec. 4.6 distribution-based clustering, 4.6.1 Gaussian Mixture Model, EM; book pp. 4-25, 4-26).",
    "SRC_TYPES": f"{B}, pp. 41–48, 61, 64 (Sec. 4.1 What is clustering; types: partitioning, hierarchical, density, distribution; book pp. 4-2 to 4-9, 4-22, 4-25). Grid-based and fuzzy types are standard additions.",
    "SRC_ELBOW": f"{B}, pp. 41–42 (uses / need of cluster analysis) and pp. 59–60 (elbow method; book pp. 4-2, 4-3, 4-20, 4-21).",
    "SRC_HC": f"{B}, pp. 48–52 (hierarchical clustering: agglomerative and divisive, dendrogram; book pp. 4-9 to 4-13). The worked example is a standard illustration.",
    "SRC_APPS": f"{B}, pp. 66–67 (Sec. 4.7 Application of Clustering Technique: market segmentation, social network analysis, image segmentation, anomaly detection; book pp. 4-27, 4-28).",
    # Unit 3 (book Unit V, PDF p = book 5-(p-67))
    "SRC_ENS": f"{B}, pp. 68–71 (Sec. 5.1 Introduction, 5.1.1 Need of Ensemble Learning, advantages and limitations; book pp. 5-1 to 5-4) and pp. 75–77 (bagging, boosting).",
    "SRC_VOTE": f"{B}, pp. 72–74 (Sec. 5.2 Voting Ensemble, 5.2.1 Types of Voting: max voting, averaging, weighted averaging; book pp. 5-5 to 5-7).",
    "SRC_STACK": f"{B}, pp. 79–80 (stacking frame, meta-learner, cross-validation; variance reduction; book pp. 5-12, 5-13).",
    "SRC_ADA": f"{B}, pp. 77–80 (boosting, AdaBoost, AdaBoost stump; book pp. 5-10 to 5-13). Weight-update formulas are the standard ones (the OCR of the formula lines was unreadable).",
    "SRC_RF": f"{B}, pp. 81–85 (Sec. 5.4 Random Forest Ensemble, advantages; book pp. 5-14 to 5-18).",
    "SRC_HOMO": f"{B}, p. 71 (homogeneous and heterogeneous ensemble methods; book p. 5-4).",
    "SRC_GB": f"{NF} (Gradient Boosting is only listed in the syllabus/contents on p. 68 of {B}; no explanation was found in the text.)",
    "SRC_BAGBOOST": f"{B}, pp. 75–77 (bagging: bootstrapping and aggregation; boosting; book pp. 5-8 to 5-10). Comparison table is standard.",
    # Unit 4 (book Unit VI, PDF p = book 6-(p-85))
    "SRC_RL": f"{B}, pp. 87–94 (Sec. 6.1 What is RL, need, elements, real-time applications; Sec. 6.2–6.3 types, positive vs negative reinforcement; book pp. 6-2 to 6-9).",
    "SRC_SUL": f"{B}, p. 92 (Sec. 6.1.6 Difference between Supervised, Unsupervised and Reinforced Learning; book p. 6-7).",
    "SRC_Q": f"{B}, pp. 99–101 (Sec. 6.5 Q Learning; book pp. 6-14 to 6-16). The numerical update example is a standard illustration.",
    "SRC_MDP": f"{B}, pp. 94–99 (Sec. 6.4 Markov Decision Process, Markov property, Bellman equation; book pp. 6-9 to 6-14).",
    "SRC_TERMS": f"{B}, pp. 95–101 (Markov property p. 95, Markov chain pp. 96–97, Markov reward process p. 98, Bellman equation pp. 98–99, Q-table / Q-function pp. 100–101; book pp. 6-10 to 6-16).",
}

GAPS = {
    1: "All Unit 1 topics were found in your textbooks (Classification in ML Unit 3-6.pdf; regression metrics and Bayesian Linear Regression in ML Textbook.pdf, Unit II). No ⚠ flags. Only the name 'hard margin' does not appear in the OCR text of the textbook.",
    2: "All Unit 2 topics were found in `ML Unit 3-6.pdf` (Unit IV); no ⚠ flags.",
    3: "**⚠ Not found:** U3-7 Gradient Boosting is only listed in the syllabus (p. 68); the answer is a standard textbook answer.",
    4: "All Unit 4 topics were found in `ML Unit 3-6.pdf` (Unit VI); no ⚠ flags.",
    "A": "**⚠ Topics not found in your materials:** U3-7 Gradient Boosting (syllabus listing only).",
}
