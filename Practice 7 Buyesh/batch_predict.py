import sqlite3
from datetime import datetime

import joblib
import pandas as pd


DB_NAME = "salary_predictions.db"
MODEL_PATH = "model.joblib"


FEATURE_COLUMNS = [
    "experience_years",
    "skills_count",
    "certifications",
    "job_title",
    "education_level",
    "industry",
    "company_size",
    "location",
    "remote_work"
]


def run_batch_prediction():
    print("Starting batch prediction...")

    # 1. Connect to database
    connection = sqlite3.connect(DB_NAME)

    # 2. Read input data that does not have predictions yet
    query = """
    SELECT 
        input_data.id,
        input_data.experience_years,
        input_data.skills_count,
        input_data.certifications,
        input_data.job_title,
        input_data.education_level,
        input_data.industry,
        input_data.company_size,
        input_data.location,
        input_data.remote_work
    FROM input_data
    LEFT JOIN predictions
        ON input_data.id = predictions.input_id
    WHERE predictions.input_id IS NULL
    """

    input_df = pd.read_sql_query(query, connection)

    if input_df.empty:
        print("No new input data for prediction.")
        connection.close()
        return

    print(f"Rows for prediction: {len(input_df)}")

    # 3. Load trained model
    model = joblib.load(MODEL_PATH)

    # 4. Prepare features
    input_ids = input_df["id"]
    X = input_df[FEATURE_COLUMNS]

    # 5. Generate predictions
    predictions = model.predict(X)

    # 6. Save predictions back to database
    prediction_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    result_df = pd.DataFrame({
        "input_id": input_ids,
        "prediction": predictions,
        "prediction_timestamp": prediction_time
    })

    result_df.to_sql(
        "predictions",
        connection,
        if_exists="append",
        index=False
    )

    connection.commit()
    connection.close()

    print("Batch prediction finished.")
    print(result_df)


if __name__ == "__main__":
    run_batch_prediction()