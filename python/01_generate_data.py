import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()
np.random.seed(42)
random.seed(42)

# --- Config ---
NUM_EMPLOYEES = 1000

departments = ['Engineering', 'Sales', 'HR', 'Finance', 'Marketing', 'Operations']
roles = {
    'Engineering': ['Junior Developer', 'Senior Developer', 'Tech Lead', 'Engineering Manager'],
    'Sales':       ['Sales Rep', 'Senior Sales Rep', 'Sales Manager', 'VP Sales'],
    'HR':          ['HR Associate', 'HR Specialist', 'HR Manager', 'HR Director'],
    'Finance':     ['Analyst', 'Senior Analyst', 'Finance Manager', 'CFO'],
    'Marketing':   ['Marketing Associate', 'Content Specialist', 'Marketing Manager', 'CMO'],
    'Operations':  ['Operations Associate', 'Operations Specialist', 'Ops Manager', 'COO'],
}
salary_ranges = {
    'Engineering': (60000, 150000),
    'Sales':       (45000, 120000),
    'HR':          (40000, 90000),
    'Finance':     (55000, 130000),
    'Marketing':   (42000, 100000),
    'Operations':  (38000, 95000),
}
education_levels = ['High School', 'Bachelor', 'Master', 'PhD']
performance_ratings = ['Poor', 'Average', 'Good', 'Excellent']

# --- Generate data ---
records = []
for emp_id in range(1001, 1001 + NUM_EMPLOYEES):
    dept = random.choice(departments)
    role = random.choice(roles[dept])
    gender = random.choice(['Male', 'Female', 'Non-binary'])
    age = random.randint(22, 60)
    hire_date = fake.date_between(start_date='-10y', end_date='today')
    tenure_years = round((datetime.today().date() - hire_date).days / 365, 1)

    # Attrition: higher chance if low salary, young, short tenure
    base_attrition = 0.15
    attrition = random.random() < base_attrition + (0.1 if tenure_years < 1 else 0)
    exit_date = None
    if attrition:
        exit_date = hire_date + timedelta(days=random.randint(90, int(tenure_years * 365) + 90))
        if exit_date > datetime.today().date():
            exit_date = datetime.today().date()

    sal_min, sal_max = salary_ranges[dept]
    salary = round(random.uniform(sal_min, sal_max), 2)
    performance = random.choices(
        performance_ratings, weights=[0.1, 0.3, 0.4, 0.2])[0]
    absences = random.randint(0, 30)
    education = random.choices(
        education_levels, weights=[0.1, 0.5, 0.3, 0.1])[0]

    records.append({
        'employee_id':    emp_id,
        'name':           fake.name(),
        'age':            age,
        'gender':         gender,
        'department':     dept,
        'role':           role,
        'education':      education,
        'hire_date':      hire_date,
        'exit_date':      exit_date,
        'tenure_years':   tenure_years,
        'salary':         salary,
        'performance':    performance,
        'absences':       absences,
        'attrition':      1 if attrition else 0,
    })

df = pd.DataFrame(records)

# --- Save ---
df.to_csv('../data/raw/hr_raw.csv', index=False)
print(f"Dataset created: {len(df)} rows")
print(df.head())
print("Attrition rate:", round(df['attrition'].mean() * 100, 2), "%")