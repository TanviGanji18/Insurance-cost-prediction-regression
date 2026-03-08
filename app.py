import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("insurance_model.pkl", "rb"))

st.title("Medical Insurance Cost Prediction")

st.write("Enter details below to estimate insurance charges")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)

children = st.number_input("Number of Children", min_value=0, max_value=10)

sex = st.selectbox("Sex", ["Male", "Female"])

smoker = st.selectbox("Smoker", ["Yes", "No"])

region = st.selectbox("Region", ["Northeast", "Northwest", "Southeast", "Southwest"])


# Convert categorical inputs to numeric
sex_male = 1 if sex == "Male" else 0
smoker_yes = 1 if smoker == "Yes" else 0

region_northwest = 1 if region == "Northwest" else 0
region_southeast = 1 if region == "Southeast" else 0
region_southwest = 1 if region == "Southwest" else 0


# Predict button
if st.button("Predict Insurance Cost"):

    input_data = np.array([[age, bmi, children, sex_male, smoker_yes,
                            region_northwest, region_southeast, region_southwest]])

    prediction = model.predict(input_data)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:.2f}")