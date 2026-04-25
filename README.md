Project Steps
1.	Install libraries with pip install -r requirements.txt.
2.	Run train.py to train the model and save model.joblib.
3.	Start MLflow UI to see parameters, metrics, and the registered model.
4.	Run FastAPI with uvicorn main:app --reload.
5.	Run Streamlit with streamlit run app.py.
6.	Enter data in the frontend and get the predicted salary.
Input Features
The model uses these features: experience years, skills count, certifications, job title, education level, industry, company size, location, and remote work.
Result
The final result is a simple complete ML system. The user can enter data in the frontend, send it to the API, and receive a salary prediction.
