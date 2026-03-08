# Medical Insurance Cost Prediction

## Project Overview

This project predicts medical insurance charges using machine learning.
The dataset contains information about individuals such as age, BMI, smoking status, and region.
The goal is to build a regression model that can estimate insurance costs based on these features.

The model is trained using **Linear Regression** and compared with a **Decision Tree Regressor**.

---

## Dataset

Dataset used: **Medical Cost Personal Dataset**

Features in the dataset include:

* age
* sex
* bmi
* children
* smoker
* region
* charges (target variable)

Source: Kaggle

---

## Problem Statement

Insurance companies need to estimate medical costs for individuals based on their personal and health-related information.
This project predicts insurance charges using machine learning techniques.

---

## Feature Engineering

New features were created to improve prediction accuracy.

### BMI Category

BMI values are grouped into:

* Underweight
* Normal
* Overweight
* Obese

### Age Group

Age values are grouped into:

* Young
* Adult
* Senior

### Interaction Feature

An interaction feature was created between **smoker and BMI** to capture the combined effect on insurance charges.

---

## Outlier Detection

Outliers in the target variable **charges** were detected and removed using the **IQR (Interquartile Range) method**.

---

## Models Used

### Linear Regression

A simple regression model used to predict insurance charges.

### Decision Tree Regressor

A nonlinear model used to compare performance with linear regression.

---

## Model Evaluation

The models were evaluated using the following metrics:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

These metrics help measure prediction accuracy and model performance.

---

## Deployment

The trained model was deployed using **Streamlit**.
Users can input details such as age, BMI, number of children, and smoking status to predict insurance charges.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* VS Code
* GitHub

---

## Project Structure

```
insurance-cost-prediction
│
├── insurance.csv
├── task2.ipynb
├── insurance_model.pkl
├── app.py
├── requirements.txt
└── README.md
```

---

## How to Run the App

Install required libraries:

```
pip install -r requirements.txt
```

Run the Streamlit application:

```
streamlit run app.py
```

---

## Author

Tanvi Ganji
