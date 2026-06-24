# 📊 Employee Salary & Demographic Analysis

An end-to-end data analytics project focused on auditing, cleaning, and exploring synthetic employee demographic data. This project showcases a production-grade data cleansing pipeline using Python and Pandas to resolve intentional data anomalies embedded in a Google Capstone exercise.

## 🛠️ Tech Stack & Structure
* **Language:** Python 3.14
* **Libraries:** Pandas, NumPy, Matplotlib, Seaborn
* **Data Flow:** `data_raw/` (Messy source data) ➡️ `01_data_cleaning.py` ➡️ `data_clean/` (Validated destination)

## 🧩 Resolved Data Quality Challenges
The dataset contained several intentional data integrity anomalies designed to test rigorous extraction and transformation skills:
1. **Primary Key Duplication:** Resolved duplicate entries under `Employee_ID` (e.g., removing redundant logs for Alice Smith).
2. **Text Inconsistencies:** Standardized mixed-case text records across departments (e.g., merging 'sales' vs 'Sales').
3. **Data Type Corruption:** Transformed text-based `Join_Date` fields into true Datetime objects for temporal metrics.
4. **Missing Values:** Addressed structural null values within the `Salary` and `Department` fields dynamically.
5.
