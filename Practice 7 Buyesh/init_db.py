import sqlite3

DB_NAME = "salary_predictions.db"

connection = sqlite3.connect(DB_NAME)
cursor = connection.cursor()

# Create table for input data
cursor.execute("""
CREATE TABLE IF NOT EXISTS input_data (
    id INTEGER PRIMARY KEY,
    experience_years REAL,
    skills_count REAL,
    certifications REAL,
    job_title TEXT,
    education_level TEXT,
    industry TEXT,
    company_size TEXT,
    location TEXT,
    remote_work TEXT
)
""")

# Create table for prediction results
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    input_id INTEGER UNIQUE,
    prediction REAL,
    prediction_timestamp TEXT
)
""")

# Insert sample rows
sample_data = [
    (
        1,
        3,
        5,
        2,
        "Data Analyst",
        "Bachelor",
        "IT",
        "Medium",
        "Almaty",
        "Yes"
    ),
    (
        2,
        5,
        8,
        3,
        "Machine Learning Engineer",
        "Master",
        "Technology",
        "Large",
        "Astana",
        "No"
    ),
    (
        3,
        1,
        3,
        0,
        "Junior Developer",
        "Bachelor",
        "IT",
        "Small",
        "Almaty",
        "Yes"
    )
]

cursor.executemany("""
INSERT OR IGNORE INTO input_data (
    id,
    experience_years,
    skills_count,
    certifications,
    job_title,
    education_level,
    industry,
    company_size,
    location,
    remote_work
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", sample_data)

connection.commit()
connection.close()

print("Database was created successfully.")
print("Sample input data was inserted.")