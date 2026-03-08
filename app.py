import streamlit as st
import pickle
import pandas as pd

# Load trained model
model = pickle.load(open("insurance_model.pkl", "rb"))

st.title("Insurance Cost Prediction App")

st.write("Enter details to estimate medical insurance cost")

# User Inputs
age = st.number_input("Age", 18, 100)
bmi = st.number_input("BMI", 10.0, 60.0)
children = st.number_input("Children", 0, 10)

sex = st.selectbox("Sex", ["female", "male"])
smoker = st.selectbox("Smoker", ["no", "yes"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# -------- Feature Engineering -------- #

# sex
sex_male = 1 if sex == "male" else 0

# smoker
smoker_yes = 1 if smoker == "yes" else 0

# smoker_bmi
smoker_bmi = bmi * smoker_yes

# region encoding
region_northwest = 1 if region == "northwest" else 0
region_southeast = 1 if region == "southeast" else 0
region_southwest = 1 if region == "southwest" else 0

# BMI category
BMI_Category_Obese = 1 if bmi >= 30 else 0
BMI_Category_Overweight = 1 if 25 <= bmi < 30 else 0
BMI_Category_Underweight = 1 if bmi < 18.5 else 0

# Age group
Age_Group_Senior = 1 if age >= 50 else 0
Age_Group_Young = 1 if age < 30 else 0

# -------- Prediction -------- #

if st.button("Predict Insurance Cost"):

    input_data = pd.DataFrame([{
        'age': age,
        'bmi': bmi,
        'children': children,
        'smoker_bmi': smoker_bmi,
        'sex_male': sex_male,
        'smoker_yes': smoker_yes,
        'region_northwest': region_northwest,
        'region_southeast': region_southeast,
        'region_southwest': region_southwest,
        'BMI_Category_Obese': BMI_Category_Obese,
        'BMI_Category_Overweight': BMI_Category_Overweight,
        'BMI_Category_Underweight': BMI_Category_Underweight,
        'Age_Group_Senior': Age_Group_Senior,
        'Age_Group_Young': Age_Group_Young
    }])

    prediction = model.predict(input_data)

    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")