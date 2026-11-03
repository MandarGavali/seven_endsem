# Canonical PYQ data for Machine Learning (417521), SPPU 2019 pattern.
# Each raw = (paper, qno, marks, exact wording). Paper unit = Q1/2 -> Unit 1, Q3/4 -> 2, Q5/6 -> 3, Q7/8 -> 4.

PAPERS = [
    ("Nov_Dec_2023", "Nov-Dec 2023", "[6181]-404, P6779", "PYQ/Machine Learning/Nov_Dec_2023.pdf"),
    ("Nov_Dec_2024", "Nov-Dec 2024", "[6354]-781, PC2632", "PYQ/Machine Learning/Nov_Dec_2024.pdf"),
    ("Nov_Dec_2025", "Nov-Dec 2025", "[6584]-383, PE2433", "PYQ/Machine Learning/Nov_Dec_2025.pdf"),
]

UNITS = {
    1: "Supervised Learning: Classification & Regression (Syllabus Unit III)",
    2: "Unsupervised Learning: Clustering (Syllabus Unit IV)",
    3: "Ensemble Learning (Syllabus Unit V)",
    4: "Reinforcement Learning (Syllabus Unit VI)",
}

Q = [
 # ---------------- UNIT 1 ----------------
 dict(id="U1-1", unit=1, q="Explain the K-Nearest Neighbour (KNN) classification algorithm with a suitable example (including numerical).",
      raw=[("2023","Q1(a)",12,"Apply K-Nearest Neighbor Algorithm (KNN) on following data. Predict the student result for values physics = 6 marks, Chemistry = 8 marks. Consider number of neighbours K = 3 and Euclidean Distance as distance measure."),
           ("2024","Q2(c)",8,"Write a detailed note on K Nearest Neighbour algorithm with suitable example."),
           ("2025","Q1(b)",6,"Explain K nearest neighbor classification algorithm with suitable example.")]),
 dict(id="U1-2", unit=1, q="Evaluation measures of binary classification: accuracy, precision, recall, F1-score (formula + numerical on confusion matrix).",
      raw=[("2023","Q2(a)",6,"Explain any 4 evaluation measures of Binary classification with example?"),
           ("2024","Q1(b)",12,"Write formula for accuracy, precision, recall and f1-score. Calculate accuracy, precision, recall and f1-score for given example. (Confusion matrix: Predicted Cancer -> 45 actual Cancer, 18 actual No Cancer; Predicted No Cancer -> 12 actual Cancer, 25 actual No Cancer)")]),
 dict(id="U1-3", unit=1, q="What are kernel functions in SVM? Describe Linear, Polynomial, Radial Basis (Gaussian) and Sigmoid kernels.",
      raw=[("2024","Q1(a)",6,"What are kernel functions in SVM? Describe the Radial Basis Kernel, and Sigmoid kernel."),
           ("2025","Q1(c)",6,"What are kernel functions in SVM? Describe the Radial Basis Kernel, Gaussian, Polynomial, and Sigmoid kernel")]),
 dict(id="U1-4", unit=1, q="Differentiate between Balanced and Imbalanced classification.",
      raw=[("2024","Q2(b)",6,"Differentiate Balanced and Imbalanced Classification."),
           ("2025","Q2(b)",6,"Differentiate between balanced and imbalanced classification.")]),
 dict(id="U1-5", unit=1, q="Explain the Support Vector Machine (SVM) classification algorithm with a suitable example.",
      raw=[("2023","Q1(b)",6,"Explain support Vector Machine classification algorithm with suitable example.")]),
 dict(id="U1-6", unit=1, q="Explain the concept of soft margin SVM. How does it differ from hard margin SVM?",
      raw=[("2025","Q2(c)",6,"Explain the concept of a soft margin SVM. How does it differ from a hard margin SVM?")]),
 dict(id="U1-7", unit=1, q="Explain construction of a multi-class classifier: (i) One-vs-All (ii) One-vs-One.",
      raw=[("2023","Q2(b)",6,"Explain construction of multi-classifier. i) One Vs. All approach ii) One Vs One approach")]),
 dict(id="U1-8", unit=1, q="Differentiate between Binary and Multiclass classification.",
      raw=[("2023","Q2(c)",6,"Differentiate between Binary - vs - Multiclass Classification.")]),
 dict(id="U1-9", unit=1, q="Explain any 4 evaluation measures of Multiclass classification.",
      raw=[("2024","Q2(a)",4,"Explain any 4 evaluation measures of Multiclass classification.")]),
 dict(id="U1-10", unit=1, q="Explain evaluation measures (SSE, MSE) for a regression model, with numerical.",
      raw=[("2025","Q1(a)",6,"Explain evaluation measures (SSE, MSE) for regression model. For a given data having 100 examples, if squared errors SE1, SE2, and SE3 are 13.33, 3.33 and 4.00 respectively, calculate Mean Squared Error (MSE). State the formula for MSE.")]),
 dict(id="U1-11", unit=1, q="Explain Bayesian Linear Regression.",
      raw=[("2025","Q2(a)",6,"Explain Baysian Linear Regression.")]),
 # ---------------- UNIT 2 ----------------
 dict(id="U2-1", unit=2, q="Explain the K-Means (centroid-based) clustering algorithm with example. State its advantages and disadvantages.",
      raw=[("2023","Q3(a)",9,"Explain K - Means clustering algorithm and states the advantages and disadvantages of k-means clustering algorithm."),
           ("2024","Q4(b)",9,"Describe centroid based clustering algorithm and explain any one type with example."),
           ("2025","Q4(b)",8,"Explain the K-Means clustering algorithm. What are its advantages and disadvantages.")]),
 dict(id="U2-2", unit=2, q="Explain the DBSCAN algorithm. How does it work? State its advantages and disadvantages.",
      raw=[("2024","Q4(a)",8,"Explain DBSCAN algorithm with advantages and disadvantages."),
           ("2025","Q3(a)",9,"Explain the DBSCAN algorithm. How does it work? What are its advantages and disadvantages.")]),
 dict(id="U2-3", unit=2, q="Describe the Gaussian Mixture Model (GMM) for distribution-based clustering with example. How is it different from other clustering algorithms?",
      raw=[("2023","Q3(b)",8,"Explain Gaussian mixture model with example."),
           ("2025","Q4(a)",9,"Describe the Gaussian Mixture Model (GMM) for distribution-based clustering. How is it different from other clustering algorithms?")]),
 dict(id="U2-4", unit=2, q="What is clustering? Elaborate the types of clustering.",
      raw=[("2024","Q3(b)",9,"What is clustering? Elaborate Types of Clustering.")]),
 dict(id="U2-5", unit=2, q="Elaborate the need of clustering and explain how the elbow method is used to decide the value of k.",
      raw=[("2023","Q4(a)",9,"Elaborate need of clustering and explain how the elbow method is used to decide the value of cluster k.")]),
 dict(id="U2-6", unit=2, q="Differentiate Agglomerative Hierarchical Clustering and Divisive Hierarchical Clustering.",
      raw=[("2024","Q3(a)",8,"Differentiate Agglomerative Hierarchical Clustering and Divisive Hierarchical Clustering.")]),
 dict(id="U2-7", unit=2, q="Explain the Divisive Hierarchical Clustering (DHC) algorithm with example.",
      raw=[("2023","Q4(b)",8,"Explain Divisive Hierarchical clustering (DHC) algorithm with example.")]),
 dict(id="U2-8", unit=2, q="Discuss applications of clustering in market segmentation, social network analysis, image segmentation and anomaly detection, with examples.",
      raw=[("2025","Q3(b)",8,"Discuss the applications of clustering techniques in market segmentaion, social network analysis, image segmentation, and anomaly detection. Provide examples for each application.")]),
 # ---------------- UNIT 3 ----------------
 dict(id="U3-1", unit=3, q="What is ensemble learning? Explain its need, advantages and limitations, and any two ensemble techniques.",
      raw=[("2023","Q6(b)",6,"What is the ensemble learning? Explain any two ensemble learning techniques."),
           ("2024","Q5(a)",9,"Explain Following with respect to Ensemble learning. i) Need of Ensemble Learning ii) Advantages of Ensemble methods iii) Ensemble learning limitations"),
           ("2025","Q5(a)",6,"Explain the concept of ensemble learning. Why is ensemble learning considered beneficial in machine learning?")]),
 dict(id="U3-2", unit=3, q="Explain the voting ensemble and the different types of voting mechanisms.",
      raw=[("2023","Q5(b)",6,"Explain different types of voting mechanisms in ensemble learning."),
           ("2024","Q6(b)",9,"Explain any three voting mechanism in ensemble learning."),
           ("2025","Q6(b)",6,"Describe the concept of a voting ensemble. What are the different types of voting techniques?")]),
 dict(id="U3-3", unit=3, q="Explain the stacking approach of ensemble learning with example. What methods are used for variance reduction in stacking?",
      raw=[("2024","Q5(b)",9,"Elaborate stacking approach of ensemble with example."),
           ("2025","Q5(b)",6,"Discuss the concept of stacking in ensemble learning. What are the different methods used for variance reduction in stacking?")]),
 dict(id="U3-4", unit=3, q="Explain the Adaptive Boosting (AdaBoost) algorithm in detail.",
      raw=[("2023","Q5(c)",6,"Explain AdaBoost algorithm in detail."),
           ("2025","Q6(c)",6,"Explain the Adaptive Boosting (AdaBoost) algorithm in detail.")]),
 dict(id="U3-5", unit=3, q="Explain the Random Forest ensemble method with an example.",
      raw=[("2023","Q6(c)",6,"Explain random forest ensembles with an example."),
           ("2025","Q5(c)",6,"Describe the Random Forest ensemble method in detail.")]),
 dict(id="U3-6", unit=3, q="Differentiate between Homogeneous and Heterogeneous ensemble methods, with examples.",
      raw=[("2023","Q6(a)",6,"Compare Homogeneous and Heterogeneous ensemble methods."),
           ("2025","Q6(a)",6,"Differentiate between homogeneous and heterogeneous ensemble methods. provide examples of each type.")]),
 dict(id="U3-7", unit=3, q="Explain Gradient Boosting ensemble learning technique.",
      raw=[("2024","Q6(a)",9,"Describe ensemble learning. Explain Gradient Boosting ensemble learning techniques.")]),
 dict(id="U3-8", unit=3, q="Differentiate the Bagging and Boosting approaches of ensemble learning.",
      raw=[("2023","Q5(a)",6,"Differentiate the Bagging and Boosting approach of ensemble learning.")]),
 # ---------------- UNIT 4 ----------------
 dict(id="U4-1", unit=4, q="What is Reinforcement Learning? Explain its need/importance, types and real-time applications.",
      raw=[("2023","Q8(a)",8,"What is Reinforcement Learning? Explain the real time applications of reinforcement learning."),
           ("2024","Q7(b)",9,"Explain Reinforcement Learning need and its types in detail?"),
           ("2025","Q7(a)",9,"Define reinforcement learning. Why is reinforcement learning important in the field of machine learning?")]),
 dict(id="U4-2", unit=4, q="Compare supervised, unsupervised and reinforcement learning with examples.",
      raw=[("2023","Q8(b)",9,"Explain following terms: i) Supervised Learning. ii) Unsupervised Learning. iii) Reinforcement Learning."),
           ("2024","Q7(a)",8,"Differentiate supervised and unsupervised learning with example."),
           ("2025","Q8(b)",8,"Compare and contrast supervised, unsupervised, and reinforcement learning. Provide examples of each type.")]),
 dict(id="U4-3", unit=4, q="Explain the Q-Learning algorithm: important terms, working, and an example.",
      raw=[("2023","Q7(b)",9,"Explain Q-Learning algorithm with an example."),
           ("2025","Q8(a)",9,"Introduce Q-learning. What are the important terms used in Q-learning? How does Q-learning work?")]),
 dict(id="U4-4", unit=4, q="Explain the Markov property and Markov Decision Process (MDP). How does the Markov property relate to RL and why is it important?",
      raw=[("2024","Q8(b)",9,"How does the Markov property relate to Reinforcement Learning? Why is it important?"),
           ("2025","Q7(b)",8,"Explain Markov's Decision Process (MDP). What is the Markov property in the context of MDP?")]),
 dict(id="U4-5", unit=4, q="Explain the terms: Markov Property, Markov Chain, Markov Reward Process, Bellman Equation, Q-table, Q-function.",
      raw=[("2023","Q7(a)",8,"Explain following terms: i) Markov Property ii) Bellman Equation iii) Markov Reward Process iv) Markov Chain"),
           ("2024","Q8(a)",8,"Explain following terms: i) Belman Equation ii) Markov Chain iii) Q table iv) Q function")]),
]

def years(c): return sorted({r[0] for r in c["raw"]})
def maxm(c): return max(r[2] for r in c["raw"])
def stars(c):
    n = len(years(c))
    if n >= 3 or (n == 2 and maxm(c) >= 8): return 3
    if n == 2: return 2
    return 1
STAR = {3: "★★★", 2: "★★", 1: "★"}
