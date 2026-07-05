CREATE DATABASE HRAnalytics;
USE HRAnalytics;
USE HRAnalytics;

CREATE TABLE employees (
    employee_id   INT PRIMARY KEY,
    name          VARCHAR(100),
    age           INT,
    gender        VARCHAR(20),
    department    VARCHAR(50),
    role          VARCHAR(100),
    education     VARCHAR(50),
    hire_date     DATE,
    exit_date     DATE,
    tenure_years  DECIMAL(5,1),
    salary        DECIMAL(10,2),
    performance   VARCHAR(20),
    absences      INT,
    attrition     INT
);
USE HRAnalytics;
SELECT COUNT(*) AS total_employees FROM employees;
SELECT * FROM employees LIMIT 5;
USE hranalytics;

-- Attrition summary by department
CREATE VIEW vw_attrition_by_dept AS
SELECT
    department,
    COUNT(*) AS total_employees,
    SUM(attrition) AS total_attrition,
    ROUND(SUM(attrition) * 100.0 / COUNT(*), 2) AS attrition_rate
FROM employees
GROUP BY department;

-- Salary analysis
CREATE VIEW vw_salary_analysis AS
SELECT
    department,
    role,
    ROUND(AVG(salary), 2) AS avg_salary,
    MIN(salary) AS min_salary,
    MAX(salary) AS max_salary,
    COUNT(*) AS headcount
FROM employees
GROUP BY department, role;

-- Workforce profile
CREATE VIEW vw_workforce_profile AS
SELECT
    department,
    gender,
    education,
    ROUND(AVG(age), 1) AS avg_age,
    ROUND(AVG(tenure_years), 1) AS avg_tenure,
    COUNT(*) AS headcount
FROM employees
GROUP BY department, gender, education;

-- Performance distribution
CREATE VIEW vw_performance AS
SELECT
    department,
    performance,
    COUNT(*) AS employee_count,
    ROUND(AVG(salary), 2) AS avg_salary
FROM employees
GROUP BY department, performance;

-- Hiring trend
CREATE VIEW vw_hiring_trend AS
SELECT
    DATE_FORMAT(hire_date, '%Y-%m') AS hire_month,
    COUNT(*) AS new_hires
FROM employees
GROUP BY hire_month
ORDER BY hire_month;
SELECT * FROM vw_attrition_by_dept;
SELECT * FROM vw_salary_analysis LIMIT 5;
USE hranalytics;
CREATE VIEW vw_attrition_by_dept AS
SELECT department, COUNT(*) AS total_employees,
SUM(attrition) AS total_attrition,
ROUND(SUM(attrition) * 100.0 / COUNT(*), 2) AS attrition_rate
FROM employees GROUP BY department;
CREATE VIEW vw_salary_analysis AS
SELECT department, role,
ROUND(AVG(salary), 2) AS avg_salary,
MIN(salary) AS min_salary,
MAX(salary) AS max_salary,
COUNT(*) AS headcount
FROM employees GROUP BY department, role;
CREATE VIEW vw_performance AS
SELECT department, performance,
COUNT(*) AS employee_count,
ROUND(AVG(salary), 2) AS avg_salary
FROM employees GROUP BY department, performance;
SELECT * FROM vw_attrition_by_dept;