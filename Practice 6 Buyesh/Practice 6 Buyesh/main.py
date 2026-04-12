from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# load model
model = joblib.load("model.joblib")

# input schema
class SalaryInput(BaseModel):
    experience_years: float
    skills_count: float
    certifications: float
    job_title: str
    education_level: str
    industry: str
    company_size: str
    location: str
    remote_work: str

@app.get("/")
def root():
    return {"message": "ML API is running"}

@app.post("/predict")
def predict(data: SalaryInput):
    input_df = pd.DataFrame([{
        "experience_years": data.experience_years,
        "skills_count": data.skills_count,
        "certifications": data.certifications,
        "job_title": data.job_title,
        "education_level": data.education_level,
        "industry": data.industry,
        "company_size": data.company_size,
        "location": data.location,
        "remote_work": data.remote_work
    }])

    prediction = model.predict(input_df)[0]

    return {"predicted_salary": float(prediction)}