🎬 Netflix Data Analysis using Pandas

📘 Project Overview
This project performs an Exploratory Data Analysis (EDA) on the Netflix dataset using Python and Pandas.  
The goal is to understand patterns in Netflix's catalog — such as the distribution of Movies vs TV Shows, popular genres, top countries, and content growth over the years.

---
 🧰 Tech Stack
- Language:** Python 3  
- Libraries:** pandas, matplotlib, pathlib  
- IDE: VS Code  
- Dataset Source: [Netflix Titles Dataset – Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

---

🗂️ Project Structure
netflix-pandas-project/
│
├── data/
│   ├── netflix_titles.csv 
│   └── netflix_clean.csv 
│
├── analysis.py
├── requirements.txt
└── README.md

---


🧮 Workflow

Phase 1 – Data Inspection**
- Load dataset using pandas  
- Display shape, column names, missing values, and data types  

Phase 2 – Data Cleaning**
- Fill missing text fields with `"Unknown"`  
- Convert `date_added` to datetime  
- Split `duration` into `duration_min` and `seasons`  
- Extract first `main_genre` and `main_country`  
- Save cleaned dataset  

Phase 3 – Exploratory Analysis**
- Count of Movies vs TV Shows  
- Top 10 Genres  
- Top 10 Countries  
- Titles added per Year (growth trend)  
- Average Movie Duration by Genre  
- Simple visualizations using matplotlib  

---

📊 Sample Outputs

1. Movies vs TV Shows
| Type | Count |
|------|-------|
| Movie | 6131 |
| TV Show | 2676 |

2. Titles Added per Year
Line chart showing Netflix catalog growth from 2010 → 2021.

3. Average Movie Duration by Genre
Bar chart of mean durations (minutes) for top genres.

---

🚀 How to Run
1. Clone the repository  
   ```bash
   git clone https://github.com/yourusername/netflix-pandas-project.git
   cd netflix-pandas-project