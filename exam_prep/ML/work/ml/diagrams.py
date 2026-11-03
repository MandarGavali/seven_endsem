"""Simple, hand-redrawable diagrams for the ML answer docs (matplotlib)."""
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Ellipse, Circle

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diagrams")
os.makedirs(OUT, exist_ok=True)
BLUE, ORANGE, GREEN, GREY, RED = "#2E74B5", "#ED7D31", "#70AD47", "#7F7F7F", "#C00000"


def save(fig, name):
    fig.savefig(os.path.join(OUT, name + ".png"), dpi=170, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def box(ax, x, y, text, w=2.6, h=0.8, fc="#DEEBF7", ec=BLUE, fs=9):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.05", fc=fc, ec=ec, lw=1.4))
    ax.text(x, y, text, ha="center", va="center", fontsize=fs, wrap=True)


def arrow(ax, a, b, text=None, color="black", fs=8, rad=0.0):
    ax.annotate("", xy=b, xytext=a, arrowprops=dict(arrowstyle="-|>", color=color, lw=1.3,
                                                     connectionstyle=f"arc3,rad={rad}"))
    if text:
        ax.text((a[0] + b[0]) / 2, (a[1] + b[1]) / 2 + 0.12, text, ha="center", fontsize=fs, color=color)


def canvas(w, h, xl, yl):
    fig, ax = plt.subplots(figsize=(w, h)); ax.set_xlim(*xl); ax.set_ylim(*yl); ax.axis("off")
    return fig, ax


def flow(name, steps, w=3.6, fs=9, decision=None):
    """Vertical flowchart of steps; decision=(index, 'loop text', back_to_index)."""
    n = len(steps); fig, ax = canvas(5.2, 0.95 * n + 0.4, (0, 6), (0, n + 0.2))
    ys = [n - i - 0.4 for i in range(n)]
    for i, (s, y) in enumerate(zip(steps, ys)):
        fc = "#FFF2CC" if decision and i == decision[0] else ("#E2EFDA" if i in (0, n - 1) else "#DEEBF7")
        box(ax, 3, y, s, w=w, h=0.62, fc=fc, fs=fs)
        if i: arrow(ax, (3, ys[i - 1] - 0.31), (3, y + 0.31))
    if decision:
        i, txt, j = decision
        ax.annotate("", xy=(3 + w / 2, ys[j]), xytext=(3 + w / 2, ys[i]),
                    arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.3, connectionstyle="arc3,rad=0.5"))
        ax.text(3 + w / 2 + 0.55, (ys[i] + ys[j]) / 2, txt, color=RED, fontsize=8, rotation=90, va="center")
    save(fig, name)


# ---------------- Unit 1 ----------------
def knn():
    pts = [((4, 3), "Fail"), ((6, 7), "Pass"), ((7, 8), "Pass"), ((5, 5), "Fail"), ((8, 8), "Pass")]
    fig, ax = plt.subplots(figsize=(5, 3.8))
    for (x, y), lab in pts:
        ax.scatter(x, y, s=90, c=GREEN if lab == "Pass" else RED, marker="o" if lab == "Pass" else "s", zorder=3)
        dx, dy = {(7, 8): (-0.2, 0.35), (8, 8): (0.15, -0.45)}.get((x, y), (0.12, -0.35))
        ax.text(x + dx, y + dy, f"({x},{y}) {lab}", fontsize=8)
    ax.scatter(6, 8, s=160, c="gold", marker="*", edgecolors="k", zorder=4); ax.text(4.2, 8.3, "Query (6,8) ?", fontsize=9)
    ax.add_patch(Circle((6, 8), 2.05, fill=False, ls="--", ec=BLUE)); ax.text(3.7, 9.6, "K = 3 nearest", color=BLUE, fontsize=8)
    ax.set_xlabel("Physics marks"); ax.set_ylabel("Chemistry marks"); ax.set_xlim(2.5, 10); ax.set_ylim(2, 10.5)
    ax.set_aspect("equal"); ax.grid(alpha=.3); save(fig, "knn")


def confusion():
    fig, ax = canvas(4.6, 3.0, (0, 6), (0, 4))
    ax.text(3.75, 3.7, "Actual", ha="center", fontsize=10, weight="bold")
    ax.text(0.35, 1.5, "Predicted", rotation=90, va="center", fontsize=10, weight="bold")
    for j, t in enumerate(["Positive", "Negative"]): ax.text(2.75 + 2 * j, 3.25, t, ha="center", fontsize=9)
    for i, t in enumerate(["Positive", "Negative"]): ax.text(1.2, 2.2 - 1.4 * i, t, ha="center", va="center", fontsize=9)
    cells = [["TP", "FP"], ["FN", "TN"]]; col = [["#E2EFDA", "#FCE4D6"], ["#FCE4D6", "#E2EFDA"]]
    for i in range(2):
        for j in range(2):
            ax.add_patch(plt.Rectangle((1.75 + 2 * j, 1.5 - 1.4 * i), 2, 1.4, fc=col[i][j], ec="k"))
            ax.text(2.75 + 2 * j, 2.2 - 1.4 * i, cells[i][j], ha="center", va="center", fontsize=13, weight="bold")
    save(fig, "confusion")


def svm():
    rng = np.random.default_rng(1)
    a = rng.normal([2, 2], .45, (12, 2)); b = rng.normal([5, 5], .45, (12, 2))
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.scatter(*a.T, c=BLUE, label="Class −1"); ax.scatter(*b.T, c=ORANGE, marker="s", label="Class +1")
    x = np.linspace(0, 7, 10)
    ax.plot(x, 7 - x, "k-", label="Hyperplane w·x + b = 0")
    ax.plot(x, 5.8 - x, "k--", lw=1); ax.plot(x, 8.2 - x, "k--", lw=1)
    ax.scatter([2.9, 4.1], [2.9, 4.1], s=200, facecolors="none", edgecolors=RED, lw=2, label="Support vectors")
    ax.annotate("", xy=(4.1, 4.1), xytext=(3.5, 3.5), arrowprops=dict(arrowstyle="<->", color=GREEN))
    ax.text(3.9, 3.2, "margin = 2/‖w‖", color=GREEN, fontsize=9)
    ax.set_xlim(0, 7); ax.set_ylim(0, 7); ax.legend(fontsize=7, loc="upper right"); ax.set_xlabel("x1"); ax.set_ylabel("x2")
    save(fig, "svm")


def kernel():
    fig, axs = plt.subplots(1, 2, figsize=(7.5, 3.2))
    rng = np.random.default_rng(2)
    inner = rng.normal(0, .5, (25, 2)); th = rng.uniform(0, 2 * np.pi, 30)
    outer = np.c_[2.2 * np.cos(th), 2.2 * np.sin(th)] + rng.normal(0, .15, (30, 2))
    axs[0].scatter(*inner.T, c=BLUE); axs[0].scatter(*outer.T, c=ORANGE, marker="s")
    axs[0].set_title("Input space: not linearly separable", fontsize=9); axs[0].set_aspect("equal")
    r_in, r_out = (inner ** 2).sum(1), (outer ** 2).sum(1)
    axs[1].scatter(inner[:, 0], r_in, c=BLUE); axs[1].scatter(outer[:, 0], r_out, c=ORANGE, marker="s")
    axs[1].axhline(2.2, color="k", ls="--"); axs[1].set_title("Feature space φ(x) = (x1, x1²+x2²): linear", fontsize=9)
    fig.text(0.5, 0.5, "φ →", fontsize=16, ha="center"); save(fig, "kernel")


def softmargin():
    rng = np.random.default_rng(3)
    a = rng.normal([2, 2], .5, (12, 2)); b = rng.normal([5, 5], .5, (12, 2))
    fig, axs = plt.subplots(1, 2, figsize=(7.5, 3.3))
    x = np.linspace(0, 7, 10)
    for ax, t, extra in ((axs[0], "Hard margin: no point inside margin", False), (axs[1], "Soft margin: slack ξ allows violations", True)):
        ax.scatter(*a.T, c=BLUE); ax.scatter(*b.T, c=ORANGE, marker="s")
        ax.plot(x, 7 - x, "k-"); ax.plot(x, (5.8 if not extra else 5.2) - x, "k--", lw=1); ax.plot(x, (8.2 if not extra else 8.8) - x, "k--", lw=1)
        if extra:
            ax.scatter([4.2], [3.6], c=BLUE); ax.scatter([3.1], [3.3], c=ORANGE, marker="s")
            ax.text(4.3, 3.0, "ξ > 0", color=RED, fontsize=9)
        ax.set_title(t, fontsize=9); ax.set_xlim(0, 7); ax.set_ylim(0, 7)
    save(fig, "softmargin")


def ova_ovo():
    fig, ax = canvas(7.5, 3.0, (0, 10), (0, 4))
    ax.text(2.5, 3.7, "One-vs-All (N classifiers)", ha="center", weight="bold", fontsize=9)
    for i, t in enumerate(["A vs {B,C}", "B vs {A,C}", "C vs {A,B}"]): box(ax, 2.5, 2.9 - i * 0.9, t, w=2.6, h=0.6, fs=8.5)
    ax.text(2.5, 0.15, "Pick class with highest score", ha="center", fontsize=8, color=RED)
    ax.text(7.5, 3.7, "One-vs-One (N(N−1)/2 classifiers)", ha="center", weight="bold", fontsize=9)
    for i, t in enumerate(["A vs B", "A vs C", "B vs C"]): box(ax, 7.5, 2.9 - i * 0.9, t, w=2.6, h=0.6, fc="#FFF2CC", ec=ORANGE, fs=8.5)
    ax.text(7.5, 0.15, "Majority vote of all pairs", ha="center", fontsize=8, color=RED)
    save(fig, "ova_ovo")


def imbalance():
    fig, axs = plt.subplots(1, 2, figsize=(6.5, 2.6))
    axs[0].bar(["Class A", "Class B"], [50, 50], color=[BLUE, ORANGE]); axs[0].set_title("Balanced (50 : 50)", fontsize=9)
    axs[1].bar(["Normal", "Fraud"], [98, 2], color=[BLUE, ORANGE]); axs[1].set_title("Imbalanced (98 : 2)", fontsize=9)
    for a in axs: a.set_ylabel("% samples", fontsize=8)
    save(fig, "imbalance")


def regression_error():
    x = np.array([1, 2, 3, 4, 5]); y = np.array([2.2, 2.8, 4.5, 4.4, 6.1]); yh = 0.95 * x + 1.1
    fig, ax = plt.subplots(figsize=(4.8, 3.2))
    ax.scatter(x, y, c=BLUE, zorder=3, label="Actual yᵢ"); ax.plot(x, yh, c=ORANGE, label="Predicted ŷᵢ")
    for xi, a, b in zip(x, y, yh): ax.plot([xi, xi], [a, b], "r--", lw=1)
    ax.text(3.1, 3.6, "error eᵢ = yᵢ − ŷᵢ", color=RED, fontsize=8); ax.legend(fontsize=8); ax.set_xlabel("x"); ax.set_ylabel("y")
    save(fig, "regression_error")


def bayes_reg():
    rng = np.random.default_rng(4); x = np.linspace(0, 5, 12); y = 1 + 0.8 * x + rng.normal(0, .5, 12)
    fig, ax = plt.subplots(figsize=(4.8, 3.2)); ax.scatter(x, y, c=BLUE, zorder=3, label="Data")
    xs = np.linspace(0, 5, 50)
    for _ in range(12):
        w0, w1 = rng.normal(1, .25), rng.normal(.8, .07); ax.plot(xs, w0 + w1 * xs, c=ORANGE, alpha=.25)
    ax.plot(xs, 1 + .8 * xs, c="k", label="Posterior mean line")
    ax.fill_between(xs, .4 + .8 * xs - .1 * xs, 1.6 + .8 * xs + .1 * xs, color=ORANGE, alpha=.12, label="Uncertainty band")
    ax.legend(fontsize=7); save(fig, "bayes_reg")


# ---------------- Unit 2 ----------------
def kmeans():
    rng = np.random.default_rng(5)
    c = np.array([[2, 2], [6, 6], [2, 6.5]]); cols = [BLUE, ORANGE, GREEN]
    fig, ax = plt.subplots(figsize=(4.6, 3.8))
    for k, (cc, col) in enumerate(zip(c, cols)):
        p = rng.normal(cc, .7, (15, 2)); ax.scatter(*p.T, c=col, s=20)
        ax.scatter(*cc, marker="X", s=220, c=col, edgecolors="k"); ax.text(cc[0] + .3, cc[1] + .4, f"C{k + 1}", fontsize=9, weight="bold")
    ax.set_title("K = 3 clusters; X = centroids", fontsize=9); ax.set_xlabel("x1"); ax.set_ylabel("x2"); save(fig, "kmeans")


def elbow():
    k = np.arange(1, 10); wcss = [1000, 600, 300, 230, 190, 165, 150, 140, 133]
    fig, ax = plt.subplots(figsize=(4.8, 3.2)); ax.plot(k, wcss, "o-", c=BLUE)
    ax.annotate("Elbow → optimal k = 3", xy=(3, 300), xytext=(4.5, 650), arrowprops=dict(arrowstyle="->", color=RED), color=RED)
    ax.set_xlabel("Number of clusters k"); ax.set_ylabel("WCSS (inertia)"); ax.grid(alpha=.3); save(fig, "elbow")


def dbscan():
    fig, ax = plt.subplots(figsize=(5, 3.6))
    core = np.array([[2, 2], [2.6, 2.3], [2.2, 2.8], [1.6, 2.5], [2.9, 2.9]])
    ax.scatter(*core.T, c=BLUE, s=60, label="Core point (≥ MinPts in ε)")
    ax.add_patch(Circle((2, 2), 0.9, fill=False, ec=BLUE, ls="--")); ax.text(1.1, 1.0, "ε-radius", color=BLUE, fontsize=8)
    ax.scatter([3.7], [3.4], c=ORANGE, s=60, marker="s", label="Border point"); ax.add_patch(Circle((3.7, 3.4), 0.9, fill=False, ec=ORANGE, ls=":"))
    ax.scatter([6, 5.5], [1, 4.8], c=RED, s=60, marker="x", label="Noise / outlier")
    ax.set_xlim(0, 7); ax.set_ylim(0, 5.5); ax.set_aspect("equal"); ax.legend(fontsize=7, loc="upper right"); save(fig, "dbscan")


def gmm():
    rng = np.random.default_rng(6); fig, ax = plt.subplots(figsize=(5, 3.6))
    for m, cov, col in (([2, 2], [[1, .6], [.6, .8]], BLUE), ([6, 4], [[.6, -.3], [-.3, 1.2]], ORANGE)):
        p = rng.multivariate_normal(m, cov, 60); ax.scatter(*p.T, s=10, c=col)
        vals, vecs = np.linalg.eigh(cov); ang = np.degrees(np.arctan2(*vecs[:, 1][::-1]))
        for s in (1, 2): ax.add_patch(Ellipse(m, 2 * s * np.sqrt(vals[1]), 2 * s * np.sqrt(vals[0]), angle=ang, fill=False, ec=col, lw=1.4))
        ax.scatter(*m, marker="+", s=150, c="k")
    ax.text(0.2, 5.6, "Each cluster = Gaussian N(μₖ, Σₖ) with weight πₖ", fontsize=8)
    ax.set_xlim(-1, 9); ax.set_ylim(-1, 6.5); save(fig, "gmm")


def dendro():
    fig, ax = plt.subplots(figsize=(5.4, 3.4)); xs = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}
    def link(x1, x2, h1, h2, h):
        ax.plot([x1, x1, x2, x2], [h1, h, h, h2], c=BLUE, lw=1.6)
    link(1, 2, 0, 0, 1); link(4, 5, 0, 0, 1.5); link(3, 4.5, 0, 1.5, 2.5); link(1.5, 3.75, 1, 2.5, 4)
    ax.set_xticks(list(xs.values())); ax.set_xticklabels(xs.keys()); ax.set_ylabel("Distance")
    ax.annotate("", xy=(5.6, 4), xytext=(5.6, 0.2), arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=1.5))
    ax.text(5.7, 1.8, "Agglomerative\n(bottom-up: merge)", color=GREEN, fontsize=7.5)
    ax.annotate("", xy=(0.4, 0.2), xytext=(0.4, 4), arrowprops=dict(arrowstyle="-|>", color=RED, lw=1.5))
    ax.text(-0.75, 1.8, "Divisive\n(top-down: split)", color=RED, fontsize=7.5)
    ax.set_xlim(-0.9, 6.9); ax.spines[["top", "right"]].set_visible(False); save(fig, "dendrogram")


def divisive():
    fig, ax = canvas(6.5, 3.2, (0, 10), (0, 4))
    box(ax, 5, 3.4, "{A, B, C, D, E}", w=3, h=0.6)
    box(ax, 2.8, 2.2, "{A, B}", w=2, h=0.6); box(ax, 7.2, 2.2, "{C, D, E}", w=2.4, h=0.6)
    arrow(ax, (5, 3.1), (2.8, 2.5)); arrow(ax, (5, 3.1), (7.2, 2.5))
    box(ax, 6.0, 1.0, "{C}", w=1.4, h=0.6); box(ax, 8.4, 1.0, "{D, E}", w=1.8, h=0.6)
    arrow(ax, (7.2, 1.9), (6.0, 1.3)); arrow(ax, (7.2, 1.9), (8.4, 1.3))
    box(ax, 1.8, 1.0, "{A}", w=1.2, h=0.6); box(ax, 3.8, 1.0, "{B}", w=1.2, h=0.6)
    arrow(ax, (2.8, 1.9), (1.8, 1.3)); arrow(ax, (2.8, 1.9), (3.8, 1.3))
    ax.text(5, 0.1, "Split the cluster with largest diameter until each point is alone (or k clusters)", ha="center", fontsize=8, color=RED)
    save(fig, "divisive")


def cluster_types():
    fig, ax = canvas(7.5, 2.8, (0, 10), (0, 3.4))
    box(ax, 5, 2.9, "Clustering methods", w=3, h=0.6, fc="#E2EFDA", ec=GREEN)
    items = ["Partitioning /\nCentroid\n(K-Means)", "Hierarchical\n(AGNES, DIANA)", "Density\n(DBSCAN)", "Distribution\n(GMM)", "Grid / Fuzzy\n(STING, FCM)"]
    for i, t in enumerate(items):
        x = 1 + i * 2; box(ax, x, 1.1, t, w=1.8, h=1.1, fs=8); arrow(ax, (5, 2.6), (x, 1.66))
    save(fig, "cluster_types")


def cluster_apps():
    fig, ax = canvas(6.5, 3.2, (0, 10), (0, 5))
    box(ax, 5, 2.5, "Clustering", w=2.4, h=0.8, fc="#E2EFDA", ec=GREEN)
    for (x, y, t) in ((1.8, 4.3, "Market\nsegmentation"), (8.2, 4.3, "Social network\nanalysis"), (1.8, 0.7, "Image\nsegmentation"), (8.2, 0.7, "Anomaly\ndetection")):
        box(ax, x, y, t, w=2.6, h=0.9, fs=8.5); arrow(ax, (5, 2.5), (x + (0.9 if x < 5 else -0.9), y + (-0.45 if y > 2.5 else 0.45)))
    save(fig, "cluster_apps")


# ---------------- Unit 3 ----------------
def ensemble():
    fig, ax = canvas(7, 3.4, (0, 10), (0, 5))
    box(ax, 1.2, 2.5, "Training\ndata D", w=1.8, h=1.0, fc="#E2EFDA", ec=GREEN)
    for i in range(3):
        y = 4.1 - i * 1.6; box(ax, 4.5, y, f"Model {i + 1}", w=2.0, h=0.7); arrow(ax, (2.1, 2.5), (3.5, y))
        arrow(ax, (5.5, y), (7.0, 2.5))
    box(ax, 7.9, 2.5, "Combine\n(vote / avg)", w=1.8, h=1.0, fc="#FFF2CC", ec=ORANGE)
    ax.text(9.15, 2.5, "→ Final\nprediction", fontsize=8.5, va="center")
    save(fig, "ensemble")


def voting():
    fig, ax = canvas(7, 3.0, (0, 10), (0, 4.4))
    box(ax, 1, 2.2, "Input x", w=1.6, h=0.7, fc="#E2EFDA", ec=GREEN)
    outs = [("Logistic Reg.", "Class A (0.7)"), ("Decision Tree", "Class B (0.6)"), ("SVM / KNN", "Class A (0.8)")]
    for i, (m, o) in enumerate(outs):
        y = 3.7 - i * 1.5; box(ax, 3.6, y, m, w=2.2, h=0.65); arrow(ax, (1.8, 2.2), (2.5, y))
        ax.text(5.0, y, o, fontsize=8, va="center"); arrow(ax, (6.5, y), (7.3, 2.2))
    box(ax, 8.4, 2.2, "Hard vote: A (2 of 3)\nSoft vote: argmax\navg probability", w=2.6, h=1.2, fc="#FFF2CC", ec=ORANGE, fs=8)
    save(fig, "voting")


def stacking():
    fig, ax = canvas(7, 3.6, (0, 10), (0, 5))
    box(ax, 1.1, 2.5, "Training\ndata", w=1.8, h=1.0, fc="#E2EFDA", ec=GREEN)
    for i, t in enumerate(["Base 1: KNN", "Base 2: Decision Tree", "Base 3: SVM"]):
        y = 4.2 - i * 1.7; box(ax, 4.0, y, t, w=2.6, h=0.7); arrow(ax, (2.0, 2.5), (2.7, y)); arrow(ax, (5.3, y), (6.3, 2.5))
    ax.text(5.9, 3.8, "Level-0\npredictions\n(out-of-fold)", fontsize=7.5, color=GREY)
    box(ax, 7.3, 2.5, "Meta-learner\n(Logistic Reg.)", w=2.0, h=1.0, fc="#FFF2CC", ec=ORANGE)
    ax.text(8.45, 2.5, "→ Final", fontsize=9, va="center"); ax.text(4.0, 0.0, "Level-0 (base learners)", ha="center", fontsize=8)
    ax.text(7.3, 1.6, "Level-1", ha="center", fontsize=8); save(fig, "stacking")


def boosting():
    fig, ax = canvas(7.5, 2.6, (0, 11), (0, 3.4))
    for i in range(3):
        x = 1.4 + i * 3.6
        box(ax, x, 2.4, f"Weighted data D{i + 1}", w=2.4, h=0.6, fc="#E2EFDA", ec=GREEN, fs=8)
        box(ax, x, 1.2, f"Weak learner h{i + 1}\n(stump), α{i + 1}", w=2.4, h=0.8, fs=8)
        arrow(ax, (x, 2.1), (x, 1.6))
        if i < 2: arrow(ax, (x + 1.2, 1.2), (x + 2.4, 2.4), color=RED)
    ax.text(5.5, 3.05, "Red arrows: weights of misclassified samples increase for the next learner", ha="center", fontsize=8, color=RED)
    ax.text(5.5, 0.15, "Final H(x) = sign( Σ αₜ hₜ(x) )", ha="center", fontsize=10, weight="bold")
    save(fig, "boosting")


def gradient_boost():
    fig, ax = canvas(7.5, 2.6, (0, 11), (0, 3.2))
    labels = ["F₀ = mean(y)", "Residuals\nr = y − F₀", "Tree h₁\nfits r", "F₁ = F₀ + η·h₁", "Repeat M\ntimes"]
    for i, t in enumerate(labels):
        x = 1.1 + i * 2.2; box(ax, x, 1.8, t, w=1.9, h=1.0, fs=8, fc="#FFF2CC" if i == 3 else "#DEEBF7")
        if i: arrow(ax, (x - 1.25, 1.8), (x - 0.95, 1.8))
    ax.annotate("", xy=(3.3, 1.25), xytext=(9.9, 1.25), arrowprops=dict(arrowstyle="-|>", color=RED, connectionstyle="arc3,rad=-0.3"))
    ax.text(6.6, 0.25, "new residuals each round (gradient of loss)", color=RED, fontsize=8, ha="center")
    save(fig, "gradient_boost")


def random_forest():
    fig, ax = canvas(7.5, 3.4, (0, 11), (0, 4.6))
    box(ax, 5.5, 4.1, "Training data (N rows, M features)", w=4.6, h=0.6, fc="#E2EFDA", ec=GREEN)
    for i in range(3):
        x = 1.8 + i * 3.7
        box(ax, x, 2.8, f"Bootstrap sample {i + 1}\n+ random √M features", w=3.0, h=0.8, fs=8); arrow(ax, (5.5, 3.8), (x, 3.2))
        ax.add_patch(plt.Polygon([[x, 2.1], [x - 0.6, 1.3], [x + 0.6, 1.3]], fc="#C5E0B4", ec=GREEN)); ax.text(x, 1.55, f"Tree {i + 1}", ha="center", fontsize=8)
        arrow(ax, (x, 2.4), (x, 2.1)); arrow(ax, (x, 1.3), (5.5, 0.6))
    box(ax, 5.5, 0.35, "Majority vote (classification) / Average (regression)", w=5.4, h=0.5, fc="#FFF2CC", ec=ORANGE, fs=8)
    save(fig, "random_forest")


def bag_vs_boost():
    fig, ax = canvas(7.5, 2.8, (0, 11), (0, 3.6))
    ax.text(2.6, 3.4, "Bagging (parallel)", ha="center", weight="bold", fontsize=9)
    for i in range(3):
        box(ax, 2.6, 2.6 - i * 0.85, f"Bootstrap {i + 1} → Model {i + 1}", w=3.6, h=0.55, fs=8)
    ax.text(2.6, 0.1, "Average / vote → ↓ variance", ha="center", fontsize=8, color=RED)
    ax.text(8.3, 3.4, "Boosting (sequential)", ha="center", weight="bold", fontsize=9)
    for i in range(3):
        box(ax, 8.3, 2.6 - i * 0.85, f"Model {i + 1} (focus on errors)", w=3.6, h=0.55, fc="#FFF2CC", ec=ORANGE, fs=8)
        if i: arrow(ax, (8.3, 2.6 - (i - 1) * 0.85 - 0.28), (8.3, 2.6 - i * 0.85 + 0.28))
    ax.text(8.3, 0.1, "Weighted sum → ↓ bias", ha="center", fontsize=8, color=RED)
    save(fig, "bag_vs_boost")


def homo_hetero():
    fig, ax = canvas(7.5, 2.6, (0, 11), (0, 3.4))
    ax.text(2.6, 3.15, "Homogeneous", ha="center", weight="bold", fontsize=9)
    for i in range(3): box(ax, 1.1 + i * 1.5, 2.1, "DT", w=1.2, h=0.6)
    ax.text(2.6, 1.2, "same algorithm,\ndifferent data samples\n(Bagging, RF, AdaBoost)", ha="center", fontsize=8)
    ax.text(8.3, 3.15, "Heterogeneous", ha="center", weight="bold", fontsize=9)
    for i, t in enumerate(["KNN", "SVM", "DT"]): box(ax, 6.8 + i * 1.5, 2.1, t, w=1.2, h=0.6, fc="#FFF2CC", ec=ORANGE)
    ax.text(8.3, 1.2, "different algorithms,\nsame data\n(Voting, Stacking)", ha="center", fontsize=8)
    save(fig, "homo_hetero")


# ---------------- Unit 4 ----------------
def rl_loop():
    fig, ax = canvas(5.6, 3.0, (0, 10), (0, 5))
    box(ax, 5, 4.0, "Agent\n(policy π)", w=3, h=1.1, fc="#E2EFDA", ec=GREEN, fs=10)
    box(ax, 5, 1.0, "Environment", w=3, h=1.1, fs=10)
    ax.annotate("", xy=(8.2, 1.0), xytext=(6.5, 4.0), arrowprops=dict(arrowstyle="-|>", lw=1.5, connectionstyle="arc3,rad=-0.4"))
    ax.text(8.4, 2.8, "Action aₜ", fontsize=9)
    ax.annotate("", xy=(3.5, 4.0), xytext=(3.5, 1.0), arrowprops=dict(arrowstyle="-|>", lw=1.5, color=BLUE, connectionstyle="arc3,rad=-0.4"))
    ax.text(0.2, 2.8, "State sₜ₊₁", fontsize=9, color=BLUE)
    ax.annotate("", xy=(4.4, 3.45), xytext=(4.4, 1.55), arrowprops=dict(arrowstyle="-|>", lw=1.5, color=ORANGE))
    ax.text(4.5, 2.4, "Reward rₜ₊₁", fontsize=9, color=ORANGE)
    save(fig, "rl_loop")


def learning_types():
    fig, ax = canvas(7.5, 2.6, (0, 11), (0, 3.2))
    box(ax, 5.5, 2.8, "Machine Learning", w=3, h=0.6, fc="#E2EFDA", ec=GREEN)
    for i, (t, s) in enumerate([("Supervised", "labelled data\n→ predict label"), ("Unsupervised", "unlabelled data\n→ find patterns"), ("Reinforcement", "rewards from env.\n→ learn policy")]):
        x = 1.8 + i * 3.7; box(ax, x, 1.6, t, w=2.6, h=0.6); arrow(ax, (5.5, 2.5), (x, 1.9)); ax.text(x, 0.55, s, ha="center", fontsize=8)
    save(fig, "learning_types")


def qlearning():
    flow("qlearning", ["Initialise Q(s,a) = 0 for all s, a", "Observe current state s", "Choose action a (ε-greedy)",
                       "Take a; get reward r, next state s′", "Q(s,a) ← Q(s,a) + α[r + γ·max Q(s′,a′) − Q(s,a)]",
                       "s ← s′ ; repeat until goal / episodes end"], w=5.2, fs=8.5, decision=(5, "next step", 1))


def mdp():
    fig, ax = canvas(6.4, 3.0, (0, 10), (0, 4.6))
    pos = {"S1\nClass": (1.5, 2.3), "S2\nStudy": (5, 3.7), "S3\nSleep": (5, 0.9), "S4\nPass": (8.6, 2.3)}
    for k, (x, y) in pos.items(): ax.add_patch(Circle((x, y), 0.65, fc="#DEEBF7", ec=BLUE, lw=1.4)); ax.text(x, y, k, ha="center", va="center", fontsize=8)
    def e(a, b, t, rad=0.15):
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.annotate("", xy=(x2 - 0.55 * np.sign(x2 - x1 or 1), y2), xytext=(x1 + 0.55 * np.sign(x2 - x1 or 1), y1),
                    arrowprops=dict(arrowstyle="-|>", connectionstyle=f"arc3,rad={rad}"))
        ax.text((x1 + x2) / 2, (y1 + y2) / 2 + (0.45 if y2 > y1 else -0.55), t, fontsize=7, ha="center", color=RED)
    k = list(pos)
    e(k[0], k[1], "a: study, P=0.8, R=−1"); e(k[0], k[2], "a: rest, P=0.2, R=0"); e(k[1], k[3], "P=0.7, R=+10"); e(k[2], k[3], "P=0.1, R=+10")
    ax.text(5, 4.5, "MDP = (S, A, P, R, γ)", ha="center", fontsize=10, weight="bold"); save(fig, "mdp")


def markov_chain():
    fig, ax = canvas(5.2, 2.2, (0, 10), (0, 3.6))
    for x, t in ((2, "Sunny"), (8, "Rainy")):
        ax.add_patch(Circle((x, 1.8), 0.9, fc="#DEEBF7", ec=BLUE, lw=1.4)); ax.text(x, 1.8, t, ha="center", va="center", fontsize=9)
    ax.annotate("", xy=(7.1, 2.1), xytext=(2.9, 2.1), arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.3")); ax.text(5, 3.0, "0.2", ha="center")
    ax.annotate("", xy=(2.9, 1.5), xytext=(7.1, 1.5), arrowprops=dict(arrowstyle="-|>", connectionstyle="arc3,rad=-0.3")); ax.text(5, 0.5, "0.4", ha="center")
    ax.text(0.2, 3.1, "stay 0.8", fontsize=8); ax.text(8.6, 3.1, "stay 0.6", fontsize=8)
    save(fig, "markov_chain")


if __name__ == "__main__":
    for f in (knn, confusion, svm, kernel, softmargin, ova_ovo, imbalance, regression_error, bayes_reg,
              kmeans, elbow, dbscan, gmm, dendro, divisive, cluster_types, cluster_apps,
              ensemble, voting, stacking, boosting, gradient_boost, random_forest, bag_vs_boost, homo_hetero,
              rl_loop, learning_types, qlearning, mdp, markov_chain):
        f()
    print("diagrams:", len(os.listdir(OUT)))
