# HR Analytics Dashboard | SQL + Python + Excel + Power BI

![SQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)
![Power BI](https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## Overview

An end-to-end HR analytics project analyzing employee attrition, workforce diversity, salary distribution, hiring trends, and department performance using SQL, Python, Excel, and Power BI. The interactive dashboard helps HR teams make data-driven decisions to reduce attrition and optimize workforce planning.

---

## Dashboard Preview

### Page 1 — HR Overview
> KPI cards, attrition by department, headcount donut chart, monthly hiring trend, and interactive slicers

![HR Overview](https://raw.githubusercontent.com/samruddhi-mahale/HR-Analytics-Dashboard/main/images/powerbi_dashboard_1.png)

### Page 2 — Attrition Detail
> Attrition by gender, education, age group, and employee detail table with drill-through from Page 1

![Attrition Detail](https://raw.githubusercontent.com/samruddhi-mahale/HR-Analytics-Dashboard/main/images/powerbi_dashboard_2.png)

### Page 3 — Salary Analysis
> Average salary by department, performance, education, and salary vs age scatter plot

![Salary Analysis](https://raw.githubusercontent.com/samruddhi-mahale/HR-Analytics-Dashboard/main/images/powerbi_dashboard_3.png)

---

## Key Findings

| Finding | Detail |
|---------|--------|
| Overall Attrition Rate | **16.4%** |
| Total Employees Analysed | **1,000** |
| Average Salary | **$80,260** |
| Highest Attrition Department | **Sales** |
| Attrition Pattern | Employees with low tenure leave more frequently |
| Salary Distribution | Most employees fall in the medium salary band |
| Departments Covered | **6** (Engineering, Sales, HR, Finance, Marketing, Operations) |
| Gender Groups | Male, Female, Non-binary |

---

## KPIs Tracked

| KPI | Description |
|-----|-------------|
| Total Employees | Overall headcount |
| Attrition Rate | Overall and by department (16.4%) |
| Avg Salary | $80.26K overall |
| Avg Tenure | By department |
| Attrition by Gender | Count and rate per gender group |
| Attrition by Education | High School, Bachelor, Master, PhD |
| Attrition by Age Group | Which age bands leave most |
| Avg Salary by Department | Salary comparison across teams |
| Avg Salary by Performance | Poor / Average / Good / Excellent |
| Avg Salary by Education | Education level vs pay |
| Salary vs Age | Scatter by performance rating |
| Monthly Hiring Trend | New hires per month Jan–Oct |

---

## Dashboard Features

- **HR Overview page** — top-level KPIs with attrition, headcount, and hiring trend
- **Attrition Detail page** — drill-through from department bar chart showing gender, education, age breakdown
- **Salary Analysis page** — multi-dimensional salary comparison with scatter plot
- **Interactive slicers** — filter by department, gender, performance, education across all pages
- **Drill-through** — right-click any department on Page 1 to drill into Attrition Detail

---

## Project Structure

```
HRAnalyticsDashboard/
├── data/
│   ├── raw/
│   │   └── hr_raw.csv                  ← 1000-row generated employee dataset
│   └── processed/
│       └── hr_clean.csv
├── sql/
│   ├── 01_create_tables.sql            ← table definitions
│   ├── 02_load_data.sql                ← data loading scripts
│   ├── 03_create_views.sql             ← cleaned views for reporting
│   └── 04_hr_kpi_queries.sql           ← KPI extraction queries
├── python/
│   ├── 01_generate_data.py             ← dataset generation script
│   └── 02_eda.ipynb                    ← exploratory data analysis notebook
├── excel/
│   └── HR_KPI_Reference.xlsx           ← KPI model with 5 sheets
├── powerbi/
│   └── HRDashboard.pbix                ← Power BI dashboard file
├── exports/
│   ├── powerbi_dashboard_1.png         ← HR Overview screenshot
│   ├── powerbi_dashboard_2.png         ← Attrition Detail screenshot
│   ├── powerbi_dashboard_3.png         ← Salary Analysis screenshot
│   ├── HRDashboard_Report.pdf
│   └── eda_charts/
│       ├── 01_attrition_by_dept.png
│       ├── 02_salary_by_dept.png
│       ├── 03_attrition_by_gender.png
│       ├── 04_attrition_by_tenure.png
│       ├── 05_correlation_heatmap.png
│       └── 06_salary_by_performance.png
└── README.md
```

---

## Dataset

- **1,000 employee records** generated using Python (Faker library)
- **14 columns** covering all key HR attributes

| Column | Description |
|--------|-------------|
| employee_id | Unique employee identifier |
| name | Employee full name |
| age | Employee age (22–60) |
| gender | Male / Female / Non-binary |
| department | Engineering, Sales, HR, Finance, Marketing, Operations |
| role | Job title within department |
| education | High School / Bachelor / Master / PhD |
| hire_date | Date of joining |
| exit_date | Date of leaving (null if still employed) |
| tenure_years | Years at company |
| salary | Annual salary |
| performance | Poor / Average / Good / Excellent |
| absences | Number of absence days |
| attrition | 1 = left, 0 = still employed |

---

## SQL Views Created

```sql
-- Attrition rate by department
CREATE VIEW vw_attrition_by_dept AS
SELECT
    department,
    COUNT(*) AS total_employees,
    SUM(attrition) AS total_attrition,
    ROUND(SUM(attrition) * 100.0 / COUNT(*), 2) AS attrition_rate
FROM employees
GROUP BY department;
```

Additional views: `vw_salary_analysis`, `vw_workforce_profile`,
`vw_performance`, `vw_hiring_trend`

---

## Python EDA Charts

Generated using pandas, matplotlib, and seaborn:

| Chart | Insight |
|-------|---------|
| Attrition by Department | Sales has highest turnover |
| Salary Distribution by Dept | Boxplot showing salary spread |
| Attrition by Gender | Gender-wise attrition count and rate |
| Attrition by Tenure Group | Short-tenure employees leave more |
| Correlation Heatmap | Relationship between age, salary, tenure, attrition |
| Salary by Performance | How performance links to pay |

---

## Tools Used

| Tool | Purpose |
|------|---------|
| MySQL Workbench | Data storage, transformation, views |
| Python (pandas, seaborn) | Data generation and EDA |
| Jupyter Notebook | Interactive EDA environment |
| Excel | KPI reference model and PivotTables |
| Power BI Desktop | Interactive dashboard |
| DAX | Custom measures and calculations |
| Git / GitHub | Version control |

---

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/samruddhi-mahale/HR-Analytics.git
cd HR-Analytics
```

2. Generate the dataset:
```bash
cd python
python 01_generate_data.py
```

3. Run SQL scripts in MySQL Workbench in order:
```
01_create_tables.sql → 02_load_data.sql → 03_create_views.sql → 04_hr_kpi_queries.sql
```

4. Run EDA notebook:
```bash
jupyter notebook 02_eda.ipynb
```

5. Open `powerbi/HRDashboard.pbix` in Power BI Desktop and click **Refresh**

---

## Conclusion

This project demonstrates end-to-end data analytics using SQL, Python, Excel, and Power BI to generate meaningful HR insights. The dashboard enables HR teams to identify attrition risks, analyse salary equity, and track workforce trends — supporting faster, evidence-based people decisions.

---

## Author

**Samruddhi Mahale**  
Data Analyst  
[GitHub](https://github.com/samruddhi-mahale) | [LinkedIn](https://linkedin.com/in/samruddhi-mahale)

---
*Project completed: July 2026*
