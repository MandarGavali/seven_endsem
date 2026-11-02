---
title: "Data Modeling and Visualization: Unit 3 Exam Answers"
subtitle: "Unit 3 (Q5/Q6): Data Aggregation and Analysis | Syllabus Unit V"
---

# Unit Snapshot

| No. | Question | Max Marks | Years Asked | Importance |
|---|---|---|---|---|
| 3.1 | Data aggregation (importance for group operations) with example | 9 | 2023, 2024, 2025 | ★★★ |
| 3.2 | GroupBy mechanics in data aggregation | 9 | 2023, 2024, 2025 | ★★★ |
| 3.3 | Cross tabulation and its uses with example | 9 | 2023, 2025, 2026 | ★★★ |
| 3.4 | Time series basics; time-indexed vs regular data | 9 | 2024, 2026 | ★★★ |
| 3.5 | Short note: pivot tables | 5 | 2023, 2024, 2025, 2026 | ★★★ |
| 3.6 | Short note: periods and period arithmetic | 5 | 2023, 2024, 2026 | ★★★ |
| 3.7 | Moving window functions | 9 | 2025 | ★ |
| 3.8 | Resampling and its role in analysis and smoothing | 8 | 2026 | ★ |
| 3.9 | Steps in split-apply-combine | 4 | 2023 | ★ |

**Must-do first (★★★):** 3.1 Data aggregation · 3.2 GroupBy · 3.3 Cross tabulation · 3.4 Time series basics · 3.5 Pivot tables · 3.6 Periods.

This is the most predictable unit: 6 of its 9 questions are ★★★. All answers are written for **(highest marks + 2)**. Source = `Textbooks/DMV Textbook.pdf` (scanned; PDF page numbers).

# Full Answers

## 3.1 Explain data aggregation and its importance for group operations, with example

**★★★ | Asked for max 9 marks → written for 11 | Asked in: 2023 (8 + short note 5), 2024 (9), 2025 (short note 4.5) | Source: DMV Textbook.pdf, PDF p. 67-70 (5.1 Introduction: Data Aggregation; 5.2.2 Data Aggregation; 5.2.2(A) Uses)**

Variants: "Describe in detail data aggregation with its importance for group operations" (2023) · "Explain Data aggregation with suitable example" (2024) · Short note: Data Aggregation (2023, 2025).

**Definition:** **Data aggregation** is any process in which information is **gathered and expressed in a summary form**, for purposes such as statistical analysis. **Atomic data rows** are replaced by **summary statistics** (sum, mean, count, ...) computed over **groups** of observations.

### 1. Process of data aggregation

![Data aggregation process](diagrams/u3_aggregation.png){width=6.2in}

1. **Collection**: aggregation tools **extract** data from multiple sources (databases, files, APIs, **IoT devices**, social media, call centres) and store it.
2. **Processing**: data is **grouped** by key variables and **aggregation functions** are applied (statistical functions, sometimes predictive analytics/ML).
3. **Presentation**: the summarised result is shown as **tables, charts, dashboards** that give new insight.

### 2. Common aggregation functions

| Function | Meaning | pandas |
|---|---|---|
| **sum** | Total | `.sum()` |
| **mean** | Average | `.mean()` |
| **median** | Middle value | `.median()` |
| **count** | Number of non-null values | `.count()` |
| **min / max** | Smallest / largest | `.min()`, `.max()` |
| **std / var** | Spread | `.std()`, `.var()` |
| **first / last** | First / last value in group | `.first()`, `.last()` |

### 3. Types of aggregation

- **Single-level**: group by one key (sales per category).
- **Multi-level (hierarchical)**: group by several keys (sales per **category and region**).
- **Time-based**: group by day/week/month (monthly revenue) → reveals **trends and seasonality**.
- **Spatial**: totals by country/state.

### 4. Importance for group operations

1. **Summarises large datasets** into manageable information.
2. Gives **information about particular groups** (by age, profession, income, region).
3. **Speeds up queries**: one aggregate row can stand for thousands of records (used in **data warehouses / OLAP**).
4. **Comparison** across groups → better **decision-making** (best region, weakest product).
5. Basis for **visualization**: bar/line/pie charts are drawn from aggregated values.
6. **Anonymisation**: individual personal details are hidden inside group summaries (e.g. average salary by department).
7. Supports **trend & seasonality analysis** through time-based aggregation.

### 5. Examples

- **Voter turnout by state**: individual voters are not shown, only totals per candidate.
- **Average age of customers by product**.
- **Number of customers by country**.
- Music website: shows CD ads based on the **user's age group** aggregate (web personalisation).

```python
df.groupby("category")["sales"].sum()                       # single-level
df.groupby(["category", "region"])["sales"].agg(["sum", "mean"])  # multi-level
df.resample("M", on="date")["sales"].sum()                  # time-based
```

**Precautions:** check the **accuracy of atomic data** and ensure **enough data** is aggregated (counting votes when only 5% are in gives a misleading total).

**Uses:** finance and business strategy, product planning, **pricing**, operations optimisation, **marketing**, statistical analysis.

**Conclusion:** Data aggregation turns **raw rows into group-level insight**; combined with GroupBy it is the core of reporting, OLAP and visualization.

> **Memory trick: "CPP"**: **C**ollect, **P**rocess, **P**resent. Functions: "**S**ome **M**en **M**ust **C**ount **M**oney **S**afely" (Sum, Mean, Median, Count, Min/Max, Std).

## 3.2 Explain GroupBy mechanics in data aggregation. How does it facilitate data analysis?

**★★★ | Asked for max 9 marks → written for 11 | Asked in: 2023 (6), 2024 (9), 2025 (9) | Source: DMV Textbook.pdf, PDF p. 68 (5.2.1 Group by Mechanics), p. 70-72 (Split-Apply-Combine and pandas GroupBy examples)**

Variants: "Explain Group by Mechanics technique in data modeling and visualization" (2023, 2024) · "What is the Group by mechanism in data aggregation, and how does it facilitate data analysis?" (2025).

**Definition:** **GroupBy** is the operation of **dividing a dataset into distinct groups** based on the values of one or more **key variables** and then **performing calculations within each group**. In pandas it follows the **split-apply-combine** strategy (term by **Hadley Wickham**).

![Split-apply-combine with GroupBy](diagrams/u3_split_apply_combine.png){width=6in}

### 1. Mechanics (how it works)

1. **Data structure**: data in a **DataFrame / table**: each row = observation, each column = variable.
2. **Choose key variable(s)**: usually **categorical/discrete** (product category, region, customer ID). Keys may be a **column name, array, dictionary, Series or function**.
3. **Split**: rows with the **same key value** are put in the **same group** (A, B, C in the figure).
4. **Apply**: a function is applied **to each group independently**:
   - **Aggregation**: sum, mean, count, std → one value per group.
   - **Transformation**: normalisation, rank, fill missing with group mean → same shape as input.
   - **Filtration**: keep only groups meeting a condition (groups with > 100 sales).
5. **Combine**: results are **merged into a new DataFrame/Series** indexed by the group keys.

**Diagram explanation:** the table is **split** by `key` into three groups; **sum()** is **applied** to each; the three results are **combined** into one result table (A = 30, B = 20, C = 10).

### 2. pandas syntax

```python
grouped = df.groupby("category")                 # GroupBy object (lazy, nothing computed yet)
grouped["sales"].sum()                            # aggregation
df.groupby(["category", "region"])["sales"].mean()   # multi-level grouping
df.groupby("category").agg({"sales": "sum", "qty": ["mean", "max"]})   # several functions
df.groupby("category")["sales"].transform(lambda x: x / x.sum())       # transformation
df.groupby("category").filter(lambda g: g["sales"].sum() > 100)        # filtration
for name, group in df.groupby("category"): print(name, len(group))    # iterate groups
```

### 3. Multi-level grouping

Grouping by **category and region** creates a **hierarchical (MultiIndex)** result, giving insight such as how each product performs in each region. `unstack()` turns it into a table for plotting.

### 4. How GroupBy facilitates data analysis

1. **Summarises** large datasets per group (total sales per category).
2. **Comparison** of groups: find top-performing categories, regions, time periods.
3. **Pattern & outlier detection** within groups.
4. **Feature engineering**: group means/ranks as new features.
5. **Data cleaning**: fill missing values with group-wise mean.
6. **Feeds visualization**: grouped results go straight to **bar, line, pie charts**.
7. **Decision-making**: resource allocation, marketing strategy, inventory planning.
8. More **expressive than SQL GROUP BY**: any Python function can be applied.

### Example

Sales data with `category`, `date`, `amount` → `df.groupby("category")["amount"].sum()` → Electronics ₹5.2 L, Clothing ₹3.1 L, Grocery ₹1.4 L → plotted as a bar chart → Electronics is the top category.

**Conclusion:** GroupBy = **split by key → apply function → combine results**. It is the main tool for group-level analysis in pandas, SQL and Excel.

> **Memory trick:** "**S-A-C = Split, Apply, Combine**" and the 3 apply types "**ATF**" (**A**ggregate, **T**ransform, **F**ilter).

## 3.3 Explain cross tabulation and its uses with a suitable example

**★★★ | Asked for max 9 marks → written for 11 | Asked in: 2023 (8), 2025 (9), 2026 (9) | Source: DMV Textbook.pdf, PDF p. 76 (5.2.5 Cross Tabulation)**

**Definition:** **Cross tabulation** (a **contingency table**, "crosstab") is a technique to analyse the **relationship between two (or more) categorical variables**. It shows the **frequency distribution** (counts or percentages) for **every combination** of categories: one variable forms the **rows**, the other the **columns**.

**Terminology:** **Banner** = column variable · **Stub** = row variable · **Cell** = count for one combination · **Marginal totals** = row/column totals · **Expected values** and **Chi-square statistic** = test of independence.

### 1. Example: Gender vs "Do you like our product?" (survey of 100 customers)

| Gender \\ Response | Like | Dislike | **Row total** |
|---|---|---|---|
| **Male** | 30 (60%) | 20 (40%) | **50** |
| **Female** | 40 (80%) | 10 (20%) | **50** |
| **Column total** | **70** | **30** | **N = 100** |

*(Percentages are row percentages.)*

**Reading:** 80% of women like the product compared with 60% of men, so the company should study what male customers dislike.

### 2. Test of independence (Chi-square)

**Expected count:** E = (Row total × Column total) / N

- E(Male, Like) = 50 × 70 / 100 = **35**; E(Male, Dislike) = 50 × 30 / 100 = **15**; similarly Female: 35 and 15.

**Chi-square:** χ² = Σ (O − E)² / E

= (30−35)²/35 + (20−15)²/15 + (40−35)²/35 + (10−15)²/15 = 0.714 + 1.667 + 0.714 + 1.667 = **4.76**

**Degrees of freedom** = (rows − 1)(columns − 1) = 1. Critical value at 5% = **3.84**. Since **4.76 > 3.84**, **gender and liking are related** (not independent).

Symbols: **O** = observed count, **E** = expected count, **N** = grand total.

### 3. In pandas

```python
pd.crosstab(df["gender"], df["response"], margins=True)                  # counts + totals
pd.crosstab(df["gender"], df["response"], normalize="index")             # row %
from scipy.stats import chi2_contingency; chi2_contingency(table)       # test
```

### 4. When to use

When you have **categorical data**: information divided into **mutually exclusive groups** (gender, region, yes/no answers, product type).

### 5. Uses / applications

1. **Survey analysis**: customer reviews by region (North, South, East, West).
2. **Employee engagement & satisfaction**: job role vs satisfaction; exit interviews (leaving vs promotion).
3. **Departmental issues**: are complaints concentrated in one department?
4. **School evaluation surveys**: student feedback vs course material / time spent.
5. **Product research & feedback**: how demographics (age, gender, region) feel about a product.
6. **Medical studies**: treatment vs outcome; smoker vs disease.
7. **Market research**: brand preference by age group.

### 6. Benefits

- **Error reduction**: large data broken into manageable, representative sub-groups.
- **More insights**: reveals relationships that would go unnoticed in totals.
- **Actionable information**: simple tables that managers can act on.
- **Easy to visualise**: as **stacked/grouped bar charts** or **heat maps**.

### Crosstab vs pivot table (one line)

A **crosstab** **counts frequencies** of category combinations by default; a **pivot table** **aggregates a numeric value** (sum/mean) over row and column categories.

**Conclusion:** Cross tabulation is the simplest way to see **how two categorical variables are related**; with the chi-square test it shows whether the relationship is **statistically significant**.

> **Memory trick:** "**Cross-tab = Count the Crossings**" (rows × columns = every combination). Expected value: "**Row × Column ÷ Total**".

## 3.4 Explain time series basics with a suitable example. How does time-indexed data differ from regular datasets?

**★★★ (asked twice at 9 marks) | Asked for max 9 marks → written for 11 | Asked in: 2024 (9, with cross tabulation), 2026 (9) | Source: DMV Textbook.pdf, PDF p. 77-78 (5.2.6 Time Series; 5.3.2 Date and Time Data Types and Tools; 5.3.3 Time Series Basics), p. 78-79 (Date Ranges, Frequencies, Shifting)**

Variants: "Explain in detail cross tabulation & Time Series" (2024) · "Explain Time Series Basics with a suitable example and how time indexed data differs from regular datasets" (2026).

**Definition:** A **time series** is a **sequence of data points collected over successive time intervals**, where each data point corresponds to a **specific time** (timestamp). Examples: daily stock prices, monthly sales, hourly temperature. Used in **finance, economics, climate science, IoT**.

![Time series with trend and seasonality](diagrams/u3_timeseries.png){width=6in}

**Diagram explanation:** the **x-axis is time** (a DatetimeIndex); the blue line is the observed series; the red dashed line is the **trend**; the repeating yearly wave is **seasonality**; small random wiggles are **noise**.

### 1. Key concepts (time series basics)

1. **Trend**: long-term **upward or downward** movement (sales growing every year).
2. **Seasonality**: patterns that **repeat at fixed intervals**: daily, weekly, yearly (ice-cream sales peak every summer).
3. **Cyclic pattern**: rises and falls **without fixed period**, e.g. economic/business cycles.
4. **Irregular / noise**: random variation.
5. **Stationarity**: statistical properties (**mean, variance, autocorrelation**) **constant over time**; needed for most forecasting models; achieved by **differencing** or transformation.
6. **Autocorrelation**: correlation of the series with its own **lagged** values (today vs yesterday).
7. **White noise**: purely random series with no pattern; the **benchmark** for "no information".

**Decomposition model:** Y~t~ = T~t~ + S~t~ + C~t~ + I~t~ (additive) or Y~t~ = T~t~ × S~t~ × C~t~ × I~t~ (multiplicative), where T = trend, S = seasonal, C = cyclic, I = irregular component at time t.

### 2. Date & time tools (pandas)

- **Timestamp** (a moment), **Period** (a span), **Timedelta** (a duration), **DatetimeIndex**.
- `pd.to_datetime()` to parse strings; `pd.date_range(start, end, freq="D")` for **date ranges**.
- **Frequencies**: D (day), W (week), M/MS (month), Q, A/Y, H (hour); regular vs irregular.
- **Shifting / lagging**: `s.shift(1)` moves data forward/backward → **lag features**, % change.
- **Resampling**: `s.resample("M").sum()`; **time-zone handling**: `tz_localize`, `tz_convert` (UTC as reference).
- **Modeling**: **ARIMA**, seasonal decomposition (**STL**) for forecasting.

### 3. Example

```python
dates = pd.date_range("2025-07-01", periods=5, freq="D")
sales = pd.Series([100, 250, 200, 80, 250], index=dates)   # time-indexed
sales["2025-07-02":"2025-07-04"]        # slice by date
sales.shift(1)                          # yesterday's sales
sales.pct_change()                      # daily growth
sales.resample("W").sum()               # weekly total
```

### 4. Time-indexed data vs regular datasets

| No. | Point | Time-indexed (time series) data | Regular (cross-sectional) data |
|---|---|---|---|
| 1 | **Index** | **Timestamps / DatetimeIndex** | Row numbers or IDs |
| 2 | **Order** | **Order matters**; cannot shuffle | Order usually irrelevant |
| 3 | **Dependence** | Observations **depend on past** values (autocorrelation) | Observations usually **independent** |
| 4 | **Patterns** | Trend, seasonality, cycles | No time patterns |
| 5 | **Operations** | Resampling, shifting/lags, rolling windows, date slicing, time-zone conversion | Grouping, filtering, sorting |
| 6 | **Missing data** | Gaps in time; filled by forward-fill/interpolation | Dropped or imputed independently |
| 7 | **Train/test split** | **Chronological** split (past → future) | Random split |
| 8 | **Goal** | **Forecasting** future values | Classification / comparison at one point in time |
| 9 | **Visualization** | **Line charts**, seasonal plots | Bar, scatter, histogram |
| 10 | **Example** | Daily closing price of a stock for 1 year | Marks of 60 students in one exam |

**Conclusion:** A time series is data **ordered and indexed by time**; understanding **trend, seasonality, stationarity and autocorrelation**, and using time-aware tools (date ranges, shifting, resampling), is essential for correct analysis and forecasting.

> **Memory trick: "TSCI"**: "**T**ime **S**eries **C**omponents **I**nclude" Trend, Seasonal, Cyclic, Irregular. Plus "**SAW**" = **S**tationarity, **A**utocorrelation, **W**hite noise.

## 3.5 Write a short note on pivot tables

**★★★ (asked in all 4 papers) | Asked for max 5 marks → written for 7 | Asked in: 2023 (5), 2024 (4.5), 2025 (4.5), 2026 (5) | Source: DMV Textbook.pdf, PDF p. 73-76 (5.2.4 Pivot Tables, Excel steps and two-dimensional pivot table)**

**Definition:** A **pivot table** is a **table of statistics that summarises the data of a larger table** (from a database, spreadsheet or BI tool). It **groups** data by row and column categories and shows an **aggregate** (sum, average, count) at each intersection.

![Building a pivot table](diagrams/u3_pivot.png){width=6.2in}

**Diagram explanation:** raw order rows are grouped by **Product (rows)** and **Country (columns)**; the **Amount** values are **summed** in each cell; **grand totals** are added on the right and bottom.

### Components (Excel PivotTable Fields pane)

1. **Rows**: categories shown down the side (Product).
2. **Columns**: categories across the top (Country) → **two-dimensional** pivot table.
3. **Values**: numeric field to summarise (Amount) with **Value Field Settings**: Sum, Count, Average, Max, Min.
4. **Filters**: show only a subset (e.g. Country = France).

### Creating one

- **Excel:** click any cell → **Insert → PivotTable** → drag fields into Rows, Columns, Values, Filters → sort / change summary.
- **pandas:**

```python
pd.pivot_table(df, index="Product", columns="Country",
               values="Amount", aggfunc="sum", margins=True, fill_value=0)
```

### Advantages / uses

- **Summarises thousands of rows** in seconds without formulas.
- **Interactive**: drag-and-drop, filter, sort, drill-down.
- Quick **comparison** (which product sells most in which country).
- Ready input for **heat maps and grouped bar charts**.

**Example (textbook):** 213 export orders (Order ID, Product, Category, Amount, Date, Country) → pivot shows **Banana** is the main export overall, and **Apple** is the main export to **France**.

**Conclusion:** A pivot table is the fastest way to **summarise and cross-compare** large data by two categories.

> **Memory trick: "RCVF"**: **R**ows, **C**olumns, **V**alues, **F**ilters ("**R**eal **C**ats **V**ery **F**luffy").

## 3.6 Write a short note on periods and period arithmetic

**★★★ | Asked for max 5 marks → written for 7 | Asked in: 2023 (5), 2024 (4.5), 2026 (5) | Source: DMV Textbook.pdf, PDF p. 80-81 (5.3.7 Periods and Periods Arithmetic)**

**Definition:** In time-series analysis, a **period** is a **fixed-length span of time**, such as a **day, month, quarter or year** (e.g. "March 2025" covers 1-31 March). It differs from a **timestamp**, which is a **single point** in time. In pandas: `pd.Period("2025-03", freq="M")`.

### Why periods are useful

- Organise data into **regular intervals** (monthly, quarterly reporting).
- Calculate **monthly averages**, identify **seasonality**, compare periods (Q1 2025 vs Q1 2024).
- Used in **resampling, frequency conversion**, and **financial calculations** (compounding per period, NPV).

### Period arithmetic (operations on periods)

| Operation | Meaning | pandas example | Result |
|---|---|---|---|
| **Addition** | Move forward n periods | `pd.Period("2023-01", "M") + 3` | `Period('2023-04', 'M')` |
| **Subtraction** | Move backward n periods | `pd.Period("2023-01", "M") - 1` | `Period('2022-12', 'M')` |
| **Difference** | Number of periods between two periods | `pd.Period("2023-06","M") - pd.Period("2023-02","M")` | 4 months (`<4 * MonthEnds>`) |
| **Range** | Sequence of periods | `pd.period_range("2023-01", "2023-12", freq="M")` | 12 monthly periods |
| **Frequency conversion** | Change period length | `pd.Period("2023", "A-DEC").asfreq("M", how="start")` | `Period('2023-01', 'M')` |
| **Fiscal quarters** | Quarters with custom year-end | `pd.Period("2024Q4", freq="Q-MAR")` | Jan-Mar 2024 quarter of FY ending March |
| **Timestamp conversion** | Period ↔ timestamp | `p.to_timestamp()`, `ts.to_period("M")` | start of period / its period |

### Example

```python
months = pd.period_range(start="2023-01", end="2023-12", freq="M")
months[0] + 3                 # Period('2023-04', 'M')
months[5] - months[1]         # 4 periods apart
```

**Conclusion:** Periods represent **time spans**, and period arithmetic lets us **shift, compare and convert** them easily for monthly/quarterly analysis.

> **Exam tip:** Clearly write **"Timestamp = point in time, Period = span of time"**; examiners look for this difference. (The textbook also mentions "multiplying" a monthly period by 3 to get a quarter; in pandas this is done with **frequency conversion (`asfreq`)**, not multiplication.)

## 3.7 What are moving window functions? How are they useful in smoothing and analysing time series data?

**★ | Asked for max 9 marks → written for 11 | Asked in: 2025 (9) | Source: DMV Textbook.pdf, PDF p. 81-82 (5.3.9 Moving Window Functions; 5.3.9(A) Example)**

**Definition:** **Moving window functions** are **aggregate functions applied to a fixed-size window of consecutive data points** that **slides along the time axis one step at a time**, recalculating the result at every position. They are used to **smooth noise** and reveal **trends** in time-series data.

![Rolling mean and EMA smoothing](diagrams/u3_rolling.png){width=6in}

**Diagram explanation:** the light line is noisy daily data; the dark line is a **7-day rolling mean** (each point = average of last 7 days); the red dashed line is the **EMA**, which reacts faster because it weights recent days more.

### 1. Basic concept (window of size 3)

Data: 10, 15, 20, 25, 30 → rolling mean (window = 3):

| Day | Value | Window used | Rolling mean |
|---|---|---|---|
| 1 | 10 | (incomplete) | NaN |
| 2 | 15 | (incomplete) | NaN |
| 3 | 20 | 10, 15, 20 | 15 |
| 4 | 25 | 15, 20, 25 | 20 |
| 5 | 30 | 20, 25, 30 | 25 |

### 2. Types of moving window functions

1. **Rolling statistics**: rolling **mean, median, std, min, max** (`s.rolling(7).std()` → volatility).
2. **Moving average (simple, SMA):** SMA~t~ = (x~t~ + x~t−1~ + ... + x~t−n+1~) / n, where **n** = window size, **x~t~** = value at time t.
3. **Exponential moving average (EMA):** EMA~t~ = α·x~t~ + (1 − α)·EMA~t−1~, with **α = 2 / (span + 1)**; gives **exponentially decreasing weights**, more weight to **recent** data (`s.ewm(span=7).mean()`).
4. **Rolling sum**: cumulative values in a window (7-day total sales, rolling COVID case counts).
5. **Expanding window**: window grows from the start (`s.expanding().mean()` → running average).
6. **Custom functions**: `s.rolling(5).apply(func)`.

### 3. Window size

- **Large window** → **smoother** curve but **slower** to react to changes (lag).
- **Small window** → **responsive** but **sensitive to noise**.
- Choose by data frequency: 7 for daily data with weekly pattern, 12 for monthly data with yearly seasonality.

### 4. Boundary effects

At the **start** (and with centred windows, the end) there are not enough points → **NaN**. Handle with `min_periods=1`, **padding**, or **weighted windows** (`win_type="triang"`, `"gaussian"`).

### 5. Usefulness in smoothing and analysing time series

1. **Noise reduction**: removes random fluctuations → clear trend line.
2. **Trend identification**: e.g. 50-day and 200-day moving averages in stock analysis (**crossover signals**).
3. **Volatility measurement**: rolling standard deviation (financial risk).
4. **Anomaly detection**: points far from the rolling mean ± 2·rolling std are outliers.
5. **Feature engineering**: rolling mean/sum as inputs to forecasting models.
6. **Seasonality removal**: a 12-month moving average removes yearly seasonality.

```python
s.rolling(window=3).mean()        # simple moving average
s.ewm(span=3).mean()              # exponential moving average
s.rolling(7, min_periods=1).sum() # rolling 7-day sum
```

**Conclusion:** Moving window functions **slide a fixed window over time** to compute local statistics; they are the simplest and most widely used tools for **smoothing, trend detection and volatility analysis**.

> **Memory trick:** "**Big window = Blurred (smooth), Small window = Sharp (noisy).**" EMA = "**E**xtra weight to **M**ost recent **A**ctivity."

## 3.8 Explain the concept of resampling and its role in data analysis and smoothing

**★ | Asked for max 8 marks → written for 10 | Asked in: 2026 (8) | Source: DMV Textbook.pdf, PDF p. 81 (5.3.8 Resampling and Frequency Conversion, with example), p. 77 (resampling overview)**

**Definition:** **Resampling** is the process of **converting a time series from one frequency to another** by **aggregating** (to a lower frequency) or **interpolating** (to a higher frequency). **Frequency conversion** means changing data to a specified frequency, e.g. daily → monthly.

![Downsampling and upsampling](diagrams/u3_resample.png){width=5.8in}

**Diagram explanation:** from daily data, **downsampling** goes to fewer, coarser points (weekly/monthly) using an aggregate; **upsampling** goes to more, finer points (hourly) and needs a **fill or interpolation** method for new empty slots.

### 1. Types of resampling

| Point | Downsampling | Upsampling |
|---|---|---|
| **Direction** | High → **low** frequency (daily → monthly) | Low → **high** frequency (daily → hourly) |
| **Number of points** | Decreases | Increases (new empty slots) |
| **Method** | **Aggregation**: sum, mean, max, `ohlc()` | **Filling**: `ffill()`, `bfill()`, `interpolate()` (linear, polynomial) |
| **Purpose** | Summarise, smooth, reduce size | Align with finer data, fill gaps |
| **pandas** | `s.resample("M").sum()` | `s.resample("H").interpolate()` |

### 2. Steps (pandas)

1. Make sure the data has a **DatetimeIndex** (`pd.to_datetime`, `set_index`).
2. Call `.resample(rule)`: rule = "W", "M", "Q", "H", ... (like a **time-based GroupBy**).
3. Apply an **aggregation** (downsampling) or a **fill/interpolation** method (upsampling).

```python
dates = pd.date_range("2023-01-01", periods=10, freq="D")
daily = pd.Series(range(10), index=dates)
weekly = daily.resample("W").sum()                 # downsample
hourly = daily.resample("H").interpolate("linear") # upsample
```

### 3. Role in data analysis

1. **Change granularity** to match the question (daily transactions → monthly revenue reports).
2. **Align multiple series** with different frequencies (daily sales + monthly ad spend).
3. **Reduce data size** for faster analysis and plotting.
4. **Handle irregular / missing timestamps** by placing data on a regular grid.
5. **Financial analysis**: OHLC (open-high-low-close) bars from tick data.

### 4. Role in smoothing

- **Downsampling averages out** day-to-day noise: a monthly mean is much smoother than daily data, so **trend and seasonality** become visible.
- Combined with **moving window functions** (3.7) for further smoothing.
- **Interpolation** in upsampling produces a smooth continuous curve between known points.

### Example

Daily website visits for one year (365 noisy points) → `resample("M").mean()` → 12 points showing a clear rise from January to December and a dip in May (holiday season).

**Conclusion:** Resampling **changes the time frequency** of data; **downsampling aggregates and smooths**, **upsampling interpolates and fills**, making time series ready for analysis and visualization.

> **Memory trick:** "**Down = Divide into buckets & aggregate; Up = Un-fill gaps by interpolation.**"

## 3.9 Explain the steps involved in the split-apply-combine strategy

**★ | Asked for max 4 marks → written for 6 | Asked in: 2023 (4) | Source: DMV Textbook.pdf, PDF p. 70-71 (Split-Apply-Combine, Fig. 5.2.3)**

**Definition:** **Split-apply-combine** is the strategy behind **GroupBy**: **split** data into groups, **apply** a function to each group independently, and **combine** the results into a new data structure.

*(See the split-apply-combine figure in answer 3.2; redraw it here in the exam.)*

### Steps

1. **Split**: divide the DataFrame into groups based on **one or more keys** (a column, several columns, a function or a dictionary). Rows with the same key go to the same group. → `g = df.groupby("product")`
2. **Apply**: apply a function **to each group independently**:
   - **Aggregate** (sum, mean, count) → `g["sales"].sum()`
   - **Transform** (normalise, fill NA with group mean) → `g["sales"].transform("mean")`
   - **Filter** (drop small groups) → `g.filter(lambda x: len(x) > 2)`
3. **Combine**: merge the per-group results into a single **Series or DataFrame**, indexed by group keys.

### Example

| product | sales |
|---|---|
| A | 10 |
| B | 5 |
| A | 20 |
| B | 15 |

Split → A: {10, 20}, B: {5, 15} → Apply sum → A = 30, B = 20 → Combine → `Series(A=30, B=20)`.

**Conclusion:** Split-apply-combine breaks a big problem into **small group-wise problems** and joins the answers, which is the basis of all group-level analysis.

> **Memory trick:** "**SAC**: like filling a **sack**: Split the grains, Apply sorting, Combine in the sack."

# Last-Minute Revision Sheet: Unit 3

| Topic | Key points to write |
|---|---|
| **Data aggregation** | Summarise rows into group statistics. Process: Collect → Process → Present. Functions: sum, mean, median, count, min, max, std. Single, multi-level, time-based. Uses: OLAP, warehouses, marketing, anonymisation. |
| **GroupBy** | Split-apply-combine. Keys = column/array/dict/function. Apply = aggregate, transform, filter (**ATF**). `df.groupby("k")["v"].sum()`, `.agg({...})`, multi-key → MultiIndex. |
| **Cross tabulation** | Contingency table of 2 categorical variables; counts/%; margins. `pd.crosstab(a, b, margins=True)`. E = row × col / N; χ² = Σ(O−E)²/E; df = (r−1)(c−1). Uses: surveys, HR, product research. |
| **Time series basics** | Data indexed by time. Trend, seasonality, cyclic, irregular; stationarity, autocorrelation, white noise. Y = T + S + C + I. Tools: to_datetime, date_range, shift, resample, tz_convert. Differences table vs regular data. |
| **Pivot tables** | Summary table: Rows, Columns, Values (aggfunc), Filters (**RCVF**). `pd.pivot_table(df, index, columns, values, aggfunc, margins=True)`. Excel: Insert → PivotTable. |
| **Periods** | Period = span, Timestamp = point. `pd.Period("2023-01","M") + 3 = 2023-04`; difference; `period_range`; `asfreq`; fiscal quarters `Q-MAR`. |
| **Moving window** | Fixed window slides over time. rolling mean/median/std/sum, SMA = Σx/n, EMA~t~ = αx~t~ + (1−α)EMA~t−1~, α = 2/(span+1). Big window smooth & laggy. Boundary NaN. |
| **Resampling** | Change frequency. Downsample (aggregate: sum/mean/ohlc) vs upsample (ffill/bfill/interpolate). `s.resample("M").sum()`. Smoothing, alignment, size reduction. |
| **Split-apply-combine** | Split by key → apply function per group → combine into new object. **SAC**. |

# Assumptions & Gaps

- Exam Unit 3 = question pair Q5/Q6 = syllabus Unit V "Data Aggregation and Analysis" (textbook Chapter 5, PDF p. 67-82).
- All citations are to `Textbooks/DMV Textbook.pdf` (scanned, OCR'd; **PDF page numbers**). There are no separate lecture notes in the repo.
- 2024 Q5b is printed as "cross tabulation **67** Time Series"; "67" is taken as a print error for "&". It is mapped to 3.4 (time series); for the cross-tabulation half, use 3.3.
- **Added from standard subject knowledge (not in the textbook):** the chi-square worked example and formulas in 3.3 (the textbook names "Chi-Square Statistic" and "Expected Values" only); the additive/multiplicative decomposition formula and the time-series vs regular-data comparison table in 3.4; SMA/EMA formulas, expanding windows and the window-size worked table in 3.7; pandas `asfreq`/fiscal-quarter examples in 3.6; OHLC and the downsampling/upsampling comparison table in 3.8.
- **Textbook point corrected:** PDF p. 80 says a monthly period can be "multiplied by 3" to give a quarterly period; pandas does not support multiplying a Period. The answer uses frequency conversion (`asfreq`) instead and notes this. The textbook's section on periods also drifts into trigonometric and financial "periods" (PDF p. 80-81); only the time-series meaning is used here, as that is what the exam asks.
- The pivot-table example (Banana/Apple exports) is from the textbook's Excel example (PDF p. 73-76); the small 5-row pivot diagram is a simplified illustration.
- No question in this unit was missing from the materials; no "⚠ Not found" flags were needed.
