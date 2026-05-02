import streamlit as st
import requests

st.set_page_config(page_title="Salary Prediction App", page_icon="💼")

st.title("Salary Prediction App")
st.write("Enter candidate/job information to get predicted salary.")

experience_years = st.number_input("Experience years", min_value=0.0, value=2.0, step=1.0)
skills_count = st.number_input("Skills count", min_value=0.0, value=5.0, step=1.0)
certifications = st.number_input("Certifications", min_value=0.0, value=1.0, step=1.0)

job_title = st.text_input("Job title", value="Data Analyst")
education_level = st.text_input("Education level", value="Bachelor")
industry = st.text_input("Industry", value="IT")
company_size = st.text_input("Company size", value="Medium")
location = st.text_input("Location", value="Almaty")
remote_work = st.text_input("Remote work", value="Yes")

if st.button("Predict salary"):
    url = "http://127.0.0.1:8000/predict"

    payload = {
        "experience_years": experience_years,
        "skills_count": skills_count,
        "certifications": certifications,
        "job_title": job_title,
        "education_level": education_level,
        "industry": industry,
        "company_size": company_size,
        "location": location,
        "remote_work": remote_work
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        predicted_salary = result["predicted_salary"]
        st.success(f"Predicted salary: {predicted_salary:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")