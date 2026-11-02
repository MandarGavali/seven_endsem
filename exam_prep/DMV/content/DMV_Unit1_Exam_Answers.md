---
title: "Data Modeling and Visualization: Unit 1 Exam Answers"
subtitle: "Unit 1 (Q1/Q2): Basics of Data Visualization | Syllabus Unit III"
---

# Unit Snapshot

| No. | Question | Max Marks | Years Asked | Importance |
|---|---|---|---|---|
| 1.1 | Data handling for data visualization (effect on accuracy & performance) | 10 | 2023, 2024, 2026 | ★★★ |
| 1.2 | Types of data visualization with examples / applications | 9 | 2023, 2024, 2025 | ★★★ |
| 1.3 | (Scientific) design choices in data visualization | 8 | 2024, 2025, 2026 | ★★★ |
| 1.4 | Need / role of graphics and computing in data visualization | 10 | 2023, 2025 | ★★ |
| 1.5 | Statistical historiography | 8 | 2023, 2025 | ★★ |
| 1.6 | Computational statistics and its role in data visualization | 8 | 2024, 2025 | ★★ |
| 1.7 | Presentation graphics vs exploratory graphics | 6 | 2025, 2026 | ★★ |
| 1.8 | Static graphics; features of a complete plot | 6 | 2026 | ★ |
| 1.9 | Output formats and speed issues | 6 | 2026 | ★ |
| 1.10 | 3-D plots in data modeling and visualization | 5 | 2026 | ★ |

**Must-do first (★★★):** 1.1 Data handling · 1.2 Types of data visualization · 1.3 Design choices.

All answers are written for **(highest marks + 2)**. Source = `Textbooks/DMV Textbook.pdf` (scanned; PDF page numbers).

# Full Answers

## 1.1 Explain data handling for data visualization. How does it affect accuracy and performance?

**★★★ | Asked for max 10 marks → written for 12 | Asked in: 2023 (10), 2024 (9), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 57-58 (Data Handling); p. 46-47 (speed strategies)**

Variants: "Explain data handling in data modeling and visualization" (2023) · "Explain data handling for data visualization" (2024) · "Discuss how data handling techniques affect visualization accuracy and performance" (2026).

**Definition:** **Data handling** is the process of **acquiring, cleaning, transforming, integrating and preparing data** before it is visualized. It decides the **quality, accuracy and structure** of the data, so that the final chart is **truthful** and **fast to render**.

### 1. Steps in data handling

![Data handling pipeline](diagrams/u1_data_handling.png){width=6.2in}

1. **Data acquisition**: collect data from **databases, files (CSV/Excel), APIs, web scraping**. Check its format and structure.
2. **Data cleaning**: handle **missing values** (impute/remove), **duplicates**, **outliers** and inconsistent entries (e.g. "Pune" vs "pune").
3. **Data transformation**: **reshape** data to suit the chart, **convert data types**, **normalise/scale** values, **aggregate** (e.g. daily → monthly).
4. **Data integration**: combine several sources by **merging, joining or appending** on a common key.
5. **Handling categorical data**: convert categories to numbers using **one-hot encoding** or **label encoding**.
6. **Handling time-series data**: **parse timestamps**, fill missing time points, align data for time comparisons.
7. **Data reduction**: **sampling or summarisation** for very large datasets.
8. **Data filtering**: keep only the subset relevant to the question (time period, region, criteria).
9. **Data exploration**: quick plots to spot issues; go back and re-clean if needed (**iterative**).

**Diagram explanation:** Steps 1 → 4 make the data **correct and complete**; steps 5 → 6 make it **small and focused**; the dashed "iterate" arrow shows that exploration often sends us back to cleaning.

### 2. Effect on accuracy

- **Missing values / outliers** not handled → bars and averages are **biased**, trends look false.
- **Duplicates** → counts are **inflated**.
- **Wrong data type** (date stored as text) → points plotted in **wrong order**.
- **Unscaled variables** → one variable dominates a multi-variable chart.
- **Correct joins** in integration → no records lost or double-counted.

### 3. Effect on performance (speed)

- **Aggregation / binning** reduces the number of points to draw (1 million rows → 365 daily totals).
- **Sampling** and **filtering** cut memory use and rendering time.
- **Correct, compact data types** (category, int32) speed up computation.
- Clean, pre-processed data allows **interactive** zoom/filter without lag.

### Example

A sales dataset of 10 lakh transactions: remove duplicate bills → fill missing city with "Unknown" → convert `date` text to datetime → **group by month** → plot a 12-point line chart. The chart is **accurate** (no double counts) and **fast** (12 points instead of 10 lakh).

**Conclusion:** Data handling is the **foundation** of visualization. Good handling gives **accurate** charts and **fast, responsive** visuals; poor handling gives misleading charts.

> **Memory trick: "A-C-T-I-R-F-E"** → **A**cquire, **C**lean, **T**ransform, **I**ntegrate, **R**educe, **F**ilter, **E**xplore. ("**ACT I R**eally **F**ind **E**rrors")

## 1.2 Explain the different types of data visualization with suitable examples / applications

**★★★ | Asked for max 9 marks → written for 11 | Asked in: 2023 (8), 2024 (9), 2025 (6) | Source: DMV Textbook.pdf, PDF p. 43 (3.1.1 Types of Data Visualization)**

Variants: "Explain the types of Data Visualization with suitable example" (2023) · "Explain the different types of Data visualization" (2024) · "...and their applications" (2025).

**Introduction:** **Data visualization** is the graphical representation of data. Different **types** suit different **data** and different **insights** (comparison, trend, proportion, relationship, distribution, location, network).

![Types of data visualization by purpose](diagrams/u1_types_dv.png){width=4.2in}

**Diagram explanation:** the chart type is chosen by the **purpose** of the question: compare → bar; trend → line; part-of-whole → pie; relationship → scatter; spread → histogram/box; location/links → map/network.

| No. | Type | How it shows data | Best for | Example / Application |
|---|---|---|---|---|
| 1 | **Bar / column chart** | Rectangular bars, length ∝ value | Comparing **discrete categories** | Sales of 5 products |
| 2 | **Line chart** | Points joined by lines | **Trends over time** | Monthly temperature, stock price |
| 3 | **Pie chart** | Slices of a circle | **Part-to-whole** (%) | Market share of brands |
| 4 | **Scatter plot** | One dot per record (x, y) | **Relationship / correlation**, clusters | Height vs weight |
| 5 | **Area chart** | Line chart with area filled | **Cumulative** totals over time | Total website traffic by source |
| 6 | **Heat map** | Colour intensity in a 2-D matrix | **Patterns / correlations** in a matrix | Correlation matrix, hourly footfall |
| 7 | **Bubble chart** | Scatter + bubble size = 3rd variable | **Three variables** | GDP vs life expectancy, size = population |
| 8 | **Histogram** | Bars over value ranges (bins) | **Distribution / frequency** | Exam-mark distribution |
| 9 | **Box plot** | Median, quartiles, whiskers, outliers | **Spread & outliers** | Salary spread per department |
| 10 | **Choropleth map** | Regions coloured by value | **Geographic** variation | COVID cases per state |
| 11 | **Tree map** | Nested rectangles, area ∝ value | **Hierarchical** part-to-whole | Disk usage by folder |
| 12 | **Network graph** | Nodes + edges | **Relationships / connections** | Social network friends |
| 13 | **Word cloud** | Word size ∝ frequency | **Text** frequency | Customer review keywords |

### Applications (where each family is used)

- **Business intelligence dashboards**: bar, line, pie, KPI charts.
- **Science & research**: scatter, histogram, box plot, heat map.
- **Geography / public health**: choropleth maps.
- **Social media / IT**: network graphs, word clouds.

**Conclusion:** No single chart fits all data; select the type by the **question you want to answer** and the **type of data** (categorical, numerical, temporal, spatial).

> **Memory trick: "CT-PR-DS"**: **C**ompare (bar), **T**rend (line), **P**art-whole (pie), **R**elationship (scatter), **D**istribution (histogram/box), **S**patial (map).
> **Common mistake:** using a pie chart for more than 5-6 categories or for trends over time.

## 1.3 Explain (scientific) design choices in data visualization. Why are they important?

**★★★ | Asked for max 8 marks → written for 10 | Asked in: 2024 (8), 2025 (6), 2026 (6) | Source: DMV Textbook.pdf, PDF p. 49-51 (3.5 Scientific Design Choices in Data Visualization)**

Variants: "Explain in detail design choices in data visualization" (2024) · "What are some key Scientific Design Choices ... why are they important?" (2025) · "Explain the concept of scientific design choices in visualization" (2026).

**Definition:** **Scientific design choices** are the **deliberate, well-informed decisions** a practitioner makes so that a visualization is **accurate, clear and effective**. They follow evidence about **human perception**, not personal taste.

![Scientific design choices](diagrams/u1_design_choices.png){width=5.2in}

**Diagram explanation:** each branch below is one decision the designer must take before the chart is final.

### Key design choices

1. **Visualization (chart) type**: match the chart to the data: bar for **categories**, line for **time trends**, scatter for **relationships**.
2. **Visual encodings**: map data to **position, length, size, colour, shape**. Position and length are read most accurately; use them for the most important variable.
3. **Colour palette**: colours must be **distinguishable** and meaningful; use **perceptually uniform** scales (e.g. viridis) for numbers and **colour-blind-safe** palettes.
4. **Scales and axes**: start bar axes at **zero**, use **log scale** for wide ranges, label units and ticks clearly. A truncated axis **distorts** differences.
5. **Labels, titles and annotations**: informative **title**, **axis labels with units**, **legend**, notes on important points.
6. **Data-ink ratio**: maximise ink used for data; remove **chartjunk** (3-D effects, heavy grids, shadows). (Edward **Tufte**'s idea.)
7. **Data density**: avoid over-plotting; use transparency, sampling or aggregation.
8. **Interactivity**: tooltips, zoom, filter, but only when they help.
9. **Accessibility & responsiveness**: readable fonts, alt-text, works on mobile screens.
10. **User-centric design & storytelling**: design for the target **audience** and guide them through a clear **narrative**.

### Why they are important

- Prevent **misleading** interpretations (e.g. truncated y-axis exaggerates a 2% rise).
- Make comparisons **reliable and quick**.
- Improve **clarity, trust and decision-making**.
- Make charts **inclusive** (colour-blind viewers).

**Example:** Showing monthly revenue for 3 regions: choose a **line chart**, encode region by **colour** (3 distinct colour-blind-safe hues), **y-axis from 0 with ₹ units**, a clear title "Monthly Revenue by Region, 2025", no 3-D effects.

**Conclusion:** Scientific design choices turn raw charts into **honest, readable and persuasive** visuals; they are the difference between information and decoration.

> **Memory trick: "TEC-SL-DI-A"**: **T**ype, **E**ncoding, **C**olour, **S**cale, **L**abels, **D**ata-ink, **I**nteractivity, **A**udience.

## 1.4 Explain the need / role of graphics and computing in data visualization (and how exploratory graphics help)

**★★ | Asked for max 10 marks → written for 12 | Asked in: 2023 (10), 2025 (6) | Source: DMV Textbook.pdf, PDF p. 45 (3.3.1 Graphics), p. 46-48 (3.3.2-3.3.5 Computing, Computational Power and Rendering, Graphic Speed and Power); p. 44-45 (Exploratory Graphics)**

Variants: "Explain need of Graphics and computing in data visualization. How exploratory graphics is useful in visualization." (2023) · "Discuss the role of Computing in Graphics and its impact on Data Visualization." (2025)

**Introduction:** **Graphics** are the **visual bridge** between raw data and human understanding. **Computing** is the **engine** that processes data, calculates statistics and **renders** graphics quickly and interactively.

### 1. Need of graphics in data visualization

1. **Visual perception**: the human eye sees patterns in a picture much faster than in tables of numbers.
2. **Communication**: complex data becomes understandable to **non-technical** audiences.
3. **Exploration and discovery**: reveals hidden **patterns, outliers, correlations**.
4. **Context and comparison**: easy comparison between categories / time periods.
5. **Storytelling**: graphics build a data-driven **narrative** for decisions.

### 2. Role of computing in data visualization

![Role of computing](diagrams/u1_computing.png){width=5.8in}

**Diagram explanation (each block):**

- **Raw data**: messy, large, many formats.
- **Data processing**: computer **cleans, integrates and aggregates** data.
- **Statistical computation**: calculates **mean, median, SD, correlation**, runs models (clustering, regression).
- **Mapping**: converts values into **visual properties**: position (x, y), size, colour, shape; computes scales and coordinates.
- **Rendering (CPU/GPU)**: draws thousands of elements; **GPU** and **parallel processing** make it fast.
- **User interaction**: zoom, pan, filter; computing **re-calculates and re-draws** in real time (dashed loop).

### 3. Impact of computing on visualization (graphic speed and power)

- **Speed**: fast rendering enables **real-time, interactive** charts; slow rendering frustrates exploration.
- **Power**: ability to handle **big data** and **3-D / complex** visuals without losing quality.
- **Strategies used:** **data aggregation**, **simplification / level-of-detail**, **progressive loading**, **GPU acceleration**, **parallel processing**, **caching**.
- **Advanced analysis**: machine-learning results (clusters, predictions) can be visualized directly.

### 4. How exploratory graphics help (2023 part)

- Quick **first look** at data **without a fixed hypothesis**.
- Detect **outliers**, clusters and relationships → **generate hypotheses**.
- Interactive and flexible: zoom, filter, drill-down.
- Typical tools: **scatter plots, histograms, box plots, heat maps**.

### Applications

Business-intelligence dashboards, scientific research, **EDA**, geospatial maps, data journalism, data-driven art.

**Conclusion:** Graphics make data **understandable**; computing makes graphics **possible, fast and interactive**. Together they turn large datasets into **insight**.

> **Exam tip:** Draw the 6-block pipeline (Data → Process → Compute → Map → Render → Display, with interaction loop). It earns diagram marks quickly.
> **Memory trick (need of graphics): "PCECS"**: **P**erception, **C**ommunication, **E**xploration, **C**omparison, **S**torytelling.

## 1.5 Write a short note on statistical historiography in data visualization

**★★ | Asked for max 8 marks → written for 10 | Asked in: 2023 (8), 2025 (6) | Source: DMV Textbook.pdf, PDF p. 48-50 (3.4 Statistical Historiography, 3.4.1 Features, 3.4.2 Applications)**

**Definition:** **Statistical historiography** is the **study of the history and evolution** of statistical graphics and visual representations of data: their **origins**, how they changed over time, and the **pioneers** who shaped the field.

### 1. Timeline of key milestones

![Milestones in statistical graphics](diagrams/u1_historiography.png){width=5.8in}

**Diagram explanation:**

- **William Playfair (late 18th century)**: invented the **line graph, bar chart and pie chart**.
- **John Snow (1854)**: **cholera map** of London; clustering of deaths around a water pump proved cholera was water-borne.
- **Florence Nightingale (1858)**: **coxcomb (polar area) chart** of Crimean-War deaths; changed hospital sanitation **policy**.
- **Charles Minard (1869)**: flow map of **Napoleon's march to Moscow** (six variables in one chart).
- **John Tukey (1970s)**: **exploratory data analysis (EDA)**, box plot.
- **Edward Tufte (1980s)**: **data-ink ratio**, avoiding **chartjunk** and misleading graphics.
- **Mid-20th century → today**: **computers**, then the **internet**, interactive web charts, data journalism and AI-assisted visualization.

### 2. Features

1. **Historical context**: explains where today's charts came from.
2. **Contributions of pioneers**: Playfair, Nightingale, Snow, Minard.
3. **Evolution of techniques**: from **hand-drawn static** charts to **interactive, computer-generated** graphics.
4. **Influence on decision-making**: Snow's map and Nightingale's charts changed public policy.
5. **Impact on communication**: stresses honest, effective presentation (Tukey, Tufte).

### 3. Applications

1. **Informing best practices**: learn from past successes and mistakes.
2. **Inspiring innovation**: old creative ideas inspire new chart types.
3. **Research and education**: teaching the evolution of visualization.
4. **Data journalism**: historical examples improve data-driven storytelling.
5. **Interdisciplinary collaboration**: brings together statisticians, computer scientists, designers, domain experts.

**Conclusion:** Statistical historiography shows that good visualization has always **changed decisions**; studying it helps us build better, more honest visuals today.

> **Memory trick: "Please Save Nurses' Maps, Tukey Teaches"** = **P**layfair → **S**now → **N**ightingale → **M**inard → **T**ukey → **T**ufte (chronological order).

## 1.6 What is computational statistics? Explain its role in data visualization

**★★ | Asked for max 8 marks → written for 10 | Asked in: 2024 (8), 2025 (6) | Source: DMV Textbook.pdf, PDF p. 43-44 (3.1.2 Computational Statistics, 3.1.3 Applications)**

Variants: "Write a short note on Role of Computational Statistics in data visualization" (2024) · "What is Computational Statistics, and how does it relate to Data Visualization?" (2025).

**Definition:** **Computational statistics** is an **interdisciplinary field** that combines **statistics, mathematics and computer science** to solve complex data-analysis problems using **algorithms, simulation and high-performance computing**. It arose because data grew too large for hand calculation.

![Computational statistics and visualization](diagrams/u1_comp_stats.png){width=6.2in}

**Diagram explanation:** three disciplines feed computational statistics; it **computes** the summaries, models and uncertainties that the visualization **draws**; the visualization in turn **suggests new hypotheses** (dashed arrow) to test computationally.

### 1. Key aspects of computational statistics

1. **Algorithm development**: numerical algorithms for statistics on large data.
2. **Simulation techniques**: **Monte Carlo** simulation to model uncertain systems.
3. **Bayesian inference**: computational methods (e.g. MCMC) for complex Bayesian models.
4. **High-performance computing**: **parallel and distributed** processing of big data.
5. **Machine-learning integration**: predictive models, pattern discovery.
6. **Resampling methods**: **bootstrapping, cross-validation** to estimate uncertainty.
7. **Optimisation**: numerical methods for **maximum likelihood estimation**.

### 2. Role / relation to data visualization

- **Computes what is drawn**: histograms need bin counts, box plots need quartiles, regression lines need fitted coefficients.
- **Uncertainty display**: bootstrap **confidence intervals** shown as error bars / bands.
- **Dimensionality reduction**: **PCA, MDS, t-SNE** compress many variables into 2-D plots.
- **Density estimation & smoothing**: KDE curves, moving averages.
- **Clustering / classification results** coloured on scatter plots.
- **Big-data visualization**: aggregation and sampling algorithms make plotting millions of points possible.
- **Visual diagnostics**: residual plots, Q-Q plots check model assumptions.

### 3. Applications

**Data science**, **bioinformatics** (genetic data), **finance** (risk modelling, option pricing), **environmental science** (climate models), social sciences.

**Example:** Estimating average delivery time with a 95% bootstrap confidence interval (1,000 resamples) and plotting it as a bar with an **error bar**.

**Conclusion:** Computational statistics is the **calculating brain** behind visualization, and visualization is the **window** through which its results are understood.

> **Memory trick: "A-S-B-H-M-R-O"** → "**A S**mart **B**oy **H**as **M**any **R**ich **O**ptions" (Algorithms, Simulation, Bayesian, HPC, ML, Resampling, Optimisation).

## 1.7 Differentiate between presentation graphics and exploratory graphics with examples

**★★ | Asked for max 6 marks → written for 8 | Asked in: 2025 (6), 2026 (5) | Source: DMV Textbook.pdf, PDF p. 44-45 (3.2 Presentation and Exploratory Graphics)**

**Introduction:** **Presentation graphics** are polished visuals made to **communicate** known insights to an **audience**. **Exploratory graphics** are quick visuals made by an **analyst** to **discover** patterns in data **without a preconceived hypothesis**.

| No. | Point | Presentation graphics | Exploratory graphics |
|---|---|---|---|
| 1 | **Purpose** | **Communicate** a known message | **Discover** unknown patterns, generate hypotheses |
| 2 | **Audience** | Others: managers, clients, public | The analyst / researcher themselves |
| 3 | **Stage of analysis** | End (reporting) | Beginning (EDA) |
| 4 | **Design effort** | High: polished colours, fonts, layout | Low: quick and rough |
| 5 | **Number made** | Few, carefully chosen | Many, made and discarded quickly |
| 6 | **Annotations** | Titles, labels, captions, story | Minimal labels |
| 7 | **Interactivity** | Mostly **static** (reports, slides) | Often **interactive**: zoom, filter, drill-down |
| 8 | **Focus** | **Clarity, simplicity, storytelling** | **Flexibility, speed, completeness** |
| 9 | **Typical charts** | Bar, line, pie, infographics | Scatter, histogram, box plot, density plot, heat map |
| 10 | **Example** | Annual-report bar chart of yearly profit | Scatter-matrix of all variables to spot correlations and outliers |

**Examples:**

- **Presentation:** a clean line chart "Revenue grew 18% in 2025" shown in a board meeting.
- **Exploratory:** an analyst draws 20 histograms and box plots of a new customer dataset and notices age has outliers (age = 999).

**Conclusion:** Exploratory graphics help **find** the story; presentation graphics help **tell** the story.

> **Memory trick:** **E**xploratory = **E**xamine (for me); **P**resentation = **P**ublic (for them).

## 1.8 Define static graphics. Discuss the features of a complete plot

**★ | Asked for max 6 marks → written for 8 | Asked in: 2026 (6) | Source: DMV Textbook.pdf, PDF p. 53-55 (3.7 Static Graphics, 3.7.2 Complete Plots and their implementation in Matplotlib)**

**Definition (static graphics):** **Static graphics** are visualizations that are **fixed and non-interactive**: an image (chart, map, infographic) that the viewer cannot zoom, filter or change. Examples: charts in **printed reports, books, academic papers, slides**.

### 1. Characteristics of static graphics

- **Simple** and easy to understand; convey a **clear, concise message**.
- **Reproducible**: same image can be reused in many documents.
- **Computationally efficient**: generated and rendered quickly.
- Need careful **design** (colour, size, layout) because the user cannot interact.
- **Limitation:** cannot show complex, multi-layer data or allow exploration.

**Definition (complete plot):** A **complete plot** is a **self-contained** visualization that includes **all the elements needed** to understand the data at a glance, without extra explanation.

![Anatomy of a complete plot](diagrams/u1_complete_plot.png){width=5.6in}

### 2. Features of a complete plot (labelled in the figure)

1. **Title** ①: tells what the plot shows.
2. **Axis labels with units** ②③: the scale and meaning of each axis.
3. **Legend** ④: identifies each series/colour (data points vs regression line).
4. **Scales, ticks and grid** ⑤: allow accurate reading of values.
5. **Annotations**: arrows or text explaining important points (e.g. highest sale).
6. **Appropriate colours and markers**: distinguish groups and highlight key data.
7. **Summary elements**: e.g. **regression line** on a scatter plot, **median/quartiles/outliers** in a box plot.
8. **Balance**: enough detail to be complete, but no clutter.

### 3. Implementation (Matplotlib)

```python
plt.scatter(x, y, label="Data Points")
plt.plot(x, m*x + c, color="r", label="Regression Line")
plt.title("Scatter Plot with Regression Line")
plt.xlabel("X"); plt.ylabel("Y"); plt.legend(); plt.show()
```

**Conclusion:** Static graphics are best for **print and reports**; making each one a **complete plot** ensures it is understood **without the presenter**.

> **Memory trick: "TALL-SAC"**: **T**itle, **A**xis labels, **L**egend, **L**ines/grid (scale), **S**ummary line, **A**nnotations, **C**olours.

## 1.9 Write short notes on output formats and speed issues

**★ | Asked for max 6 marks → written for 8 | Asked in: 2026 (6) | Source: DMV Textbook.pdf, PDF p. 57 (3.8.2 Output Formats); p. 46-47 (Graphic Speed and Power, Computational Power and Rendering)**

### (a) Output formats

**Definition:** **Output formats** are the different ways visualizations or model results are **presented, shared or saved**. The choice depends on data complexity, **audience**, need for **interactivity**, and intended use.

![Output formats](diagrams/u1_output_formats.png){width=4.4in}

1. **Static images**: **PNG, JPEG** (raster, pixel-based), **SVG, PDF** (vector, scale without blur). Used in **reports, papers, slides**.
2. **Interactive web-based visualizations**: **D3.js, Plotly, Bokeh**; embedded in websites; user can zoom, filter.
3. **Dashboards**: **Tableau, Power BI, Grafana**; collection of linked charts for real-time monitoring and business intelligence.
4. **Animated visualizations**: **GIF, MP4**; show change over time, simulations.
5. **Data files**: **CSV, JSON** for model outputs (predictions, feature importances) to reuse in other tools.
6. **Model serialization**: **Pickle, ONNX, PMML**; save trained models.
7. **3-D printing**: physical models in engineering and medical visualization.

### (b) Speed issues

**Meaning:** **Speed** = how quickly a visualization is **rendered and updated** when data or user input changes. Slow rendering frustrates users and blocks interactive exploration, especially with **big data** or **3-D** charts.

**Causes of slowness:** very large number of points, complex 3-D/animated graphics, heavy computations on every interaction, limited hardware.

**Strategies to improve speed:**

1. **Data aggregation / binning**: draw summaries, not every row.
2. **Sampling and simplification**: fewer points / **level-of-detail (LOD)** rendering.
3. **Progressive loading**: show a rough view first, add detail later.
4. **GPU acceleration** for 3-D and real-time graphics.
5. **Parallel processing** and **caching** of computed results.
6. Choose a **lighter format** (PNG instead of SVG with 1 lakh elements; WebGL for big web charts).

**Conclusion:** Pick the output format to fit the **audience and medium**, and manage speed by **reducing what must be drawn** and using **hardware acceleration**.

> **Memory trick (formats): "SIDAD-M3"**: **S**tatic, **I**nteractive, **D**ashboard, **A**nimated, **D**ata files, **M**odel serialization, **3**-D print.

## 1.10 Explain 3-D plots in data modeling and visualization

**★ | Asked for max 5 marks → written for 7 | Asked in: 2026 (5) | Source: DMV Textbook.pdf, PDF p. 56-57 (3.8.1 What are 3D Plots?)**

**Definition:** **3-D plots** are visual representations of data in **three dimensions (x, y, z)**. They are used when data has **three variables** or has **spatial, temporal or volumetric** nature, giving a fuller view of structure and patterns.

### Types of 3-D plots

| Type | What it shows | Example |
|---|---|---|
| **3-D scatter plot** | Points defined by 3 attributes | Height, weight, age of patients |
| **3-D surface plot** | Continuous surface z = f(x, y) | Terrain elevation, loss surface |
| **3-D line plot** | Line through 3-D points | Flight path / trajectory over time |
| **3-D bar plot** | Bars across two category axes | Sales by region × year |

### Uses in data modeling

1. **3-D feature space**: see how three features relate to the target.
2. **3-D decision boundaries**: how a classifier separates classes.
3. **Model evaluation / hyperparameter tuning**: accuracy as a surface over two hyperparameters.
4. **Medical & engineering**: CT/MRI volume rendering, CAD models.

### Implementation (Matplotlib)

```python
from mpl_toolkits.mplot3d import Axes3D
ax = plt.figure().add_subplot(projection="3d")
ax.scatter(x, y, z)
```

### Limitations

- **Occlusion** (points hide each other) and **perspective distortion** make values hard to read.
- Harder to interpret on paper; needs rotation/interaction.
- Not suitable for **very high-dimensional** data (use PCA/MDS instead).

**Conclusion:** 3-D plots are powerful for **spatial and three-variable** data but must be used **judiciously**; a 2-D chart is often clearer.

> **Exam tip:** Always mention one **limitation** (occlusion/distortion); examiners look for balanced answers.

# Last-Minute Revision Sheet: Unit 1

| Topic | Key points to write |
|---|---|
| **Data handling** | Acquire → Clean → Transform → Integrate → Reduce → Filter → Explore. Accuracy (no bias/duplicates) + Performance (aggregate, sample). **"ACT I R F E"** |
| **Types of DV** | Bar (compare), Line (trend), Pie (part-whole), Scatter (relationship), Histogram/Box (distribution), Heat map, Bubble, Choropleth, Tree map, Network, Word cloud. **"CT-PR-DS"** |
| **Design choices** | Chart type, encoding, colour, scale/axes (start at 0), labels, data-ink ratio (no chartjunk, Tufte), interactivity, audience/accessibility. **"TEC-SL-DI-A"** |
| **Graphics & computing** | Graphics = visual bridge (perception, communication, exploration, comparison, storytelling). Computing = process → compute → map → render (GPU) → interact. Speed & power. |
| **Statistical historiography** | History of statistical graphics. Playfair (line/bar/pie), Snow (cholera map 1854), Nightingale (coxcomb 1858), Minard (1869), Tukey (EDA, box plot), Tufte (data-ink). |
| **Computational statistics** | Stats + maths + CS. Algorithms, Monte Carlo, Bayesian, HPC, ML, bootstrap/cross-validation, optimisation (MLE). Computes what charts draw. |
| **Presentation vs exploratory** | Presentation: communicate, audience, polished, static. Exploratory: discover, analyst, quick, interactive. **E = Examine, P = Public** |
| **Static graphics / complete plot** | Static = fixed, non-interactive. Complete plot = title, axis labels+units, legend, scale/grid, annotations, summary line. **"TALL-SAC"** |
| **Output formats** | PNG/JPEG/SVG/PDF, interactive web (D3, Plotly, Bokeh), dashboards (Tableau, Power BI), GIF/MP4, CSV/JSON, Pickle/ONNX/PMML, 3-D print. |
| **Speed** | Aggregation, sampling/LOD, progressive loading, GPU, parallel processing, caching. |
| **3-D plots** | Scatter, surface, line, bar in 3-D. Uses: feature space, decision boundary, model tuning. Limits: occlusion, distortion. |

**Key formulas / facts:**

- **Data-ink ratio** = ink used to show data ÷ total ink used in the graphic (aim close to 1).
- **Box plot** = min, **Q1**, **median (Q2)**, **Q3**, max; **IQR = Q3 − Q1**; outlier if value < Q1 − 1.5·IQR or > Q3 + 1.5·IQR.

# Assumptions & Gaps

- Exam Unit 1 = question pair Q1/Q2 = syllabus Unit III "Basics of Data Visualization" (textbook Chapter 3, PDF p. 43-58).
- The only DMV study material is the textbook (no separate lecture notes in the repo); all citations are to `Textbooks/DMV Textbook.pdf`, using **PDF page numbers**. The PDF is scanned; text was read via OCR, and some pages (e.g. p. 46, 49, 57) are partly blurred, so missing words were completed from standard subject knowledge consistent with the visible text.
- **Historiography dates and names** (Playfair, Snow 1854, Nightingale 1858, Minard 1869, Tukey, Tufte) are in the textbook (PDF p. 48-50) except exact years for Playfair/Minard/Tukey/Tufte, which are added from standard knowledge.
- **Data-ink ratio formula, box-plot IQR rule and the code snippets** are standard knowledge added for completeness (the textbook mentions the concepts and shows similar Matplotlib code on PDF p. 54-55).
- 2023 Q1a (graphics & computing + exploratory graphics) is answered under 1.4, with a section on exploratory graphics.
- No question in this unit was missing from the materials; no "⚠ Not found" flags were needed.
