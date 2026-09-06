
# Bangladesh Election 2026: Electoral, Demographic & Socioeconomic Data Analytics

##  Executive Summary
- **Total Constituencies:** 299
- **Total Registered Voters:** 127,062,426
- **Average Poverty Rate:** 19.2%
- **Average Literacy Rate:** 49.3%
- **Average Winning Margin:** 44,660

##  Key Findings

### 1. Electoral Analysis
- **Most Competitive Division:** Rangpur (avg margin: 34,266)
- **Least Competitive Division:** Sylhet (avg margin: 57,963)
- **Closest Contest:** Madaripur-1 (margin: 385.0 votes)
- **Largest Margin Victory:** Rangamati (margin: 170,322.0 votes)

### 2. Party Performance
- **Largest Party:** BNP (212 seats)
- **Party with Largest Average Margin:** GSA
- **Party with Smallest Average Margin:** IAB

### 3. Socioeconomic Insights
- **Correlation: Poverty vs Literacy:** 0.001
- **Correlation: Poverty vs Margin:** -0.013
- **Correlation: Literacy vs Margin:** -0.051

### 4. Demographic Patterns
- **Division with Highest Female Voter %:** Rangpur
- **Division with Lowest Female Voter %:** Chittagong
- **Average Female Voter %:** 49.4%
- **Average Male Voter %:** 51.0%
- **Gender Gap (National):** 1.5 percentage points

### 5. Competitiveness Categories
- **Very Close (<5% margin):** 51 constituencies
- **Close (5-15% margin):** 84 constituencies
- **Moderate (15-30% margin):** 97 constituencies
- **Large (30-50% margin):** 47 constituencies
- **Very Large (>50% margin):** 20 constituencies

### 6. Clustering Analysis
- **Optimal Number of Clusters:** 4
- **Cluster Characteristics:** See cluster_summary.csv for details

### 7. Referendum Results
- **Yes Votes:** 47,225,980 (68.3%)
- **No Votes:** 21,960,231 (31.7%)
- **Valid Votes:** 69,186,211 (90.3%)
- **Invalid/Blank Votes:** 7,435,196 (9.7%)

##  Data Quality Report
- **Total Records:** 300
- **Missing Values:** 14
- **Data Quality Issues:** 1 issues identified

##  Technology Stack
- **Data Processing:** Python, Pandas, NumPy, PySpark
- **Analysis:** Pandas, Scikit-learn, Statistical Analysis
- **Visualization:** Matplotlib, Seaborn, Plotly, Folium
- **Environment:** Google Colab

##  Limitations
1. **Dataset Size:** 300 constituency-level records - not big data
2. **Candidate Coverage:** Only winner and runner-up votes available
3. **Turnout:** Cannot calculate true voter turnout from available data
4. **Socioeconomic Variables:** May come from different reference periods
5. **Correlation vs Causation:** Observed relationships do not imply causation

---

*Report generated on: 2026-09-06 08:08:29*
