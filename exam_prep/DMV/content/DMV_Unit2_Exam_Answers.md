---
title: "Data Modeling and Visualization: Unit 2 Exam Answers"
subtitle: "Unit 2 (Q3/Q4): Data Visualization and Data Wrangling | Syllabus Unit IV"
---

# Unit Snapshot

| No. | Question | Max Marks | Years Asked | Importance |
|---|---|---|---|---|
| 2.1 | Force-directed techniques in graph layout (with MDS) | 9 | 2023, 2024, 2025 | ★★★ |
| 2.2 | Process / key steps of data wrangling | 9 | 2023, 2024, 2025 | ★★★ |
| 2.3 | Multidimensional scaling (MDS) and its role in visualizing high-dimensional data | 9 | 2025, 2026 | ★★ |
| 2.4 | Pulling under constraints model | 8 | 2024, 2026 | ★★ |
| 2.5 | Reshaping and pivoting | 8 | 2024, 2026 | ★★ |
| 2.6 | Functions available in matplotlib | 7 | 2023, 2026 | ★★ |
| 2.7 | Graph layout techniques (any two with examples) | 6 | 2023, 2026 | ★★ |
| 2.8 | Seaborn vs matplotlib (and pandas) | 6 | 2025, 2026 | ★★ |
| 2.9 | Bipartite graph and its applications | 6 | 2023 | ★ |
| 2.10 | Combining vs merging data sets; when to use each | 6 | 2025 | ★ |
| 2.11 | Differentiate force-directed techniques and MDS | 4 | 2023 | ★ |

**Must-do first (★★★):** 2.1 Force-directed techniques · 2.2 Data wrangling. *(FD + MDS together appear in all 4 papers, so also do 2.3 and 2.11 right after.)*

All answers are written for **(highest marks + 2)**. Source = `Textbooks/DMV Textbook.pdf` (scanned; PDF page numbers).

# Full Answers

## 2.1 Explain force-directed techniques in graph layout (and their relation to MDS)

**★★★ | Asked for max 9 marks → written for 11 | Asked in: 2023 (7), 2024 (9), 2025 (8) | Source: DMV Textbook.pdf, PDF p. 64-66 (4.4.1 Graph Layout Techniques; Force-directed Techniques and Multidimensional Scaling)**

Variants: "Explain in detail force-directed techniques in multidimensional Scaling" (2023) · "Explain the Force-directed Techniques and Multidimensional Scaling in detail" (2024) · "What are Force-directed Techniques in Graph Layout, and how do they help in visualizing complex data structures?" (2025).

**Definition:** **Force-directed techniques** are graph-layout algorithms that **simulate physical forces**: **nodes repel each other** like charged particles, and **edges act like springs** pulling connected nodes together. The algorithm moves nodes until the forces are in **equilibrium**, giving a layout with **few edge crossings and node overlaps**.

### 1. Basic idea (physical model)

- **Repulsive force** between **every pair** of nodes → nodes spread out, no overlap.
- **Attractive (spring) force** along **each edge** → connected nodes stay close.
- **Equilibrium** (minimum energy) → final positions; clusters of tightly linked nodes appear naturally.

### 2. Algorithm (steps)

![Force-directed layout algorithm](diagrams/u2_force_directed.png){width=3.6in}

1. Place all nodes at **random** positions.
2. For each pair of nodes, compute the **repulsive force**.
3. For each edge, compute the **attractive (spring) force**.
4. Add the forces and **move each node** in the direction of the net force; the step size is limited by a **temperature**.
5. **Cool down**: reduce the temperature so movements become smaller.
6. Repeat until forces are **balanced** or the maximum number of iterations is reached.

**Diagram explanation:** the loop (steps 2-5) runs many times; the diamond checks for **convergence**; the output is the **equilibrium layout**.

### 3. Formulas (Fruchterman-Reingold model)

- **Ideal edge length:** k = C · √(Area / n)
- **Attractive force:** f~a~(d) = d² / k
- **Repulsive force:** f~r~(d) = − k² / d

where **d** = distance between two nodes, **n** = number of nodes, **Area** = drawing area, **C** = constant. (Eades' spring model: spring force = c~1~ · log(d / c~2~), repulsion = c~3~ / d².)

### 4. Popular force-directed algorithms

- **Eades spring embedder** (1984): the first spring model.
- **Fruchterman-Reingold**: balances attraction between connected nodes and repulsion between all nodes (named in the textbook).
- **Kamada-Kawai**: treats graph-theoretic distances as ideal spring lengths and **minimises an energy (cost) function**; preserves overall topology.
- **Pulling under constraints** (see 2.4): FD + extra constraints.

### 5. How they help in visualizing complex data structures

- Reveal **clusters / communities** (e.g. friend groups in social networks).
- Show **central (hub) nodes** and bridges.
- Produce **symmetric, aesthetically pleasing** layouts automatically.
- Work for **any general graph** without needing a hierarchy.
- **Interactive**: the user can drag a node and the layout re-balances.

### 6. Relation to MDS

- Both place objects so that **layout distance reflects relationship**.
- **Kamada-Kawai** is effectively **MDS on graph distances**: it tries to make the drawn distance equal the **shortest-path distance**, which is exactly MDS's goal (see 2.3, 2.11).

### Advantages / Disadvantages

| Advantages | Disadvantages |
|---|---|
| Simple, intuitive (physics analogy) | Slow for large graphs: O(n²) repulsion per iteration |
| Good symmetry, shows clusters | Can get stuck in **local minima** |
| No prior structure needed | Result changes with random start |
| Easy to make interactive | "Hairball" for very dense graphs |

**Applications:** social-network analysis, biological (protein-interaction) networks, web-link graphs, knowledge graphs. Tools: **NetworkX** `spring_layout()`, **Gephi**, **D3.js** force layout, Cytoscape.

**Conclusion:** Force-directed techniques turn the **structure of a network into geometry**, using a simple attraction-repulsion model to reveal clusters and relationships.

> **Memory trick:** "**Nodes are magnets, edges are springs**" (**R**epel all, **A**ttract linked, **M**ove, **C**ool, **R**epeat: **"RAM-CR"**).

## 2.2 Explain the process / key steps of data wrangling

**★★★ | Asked for max 9 marks → written for 11 | Asked in: 2023 (4), 2024 (9), 2025 (5) | Source: DMV Textbook.pdf, PDF p. 59-60 (4.2 Data Wrangling)**

Variants: "Describe the key steps involved in the process of data wrangling" (2023, 2025) · "Explain the process of data wrangling in detail" (2024).

**Definition:** **Data wrangling** (also called **data munging** or **data preprocessing**) is the process of **cleaning, transforming and preparing raw data** into a format suitable for analysis. Raw data is usually messy, unstructured, with **errors, missing values and inconsistencies**.

![Data wrangling process](diagrams/u2_wrangling.png){width=6.2in}

### Steps of data wrangling

1. **Data collection (gathering)**: get raw data from **databases, files, APIs, web scraping**.
2. **Data cleaning**: identify and correct **errors**, handle **missing data** (drop / fill with mean, median, mode), **standardise formats** (dates, units, case), **remove duplicates**.
3. **Data transformation**: convert data into the required format: **reshaping** (pivot/melt), **aggregating**, creating new variables, encoding categories.
4. **Data integration**: **combine data from different sources** into one unified dataset (merge/join, concatenate).
5. **Data reduction**: reduce size while keeping essential information: **filtering, sampling, summarising**, dropping irrelevant columns.
6. **Data enrichment**: add **external data** or extra information to improve quality (e.g. add city population to sales data).
7. **Handling outliers**: detect (box plot, z-score, IQR) and treat outliers that may skew results.
8. **Data formatting**: correct **data types** (numeric, categorical, datetime).
9. **Handling imbalanced data**: fix class imbalance (oversampling e.g. **SMOTE**, undersampling).
10. **Feature engineering**: create new features (e.g. `age` from `date_of_birth`, `month` from timestamp).
11. **Validation & documentation**: check ranges, uniqueness, consistency; record every step for **reproducibility**.

**Diagram explanation:** the top row makes the data **correct and unified**; the bottom row makes it **compact, rich and model-ready**; the final box is the **analysis-ready dataset**.

### Example (pandas)

```python
df = pd.read_csv("sales.csv")                      # collect
df = df.drop_duplicates()                           # clean
df["city"] = df["city"].str.title().fillna("Unknown")
df["date"] = pd.to_datetime(df["date"])             # format
df = df.merge(cities, on="city", how="left")        # integrate / enrich
monthly = df.groupby(df["date"].dt.month)["amount"].sum()   # transform / reduce
```

### Tools

**Python**: pandas, NumPy · **R**: dplyr, tidyr · **GUI**: OpenRefine, Trifacta, Excel Power Query.

### Importance

- **Garbage in, garbage out**: models and charts are only as good as the data.
- Analysts typically spend **60-80% of their time** on wrangling.
- Ensures **accurate, consistent and reliable** analysis and better decisions.

**Conclusion:** Data wrangling converts **messy raw data into clean, structured, analysis-ready data**; it is the most time-consuming but most important step of the data pipeline.

> **Memory trick: "Can Clever Teams Integrate, Reduce, Enrich Our Final Insights Fast?"**: **C**ollect, **C**lean, **T**ransform, **I**ntegrate, **R**educe, **E**nrich, **O**utliers, **F**ormat, **I**mbalance, **F**eature engineering.

## 2.3 What is multidimensional scaling (MDS)? Explain its role in visualizing high-dimensional data

**★★ | Asked for max 9 marks → written for 11 | Asked in: 2025 (9), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 65-66 (Multidimensional Scaling); p. 51 (Higher-Dimensional Displays)**

Variants: "Describe the concept of Multidimensional Scaling and its role in Data Visualization" (2025) · "What is multidimensional scaling (MDS) and how MDS helps in visualizing high dimensional data" (2026).

**Definition:** **Multidimensional Scaling (MDS)** is a **dimensionality-reduction** technique that represents objects as points in a **low-dimensional space (2-D or 3-D)** such that the **distances between points match the original (high-dimensional) distances or dissimilarities** as closely as possible.

![MDS process](diagrams/u2_mds.png){width=6.2in}

**Diagram explanation:**

- **High-dimensional data**: n objects each with p features (p can be 50, 100, ...), impossible to plot directly.
- **Distance matrix D**: pairwise dissimilarities δ~ij~ using **Euclidean** or **correlation** distance (MDS can also start directly from a given dissimilarity matrix, e.g. survey ratings).
- **MDS**: searches for 2-D coordinates whose distances d~ij~ ≈ δ~ij~ by **minimising stress**.
- **Output map**: similar objects appear **close together**, dissimilar ones **far apart**.

### Steps (classical / metric MDS)

1. Compute the n × n **distance matrix** D = [δ~ij~].
2. Square the distances and apply **double centering**: B = −½ · J · D^(2)^ · J, where J = I − (1/n)·11ᵀ.
3. Find the **eigenvalues and eigenvectors** of B.
4. Take the top m (= 2) eigenvalues Λ~m~ and eigenvectors E~m~; coordinates **X = E~m~ · Λ~m~^½^**.
5. Plot X as a scatter plot.

### Stress (goodness of fit)

**Stress** = √[ Σ (d~ij~ − δ~ij~)² / Σ d~ij~² ]

where **δ~ij~** = original dissimilarity, **d~ij~** = distance in the low-dimensional map. **Lower stress = better fit** (Kruskal's guide: < 0.05 excellent, < 0.1 good, > 0.2 poor).

### Types of MDS

- **Classical (Torgerson) MDS**: Euclidean distances, eigen-decomposition (same result as PCA on Euclidean data).
- **Metric MDS**: preserves actual distance values (iterative stress minimisation).
- **Non-metric MDS**: preserves only the **rank order** of dissimilarities (good for ratings / ordinal data).

### Role in visualizing high-dimensional data

- **Reduces p dimensions to 2-D/3-D** so data can be shown as a scatter plot.
- Reveals **clusters, groups and outliers**.
- Shows **similarity structure**: which products, customers or genes are alike.
- Works with **any distance measure**, even when only similarities (not features) are available.
- In **graph visualization**, MDS on shortest-path distances gives a node layout (link to force-directed methods).

### Example

Distances between 10 Indian cities (road km) → MDS → a 2-D map that looks almost like the real map of India. Similarly, customer-preference data → MDS → brands that customers see as similar appear close together (**market positioning map**).

```python
from sklearn.manifold import MDS
X2 = MDS(n_components=2, dissimilarity="euclidean").fit_transform(X)
plt.scatter(X2[:,0], X2[:,1])
```

### Advantages / Limitations

- **+** Simple, intuitive output; works with any dissimilarity; non-metric version handles ordinal data.
- **−** Slow for large n (n × n matrix); axes have **no direct meaning**; result can be rotated/flipped; may lose information if stress is high.

**Applications:** marketing (perceptual maps), psychology, bioinformatics (gene expression), document similarity, graph layout.

**Conclusion:** MDS turns a **table of distances into a picture**, preserving similarity so that hidden **patterns in high-dimensional data** become visible in 2-D.

> **Memory trick:** "**MDS = Map from Distance Sheet**" (like drawing a map of cities from a road-distance table).

## 2.4 Write a short note on the pulling under constraints model

**★★ | Asked for max 8 marks → written for 10 | Asked in: 2024 (8), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 66 (The Pulling under Constraints Model)**

**Definition:** The **Pulling Under Constraints (PUC) model** is an approach used in **force-directed graph layout** that adds **constraints on node and edge positions** (based on graph properties or **user-defined rules**) to the usual attraction-repulsion forces. Nodes are **pulled** towards positions that satisfy the constraints, giving a **more controlled, structured layout**.

### 1. Why it is needed

- Plain force-directed layouts of **complex graphs** can become **chaotic**: tangled "hairballs", oscillating nodes, no meaningful order.
- PUC imposes **structure and control**, giving more **informative and organised** visualizations.

![Pulling under constraints model](diagrams/u2_puc.png){width=6.2in}

**Diagram explanation:** the normal **force model** and a set of **constraints** both act on each node; the node is **pulled** to a position that balances the forces while **respecting the constraints**; the result is a **stable, readable layout**.

### 2. Key features / constraints

1. **Fixed positions**: some nodes are **anchored** at predefined positions and not moved by forces (e.g. root of a hierarchy, known geographic locations).
2. **Inertial constraints**: **inertia** is added to node motion so nodes move **smoothly**, resisting sudden jumps; this **stabilises** the layout and reduces **oscillations**.
3. **Edge bundling**: many edges between the same groups are **bundled into one curved path**, reducing **visual clutter** in dense graphs.
4. **Alignment / separation constraints**: nodes can be forced to lie on the same horizontal/vertical line or keep a minimum gap (e.g. parent above child).
5. **Region / boundary constraints**: groups of nodes kept inside a given area (cluster boxes).

### 3. Working (steps)

1. Start with a force-directed layout (repulsion + springs).
2. Compute forces and **tentative new positions**.
3. **Project / pull** each node back to the nearest position that satisfies all constraints.
4. Apply **inertia** (damping) to smooth movement.
5. Repeat until stable.

### 4. Example

A company org-chart network: the **CEO node is fixed at the top**, each department is **constrained to its own region**, levels are **aligned horizontally**, and the many email links between two departments are **bundled**. The result is readable, unlike a plain spring layout.

### 5. Applications

**Social networks**, **biological networks**, **large-scale datasets**, hierarchical/organisational graphs, metro/transport maps, software dependency graphs.

**Advantages:** structured and predictable layouts, user control, stable (less jitter), less clutter. **Limitation:** extra computation; too many constraints can conflict.

**Conclusion:** PUC = **force-directed layout + rules**. The forces give a natural layout; the constraints make it **meaningful and stable**.

> **Memory trick: "FIBAR"**: **F**ixed positions, **I**nertia, **B**undling of edges, **A**lignment, **R**egion constraints.

## 2.5 Explain reshaping and pivoting and their importance in data visualization

**★★ | Asked for max 8 marks → written for 10 | Asked in: 2024 (8), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 60 (4.2.1 Hierarchical Indexing; 4.2.2 Combining and Merging Data Sets, Reshaping and Pivoting)**

Variants: "Explain importance of reshaping and pivoting in data visualization" (2024) · "Write short notes on Reshaping and pivoting" (2026).

**Definition:** **Reshaping** means **changing the layout (structure) of a dataset** (rows ↔ columns) without changing its values. **Pivoting** is a type of reshaping that turns **unique values of a column into new columns** (long → wide), optionally aggregating values.

![Wide vs long format](diagrams/u2_reshape.png){width=5.2in}

**Diagram explanation:** **Wide format** has one row per entity and one column per year; **long (tidy) format** has one row per observation (city, year, sales). **melt()/stack()** convert wide → long; **pivot()/unstack()** convert long → wide.

### 1. Reshaping operations (pandas)

| Operation | Direction | pandas function | Example |
|---|---|---|---|
| **Pivot** | Long → wide | `df.pivot(index, columns, values)` | rows = city, columns = year |
| **Pivot table** | Long → wide **with aggregation** | `pd.pivot_table(df, index, columns, values, aggfunc="sum")` | total sales per city per year |
| **Melt** | Wide → long | `pd.melt(df, id_vars, value_vars)` | year columns → one "year" column |
| **Stack** | Columns → inner row index | `df.stack()` | makes a MultiIndex Series |
| **Unstack** | Inner row index → columns | `s.unstack()` | reverse of stack |

**Hierarchical indexing (MultiIndex):** multiple index levels (e.g. Region → Year) let 2-D tables hold higher-dimensional data; `stack`/`unstack` move levels between rows and columns.

### 2. Example

```python
long = pd.melt(wide, id_vars="city", var_name="year", value_name="sales")
wide2 = long.pivot(index="city", columns="year", values="sales")
```

### 3. Importance in data visualization

1. **Libraries expect a certain shape**: Seaborn/Plotly prefer **long (tidy)** data (`hue="year"`), while heat maps and pandas `.plot()` need **wide** data.
2. **Comparison across categories**: pivoted tables put categories side by side for **grouped bar charts**.
3. **Heat maps** need a **matrix** (rows × columns) → created by pivoting.
4. **Summarisation**: `pivot_table` aggregates (sum, mean) before plotting, reducing data size.
5. **Time-series plots**: pivot dates to rows and series to columns → multi-line chart.
6. **Cleaner, tidier data**: one variable per column, one observation per row → fewer errors.
7. **Multi-dimensional analysis** using hierarchical indexes.

**Conclusion:** Reshaping and pivoting put data in the **right shape for the chart**, making visualization **easy, correct and efficient**.

> **Memory trick:** "**Melt makes it Long; Pivot makes it wide (P for Panorama)**." Stack ↓ (columns go down into rows), Unstack ↑.

## 2.6 Discuss various functions available in matplotlib

**★★ | Asked for max 7 marks → written for 9 | Asked in: 2023 (7), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 61-62 (Data Visualization Matplotlib; Colors, Markers and Line Styles; matplotlib configuration)**

**Introduction:** **Matplotlib** is the most popular **Python library for 2-D plotting**, created by **John D. Hunter**. It produces **static, interactive and publication-quality** plots, and is used through the `matplotlib.pyplot` module (`import matplotlib.pyplot as plt`).

![Matplotlib structure and functions](diagrams/u2_mpl_anatomy.png){width=5.6in}

**Diagram explanation:** a **Figure** is the whole canvas; it holds one or more **Axes** (plots); each Axes contains **plot elements**, **decorations** and **scales**; finally the figure is **shown or saved**.

### Functions (grouped)

| Group | Function | Purpose |
|---|---|---|
| **Figure & layout** | `plt.figure(figsize=(w,h))` | Create a new figure |
| | `plt.subplot(r,c,i)`, `plt.subplots(r,c)` | Multiple plots in a grid |
| **Plot types** | `plt.plot(x, y, 'g--o')` | Line plot (colour, line style, marker string) |
| | `plt.scatter(x, y)` | Scatter plot |
| | `plt.bar()` / `plt.barh()` | Vertical / horizontal bar chart |
| | `plt.hist(data, bins=10)` | Histogram |
| | `plt.pie(sizes, labels=...)` | Pie chart |
| | `plt.boxplot(data)` | Box-and-whisker plot |
| | `plt.imshow()`, `plt.contour()` | Image / heat map, contour plot |
| **Labels & decoration** | `plt.title()`, `plt.xlabel()`, `plt.ylabel()` | Title and axis labels |
| | `plt.legend()` | Legend |
| | `plt.grid(True)` | Grid lines |
| | `plt.text()`, `plt.annotate()` | Text / arrow annotations |
| **Axes & ticks** | `plt.xlim()`, `plt.ylim()` | Axis range |
| | `plt.xticks()`, `plt.yticks()` | Tick positions and labels |
| **Styling / config** | `color=`, `linestyle='dashed'`, `marker='o'` | Colours, line styles, markers |
| | `plt.rc('figure', figsize=(10,10))` | Global settings (rc params), also `matplotlibrc` file |
| | `plt.style.use('ggplot')` | Ready-made styles |
| **Output** | `plt.show()` | Display the plot |
| | `plt.savefig('fig.png', dpi=300)` | Save as PNG, PDF, SVG |

### Example

```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]; y = [10, 20, 15, 25]
plt.plot(x, y, 'g--o', label="Sales")   # green dashed line, circle markers
plt.title("Quarterly Sales"); plt.xlabel("Quarter"); plt.ylabel("₹ lakh")
plt.legend(); plt.grid(True); plt.savefig("sales.png"); plt.show()
```

**Features:** works with NumPy/pandas, integrates with **IPython/Jupyter** (zoom and pan toolbar), highly **customisable**, many output formats; **Seaborn and pandas plotting are built on it**.

**Conclusion:** Matplotlib offers **low-level, complete control** over every plot element through simple pyplot functions, which makes it the foundation of Python visualization.

> **Memory trick: "F-P-L-A-S-O"**: **F**igure, **P**lot types, **L**abels, **A**xes/ticks, **S**tyle, **O**utput.

## 2.7 Explain graph layout techniques in data visualization (any two with examples)

**★★ | Asked for max 6 marks → written for 8 | Asked in: 2023 (6), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 64-65 (4.4.1 Data and Graphs, Graph Layout Techniques)**

Variants: "Explain effective graph layout techniques in data visualization" (2023) · "Describe any two layout techniques used in graph visualization with examples" (2026).

**Definition:** **Graph layout techniques** are methods to decide the **positions of nodes (vertices) and edges** of a graph on a 2-D or 3-D plane, so that the graph is **clear**, has **minimum overlaps and edge crossings**, and shows meaningful **patterns or structures**.

![Common graph layouts](diagrams/u2_layouts.png){width=6.2in}

### Layout techniques

1. **Force-directed layout**: nodes repel, edges act as springs; finds **equilibrium** (see 2.1). *Example:* social-network friend clusters.
2. **Circular layout**: nodes placed on a **circle** (ordered by attribute). *Example:* cyclic processes, ring networks, showing connections between departments.
3. **Hierarchical (tree) layout**: nodes in **levels**, parent above child. *Example:* organisation chart, **decision tree**, file system.
4. **Layered (Sugiyama) layout**: nodes in horizontal/vertical **layers**, edges mostly point one way. *Example:* **DAGs**, flowcharts, workflow pipelines.
5. **Kamada-Kawai layout**: minimises an **energy/cost** based on graph distances; preserves topology and reduces crossings.
6. **Fruchterman-Reingold layout**: a force-directed algorithm balancing attraction (connected nodes) and repulsion (all nodes).
7. **Spectral layout**: uses **eigenvectors of the adjacency / Laplacian matrix**; good for **clustering and community detection**.
8. **Grid layout**: nodes on a **regular grid**; simple, consistent for small graphs. *Example:* sensor networks, pixel/mesh graphs.

**Diagram explanation:** the same idea (nodes + edges) looks very different under each layout: the **spring** layout reveals branches, the **circular** layout shows the cycle, the **tree** layout shows levels, and the **grid** layout shows regular structure.

### Example (NetworkX)

```python
pos = nx.spring_layout(G)   # or nx.circular_layout(G), nx.kamada_kawai_layout(G)
nx.draw(G, pos, with_labels=True)
```

### Choosing a layout

Depends on **graph type** (tree, DAG, cyclic, general), **size**, and **insight needed** (clusters → force-directed; hierarchy → tree; cycles → circular). Tools: **NetworkX** (Python), **Cytoscape**, Gephi, Graphviz.

**Conclusion:** The right layout makes a network **readable**; force-directed and hierarchical layouts are the most commonly used.

> **Memory trick: "FC-HL-KF-SG"** → "**F**ancy **C**ats **H**ate **L**oud **K**ids, **F**riendly **S**ilent **G**uests" (Force, Circular, Hierarchical, Layered, Kamada-Kawai, Fruchterman-Reingold, Spectral, Grid).

## 2.8 Compare matplotlib, pandas and seaborn for data visualization. What is seaborn and its advantages over matplotlib?

**★★ | Asked for max 6 marks → written for 8 | Asked in: 2025 (6), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 61-63 (Plotting with Pandas and Seaborn; Python Visualization Tool Ecosystem)**

Variants: "How does matplotlib compare to pandas and seaborn in terms of Data Visualization capabilities?" (2025) · "What is seaborn? Discuss the advantages over matplotlib." (2026).

**Definition:** **Seaborn** is a **high-level statistical visualization library** built **on top of Matplotlib**. It works directly with **pandas DataFrames** and creates attractive, informative statistical plots with **less code**.

![Relationship of the three libraries](diagrams/u2_libs.png){width=4.6in}

**Diagram explanation:** **Matplotlib** is the base layer; **pandas `.plot()`** and **Seaborn** are higher-level layers that call Matplotlib internally, so Matplotlib functions can still be used to fine-tune their plots.

### Comparison

| Point | Matplotlib | pandas plotting | Seaborn |
|---|---|---|---|
| **Level** | **Low-level**, full control | High-level wrapper | **High-level**, statistical |
| **Input** | Lists / NumPy arrays | DataFrame / Series | DataFrame (column names) |
| **Code needed** | Most code | One line: `df.plot()` | Short: `sns.boxplot(x=, y=, data=)` |
| **Default look** | Plain | Plain (Matplotlib defaults) | **Attractive themes & palettes** |
| **Statistical plots** | Manual | Basic (hist, box, kde) | **Built-in**: regression, violin, pair, heat map, distribution |
| **Grouping by category** | Manual loops | Limited | Automatic via `hue`, `col`, `row` |
| **Customisation** | **Unlimited** | Moderate | Good + Matplotlib for details |
| **Best for** | Publication-quality custom figures | Quick EDA of a DataFrame | Statistical EDA, multi-variable comparison |

### Advantages of Seaborn over Matplotlib

1. **Less code** for complex plots (one line for a grouped box plot).
2. **Beautiful default themes** and colour palettes (`sns.set_theme()`).
3. **Direct DataFrame support**: use column names; automatic axis labels.
4. **Built-in statistical functions**: regression lines with confidence intervals (`regplot`), kernel density (`kdeplot`), aggregation with error bars (`barplot`).
5. **Special plots**: `pairplot`, `heatmap`, `violinplot`, `jointplot`, `FacetGrid`.
6. **Automatic grouping** with `hue`, `col`, `row` for multi-variable comparison.

**Limitations of Seaborn:** fewer plot types for non-statistical graphics, less fine control, slower for very large data; you still need Matplotlib for detailed customisation.

### Example

```python
import seaborn as sns
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="sex", data=tips)   # one line
```

The same plot in pure Matplotlib needs manual grouping, positioning and a legend (10+ lines).

**Conclusion:** Use **Matplotlib** for full control, **pandas** for quick plots of DataFrames, and **Seaborn** for fast, beautiful **statistical** plots; they work best **together**.

> **Memory trick:** "**Matplotlib = Manual, Pandas = Pronto (quick), Seaborn = Statistical & Stylish.**"

## 2.9 Explain bipartite graph and its applications

**★ | Asked for max 6 marks → written for 8 | Asked in: 2023 (6) | Source: DMV Textbook.pdf, PDF p. 66 (Bipartite Graphs)**

**Definition:** A **bipartite graph (bigraph)** is a graph whose vertex set V can be **divided into two disjoint sets U and V** such that **every edge connects a vertex in U to a vertex in V**; there are **no edges within the same set**.

Formally: G = (U ∪ V, E), U ∩ V = ∅, and every edge (u, v) ∈ E has u ∈ U, v ∈ V.

![Bipartite graph: students and courses](diagrams/u2_bipartite.png){width=3.4in}

**Diagram explanation:** left set **U = students**, right set **V = courses**; each edge means "student enrolled in course". No student-student or course-course edges exist.

### Properties

1. A graph is bipartite **if and only if it has no odd-length cycle** (no triangles).
2. It is **2-colourable**: colour U one colour and V another; no edge joins the same colour.
3. **Complete bipartite graph K~m,n~**: every vertex of U is joined to every vertex of V; it has m × n edges.
4. Sum of degrees in U = sum of degrees in V = |E|.
5. Can be checked using **BFS/DFS 2-colouring** in O(V + E).

### Applications

1. **Matching problems**: students ↔ courses, employees ↔ tasks, advertisers ↔ target customers (maximum matching).
2. **Recommendation systems**: users ↔ items (edge = purchase / rating); used in collaborative filtering.
3. **Social-network analysis**: people ↔ groups/communities (memberships, affiliations).
4. **Transportation networks**: suppliers ↔ consumers, flow of goods.
5. **Resource allocation**: tasks ↔ workers, funds ↔ projects.
6. **Information retrieval**: documents ↔ terms.

### Visualization

Place one set on the **left** and the other on the **right** (two-column layout) with edges crossing between them; heavy edges can be **bundled** or shown as a **matrix (heat map)**.

**Conclusion:** Bipartite graphs model **relationships between two different types of entities**, which is why they are central to matching and recommendation problems.

> **Exam tip:** Your textbook (PDF p. 66) states that bipartite graphs are always "planar". This is **not true in general**: **K~3,3~** is bipartite but **not planar**. Write "**no odd cycles**" as the key property and avoid writing "always planar".

## 2.10 Explain the differences between combining and merging data sets. When should each be used?

**★ | Asked for max 6 marks → written for 8 | Asked in: 2025 (6) | Source: DMV Textbook.pdf, PDF p. 60 (4.2.2 Combining and Merging Data Sets)**

**Introduction:** **Combining (concatenation)** **stacks** data frames together **along an axis** (rows or columns). **Merging (joining)** combines data frames **based on common key column(s)**, like a **SQL join**.

| No. | Point | Combining (Concatenation) | Merging (Join) |
|---|---|---|---|
| 1 | **Meaning** | Stack data frames one **below** or **beside** another | Match rows using **common key** values |
| 2 | **pandas function** | `pd.concat([df1, df2], axis=0/1)` (also `combine_first`) | `pd.merge(df1, df2, on="key", how=...)`, `df.join()` |
| 3 | **Basis** | **Position / index** alignment | **Key column(s)** values |
| 4 | **Structure needed** | Same columns (axis=0) or same index (axis=1) | At least one **common key** column |
| 5 | **Types** | Vertical (rows), horizontal (columns) | **inner, outer, left, right** joins |
| 6 | **Result size** | rows = sum of rows (axis=0) | Depends on matches; can grow (one-to-many) |
| 7 | **Missing matches** | Fills NaN for non-shared columns | Depends on join type (inner drops, outer keeps with NaN) |
| 8 | **SQL analogy** | `UNION ALL` | `JOIN` |
| 9 | **Example** | Jan sales + Feb sales → one table | Orders + customer details on `customer_id` |

### When to use which

- **Use combining** when datasets have the **same structure** and you are **adding more records** (monthly files, data from several branches) or adding columns with the **same index**.
- **Use merging** when datasets hold **different information about the same entities** and must be **linked by a key** (orders ↔ customers, students ↔ marks).

### Example

```python
all_sales = pd.concat([jan, feb], axis=0)                       # combine
full = pd.merge(orders, customers, on="customer_id", how="left")  # merge
```

**Conclusion:** **Concat = stack by position; Merge = link by key.** Choose concat to **append**, merge to **enrich**.

> **Memory trick:** "**Concat stacks, Merge matches.**"

## 2.11 Differentiate force-directed techniques and multidimensional scaling

**★ | Asked for max 4 marks → written for 6 | Asked in: 2023 (4) | Source: DMV Textbook.pdf, PDF p. 65-66 (Difference between Force-directed Techniques and MDS)**

**Introduction:** Both techniques place objects in 2-D so that **distance shows relationship**, but **force-directed** methods lay out **graphs**, while **MDS** reduces the **dimensions of general data**.

| No. | Point | Force-directed techniques | Multidimensional scaling (MDS) |
|---|---|---|---|
| 1 | **Purpose** | **Graph layout** (draw networks nicely) | **Dimensionality reduction** and similarity visualization |
| 2 | **Input** | Graph: nodes + edges | **Distance / dissimilarity matrix** (or high-dimensional data) |
| 3 | **Principle** | Physics: **repulsion** between nodes, **springs** on edges | Preserve **pairwise distances** in low dimension |
| 4 | **Objective** | Reach **force equilibrium** (min energy), few crossings | Minimise **stress** (distance mismatch) |
| 5 | **Method** | Iterative simulation | Eigen-decomposition (classical) or iterative optimisation |
| 6 | **Output** | Node positions for drawing a network | 2-D/3-D coordinates (scatter plot) |
| 7 | **Scope** | Specific to **graphs** | General: any objects with distances |
| 8 | **Examples** | Fruchterman-Reingold, Eades, Kamada-Kawai | Classical, metric, non-metric MDS |
| 9 | **Application** | Social networks, protein networks | Market perception maps, gene data, city maps |

**Conclusion:** Force-directed = **draw a network**; MDS = **map high-dimensional similarity**. (Kamada-Kawai links the two: it is MDS applied to graph distances.)

> **Memory trick:** "**Force → Friends network; MDS → Map of Distances.**"

# Last-Minute Revision Sheet: Unit 2

| Topic | Key points to write |
|---|---|
| **Force-directed** | Nodes repel, edges = springs, iterate to equilibrium. FR: f~a~ = d²/k, f~r~ = −k²/d, k = C√(A/n). Algorithms: Eades, Fruchterman-Reingold, Kamada-Kawai. Pros: clusters, symmetry. Cons: O(n²), local minima. **"RAM-CR"** |
| **Data wrangling** | Collect, Clean, Transform, Integrate, Reduce, Enrich, Outliers, Format, Imbalance, Feature engineering, Validate. "Garbage in, garbage out". |
| **MDS** | Distances → low-dim map. Classical: B = −½ J D² J, eigenvectors, X = E Λ^½^. Stress = √[Σ(d−δ)²/Σd²], < 0.1 good. Types: classical, metric, non-metric. |
| **PUC model** | FD + constraints: **F**ixed nodes, **I**nertia, edge **B**undling, **A**lignment, **R**egion → "FIBAR". Stable, structured layout. |
| **Reshaping & pivoting** | Wide ↔ long. melt/stack (→ long), pivot/unstack (→ wide), pivot_table (aggregate). MultiIndex. Needed for heat maps, grouped bars, seaborn hue. |
| **Matplotlib functions** | figure, subplot(s), plot, scatter, bar, hist, pie, boxplot, imshow, title, xlabel, ylabel, legend, grid, annotate, xlim, xticks, rc, style.use, show, savefig. **"F-P-L-A-S-O"** |
| **Graph layouts** | Force-directed, circular, hierarchical, layered (DAG), Kamada-Kawai, Fruchterman-Reingold, spectral (eigenvectors), grid. NetworkX, Cytoscape. |
| **Seaborn vs Matplotlib** | Seaborn = high-level, statistical, built on Matplotlib, DataFrame input, nice themes, hue/col, pairplot/heatmap/violin. Matplotlib = low-level, full control. pandas = quick `.plot()`. |
| **Bipartite graph** | Two disjoint sets, edges only across. No odd cycles, 2-colourable, K~m,n~ has mn edges. Uses: matching, recommendation, social groups, transport, resource allocation. |
| **Concat vs merge** | Concat stacks by position (`pd.concat`, axis 0/1); merge matches by key (`pd.merge`, inner/outer/left/right). |
| **FD vs MDS** | FD: graph layout, physics, equilibrium. MDS: dimensionality reduction, distance matrix, stress. |

# Assumptions & Gaps

- Exam Unit 2 = question pair Q3/Q4 = syllabus Unit IV "Data Visualization and Data Wrangling" (textbook Chapter 4, PDF p. 59-66).
- All citations are to `Textbooks/DMV Textbook.pdf` (scanned, OCR'd; **PDF page numbers**). There are no separate lecture notes in the repo.
- **Added from standard subject knowledge (not in the textbook):** Fruchterman-Reingold / Eades force formulas (2.1); classical-MDS eigen-decomposition steps, stress formula and Kruskal thresholds, MDS types (2.3); the alignment/separation and region constraints and the step-wise working of PUC (2.4; the textbook lists fixed positions, inertial constraints and edge bundling); bipartite properties 2-5 (2.9); most Matplotlib function names beyond `plot`, colours/markers/line styles and `rc` configuration (2.6; the textbook covers only these and the pandas `.plot()` methods); the comparison tables in 2.8 and 2.10 beyond what the textbook states.
- **Textbook error flagged:** PDF p. 66 says bipartite graphs "are planar". This is false in general (K~3,3~ is bipartite and non-planar); the answer gives the correct statement.
- 2024 Q3a ("Force-directed Techniques and MDS in detail") is mapped to 2.1; for the MDS half, also write the key points of 2.3.
- No question in this unit was missing from the materials; no "⚠ Not found" flags were needed.
