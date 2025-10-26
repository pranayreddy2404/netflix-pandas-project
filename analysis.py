import pandas as pd
from pathlib import Path
BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "netflix_titles.csv"
df = pd.read_csv(DATA)
print ("Loaded.")
print ("Shape:", df.shape)
print ("\n---Column Names---")
print (df.columns)
print("\n--- First 5 Rows ---")
print(df.head())
print("\n--- Data Types and Non-Null Counts ---")
print(df.info())
print("\n--- Missing Values per Column ---")
print(df.isna().sum())
print("\n--- Basic Statistics for Numeric Columns ---")
print(df.describe())

# --- Phase 2: Cleaning & Preprocessing ---

# 1. Fill or drop missing values
text_columns = ["director", "cast", "country", "rating"]
for col in text_columns:
    df[col] = df[col].fillna("Unknown")
df = df.dropna(subset=["title", "type"])


df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")
df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month


df["duration_min"] = df["duration"].str.extract(r"(\d+)").astype(float)
df["seasons"] = df["duration"].apply(
    lambda x: float(x.split()[0]) if "Season" in str(x) else None
)


df["main_genre"] = df["listed_in"].str.split(",").str[0].str.strip()
df["main_country"] = df["country"].str.split(",").str[0].str.strip()

clean_path = BASE / "data" / "netflix_clean.csv"
df.to_csv(clean_path, index=False)
print("Cleaned data saved to:", clean_path)


df = pd.read_csv(BASE / "data" / "netflix_clean.csv")
print("=== Cleaned data loaded ===")
print(df.head())
type_counts = df["type"].value_counts()
print("\n--- Movies vs TV Shows ---")
print(type_counts)
top_genres = df["main_genre"].value_counts().head(10)
print("\n--- Top 10 Genres ---")
print(top_genres)
top_countries = df["main_country"].value_counts().head(10)
print("\n--- Top 10 Countries ---")
print(top_countries)
added_by_year = df["year_added"].value_counts().sort_index()
print("\n--- Titles Added Per Year ---")
print(added_by_year)
avg_durations = (
    df[df["type"] == "Movie"]
    .groupby("main_genre")["duration_min"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
print("\n--- Average Movie Duration by Genre ---")
print(avg_durations)
import matplotlib.pyplot as plt


type_counts.plot(kind="bar", title="Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.show()

added_by_year.plot(kind="line", title="Netflix Titles Added per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.show()