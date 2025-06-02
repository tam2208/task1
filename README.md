# task1
### 🎯 Objective:
Clean and prepare a raw dataset (with nulls, duplicates, inconsistent formats) for analysis.

---

## 🗂 Dataset Used:
**Netflix Movies and TV Shows** (`netflix_titles.csv` from Kaggle)

---

## ✅ Steps Performed:

1. **Column Name Cleaning:**
   - Converted all column headers to lowercase and replaced spaces with underscores.

2. **Missing Value Treatment:**
   - Filled missing values in `director`, `cast`, and `country` with `"Unknown"`.
   - Dropped rows missing critical fields: `date_added`, `rating`, `duration`.

3. **Duplicate Removal:**
   - Removed all duplicate records from the dataset.

4. **Date Format Standardization:**
   - Converted `date_added` to `datetime` format (`yyyy-mm-dd`).

5. **Data Type Corrections:**
   - Ensured `release_year` is of type `int`.

---

## 🧼 Cleaned Dataset Summary:

- **Rows:** 8,790  
- **Columns:** 12  
- **File:** [`netflix_titles_cleaned_final.csv`](netflix_titles_cleaned_final.csv)

---

## 💡 Interview Q&A Preparation

### 1. What are missing values and how do you handle them?
Missing values are empty cells in a dataset. We can handle them by:
- Filling with a default or inferred value (e.g., `"Unknown"`)
- Dropping rows with critical missing data

### 2. How do you treat duplicate records?
We identify and remove them using `.drop_duplicates()` in Pandas.

### 3. Difference between dropna() and fillna() in Pandas?
- `dropna()` removes rows/columns with missing values.
- `fillna()` fills missing values with a specified value.

### 4. What is outlier treatment and why is it important?
Outlier treatment involves identifying and managing extreme values that may skew analysis. It helps ensure reliable statistical insights.

### 5. Explain the process of standardizing data.
Standardizing involves transforming values to a consistent format, e.g., dates, text casing, numeric scaling.

### 6. How do you handle inconsistent data formats?
We convert fields like dates to consistent `datetime` format using `pd.to_datetime()`.

### 7. What are common data cleaning challenges?
- Handling missing/inconsistent values
- Formatting dates
- Ensuring correct data types
- Dealing with duplicates and typos

### 8. How can you check data quality?
By checking:
- Null values (`.isnull()`)
- Duplicate entries
- Unexpected data types
- Logical consistency (e.g., invalid dates)

---

## 📝 Submission Notes:
- All preprocessing was done using Python (Pandas).
- The cleaned dataset and this README are part of the GitHub submission.


