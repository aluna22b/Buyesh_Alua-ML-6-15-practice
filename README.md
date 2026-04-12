Project: Deploy ML Model with FastAPI and Docker

1. Prepare the dataset
First, I used the file job_salary_prediction_dataset.csv.
This file contains the data for salary prediction.

2. Train the machine learning model
I created the train.py file.
In this file, I loaded the dataset, selected the input features, selected the target column, and trained the model.
After training, I saved the model as model.joblib.
This file is important because the API will use it later.

3. Create the FastAPI application
Next, I created the main.py file.
This file contains the FastAPI app.
I added two endpoints:
- GET / -> checks that the API is running
- POST /predict -> sends input data to the model and returns the prediction

4. Run the API locally
After that, I started the FastAPI server with Uvicorn.
Then I tested:
- the root endpoint
- the prediction endpoint
- the Swagger documentation page at /docs

5. Create requirements.txt
I created the requirements.txt file.
This file contains all Python libraries needed for the project.
It helps install the same dependencies again later.

6. Create the Dockerfile
Then I created the Dockerfile.
This file describes how to run the project inside a Docker container.
It:
- uses a Python base image
- creates a working directory
- copies project files
- installs dependencies
- starts the FastAPI server

7. Build the Docker image
Next, I built the Docker image.
This image includes the code, libraries, and runtime environment.
It makes the project portable and reusable.

8. Run the Docker container
After building the image, I ran the container.
I exposed the application port and tested the API again.
This showed that the project works not only locally, but also inside Docker.

9. Final project structure
The final project contains:
- train.py
- main.py
- model.joblib
- model_features.joblib
- requirements.txt
- Dockerfile
- README.md

10. Result
In this work, I trained a machine learning model, deployed it with FastAPI, and containerized it with Docker.
The API can accept input data and return salary predictions.