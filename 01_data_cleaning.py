import pandas as pd
import numpy as np

raw_data = {
    'Employee_ID': [101,102,103,104,105,106,101,108,109,110,111,112,113,114,115],
    'Name': ['Alice Smith','Bob Jones','Charlie Brown','Diana Prince','Evan Wright','Fiona Gallagher','Alice Smith','George Clark','Hannah Abbott','Ian Malcolm','Julia Roberts','Kevin Bacon','Laura Croft','Mike Tyson','Nina Simone'],
    'Department': ['HR','Engineering','Marketing','Engineering','HR','Sales','HR','sales',np.nan,'Engineering','Marketing','Sales','HR','Engineering','Finance'],
    'Salary':[65000,85000,55000,95000,np.nan,60000,65000,62000,70000,105000,np.nan,58000,72000,88000,91000],
    'Join_Date': ['2021-03-15','2020-01-10','2022-06-01','2019-11-20','2023-02-01','2021-08-14','2021-03-15','2022-09-10','2021-11-05','2018-05-12','2022-07-19','2023-01-15','2020-05-22','2019-04-01','2021-10-30']
    }

df = pd.DataFrame(raw_data)

df.to_csv("data_raw/employee_salaries_raw.csv", index=False)

print("Success! The messy datasethas been saved to data_raw/employee_salaries_raw.csv")

import pandas as pd

file_path = "data_raw/employee_salaries_raw.csv"
df = pd.read_csv(file_path)

print("--- Data Shape ---")
print(df.shape)

print("\n--- First 5 Rows of Data ---")
print(df.head())

print("\n--- Summary Information ---")
df.info()

print("\n--- Count of Missing Values ---")
print(df.isnull().sum())

df['Department'] = df['Department'].fillna('Unknown')
median_salary = df['Salary'].median()
df['Salary'] = df['Salary'].fillna(median_salary)
print("\n---Missing Values After Cleaning ---")
print(df.isnull().sum())

clean_file_path = "data_clean/employee_salaries_clean.csv"
df.to_csv(clean_file_path, index=False)

print("\nSuccess! Cleaned dataset saved to data_clean Folder.")
