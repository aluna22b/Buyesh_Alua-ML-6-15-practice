1. Batch prediction pipeline

In addition to the FastAPI API, I added a batch prediction pipeline.

The batch prediction pipeline simulates a real-world machine learning system.

It does the following:

1. Reads input data from a database
2. Loads the trained model from model.joblib
3. Generates predictions
4. Saves prediction results back into the database
5. Runs automatically on a schedule


2. Database

The project uses SQLite as a simple database.

The database file is:

salary_predictions.db

SQLite is a simple database stored as one file.

The database has two tables:

input_data

This table stores the input data for prediction.

Columns:

- id
- experience_years
- skills_count
- certifications
- job_title
- education_level
- industry
- company_size
- location
- remote_work

predictions

This table stores the prediction results.

Columns:

- id
- input_id
- prediction
- prediction_timestamp

The column prediction_timestamp shows when the prediction was created.


3. init_db.py

The file init_db.py creates the SQLite database.

It creates two tables:

1. input_data
2. predictions

It also inserts sample input rows for testing.

To run it:

python init_db.py


4. batch_predict.py

The file batch_predict.py runs the batch prediction process.

It does the following:

1. Connects to the SQLite database
2. Reads new rows from input_data
3. Loads the trained model from model.joblib
4. Generates salary predictions
5. Saves the results into the predictions table

To run it manually:

python batch_predict.py


5. scheduler.py

The file scheduler.py runs the batch prediction automatically.

It uses the schedule library.

The script runs the prediction every 5 minutes.

5 minutes = 300 seconds

To start the scheduler:

python scheduler.py

The program will continue running and will repeat the batch prediction process every 5 minutes.


6. Final project structure

The final project contains:

- job_salary_prediction_dataset.csv
- train.py
- main.py
- model.joblib
- model_features.joblib
- requirements.txt
- Dockerfile
- README.md
- init_db.py
- batch_predict.py
- scheduler.py
- salary_predictions.db


7. How to run the full project

Step 1. Install dependencies

pip install -r requirements.txt

Step 2. Train the model

python train.py

Step 3. Run the FastAPI app locally

uvicorn main:app --reload

Step 4. Open Swagger documentation

http://127.0.0.1:8000/docs

Step 5. Create the database

python init_db.py

Step 6. Run batch prediction manually

python batch_predict.py

Step 7. Run automatic scheduler

python scheduler.py

Step 8. Build Docker image

docker build -t salary-prediction-api .

Step 9. Run Docker container

docker run -p 8000:8000 salary-prediction-api


8. Result

In this project, I trained a machine learning model for salary prediction.

Then I deployed the model using FastAPI.

After that, I containerized the API with Docker.

Finally, I created a batch prediction pipeline that reads data from a database, generates predictions, saves the results, and runs automatically every 5 minutes.

This project shows how a machine learning model can be used in a real application.