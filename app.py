import streamlit as st

st.set_page_config(page_title="Heart Disease Prediction", layout="centered")

st.title("Heart Disease Prediction App")
st.write("""
Welcome to the Heart Disease Prediction App!  
Fill in your details below to check your risk.
""")

# Example input fields
age = st.number_input("Age", min_value=1, max_value=120)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200)
chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["True", "False"])
restecg = st.selectbox("Resting ECG Results", ["Normal", "Having ST-T wave abnormality", "Showing probable or definite left ventricular hypertrophy"])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220)
exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])

if st.button("Predict"):
    # Placeholder for prediction logic
    st.success("Prediction: true")

st.sidebar.header("About")
st.sidebar.info("This app predicts the likelihood of heart disease based on user input. Add your ML model for real predictions.")
