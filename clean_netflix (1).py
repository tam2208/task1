
import pandas as pd

# Load the raw Netflix dataset
df = pd.read_csv("netflix_titles.csv")

# Step 1: Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 2: Handle missing values
df['director'].fillna('Unknown', inplace=True)
df['cast'].fillna('Unknown', inplace=True)
df['country'].fillna('Unknown', inplace=True)

# Drop rows with missing critical fields
df.dropna(subset=['date_added', 'rating', 'duration'], inplace=True)

# Step 3: Remove duplicates
df.drop_duplicates(inplace=True)

# Step 4: Convert date_added to datetime
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

# Step 5: Ensure correct data types
df['release_year'] = df['release_year'].astype(int)

# Save the cleaned dataset
df.to_csv("netflix_titles_cleaned_final.csv", index=False)
print("✅ Cleaned dataset saved as 'netflix_titles_cleaned_final.csv'")
