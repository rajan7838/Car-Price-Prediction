Car Price Prediction (Machine Learning)

This project predicts the selling price of used cars using machine learning regression models.
It covers the complete ML pipeline from data preprocessing to model deployment using Streamlit.

“I built an end-to-end car price prediction project using supervised machine learning.
I cleaned the dataset, removed unnecessary columns, and handled categorical variables using One-Hot Encoding.
Numerical features were scaled with StandardScaler and combined using a ColumnTransformer.
I trained Polynomial Regression and Support Vector Regression models and tuned their hyperparameters using GridSearchCV with R² as the evaluation metric.
The best performing model was saved using joblib and deployed using a Streamlit web application, where users can input car details and get the predicted selling price.”

🔍 Problem Statement

Estimate the car selling price based on features like brand, model, vehicle age, mileage, engine, fuel type, transmission, and seats.

🧠 Models Used

Linear Regression

Polynomial Regression

Ridge Regression

Support Vector Regression (SVR)

Random Forest Regressor

Best model selected using:

R² Score

RMSE

Hyperparameter tuning is done with GridSearchCV.

⚙️ Data Preprocessing

Missing values removed

Categorical features encoded using OneHotEncoder

Numerical features scaled using StandardScaler

Combined using ColumnTransformer

🧪 Features

Input:
brand, model, vehicle_age, km_driven, seller_type, fuel_type, transmission_type, mileage, engine, max_power, seats

Target:
selling_price

Tech Stack

Python

Pandas, NumPy

Scikit-learn

Streamlit

Joblib

ech Stack

Python

Pandas, NumPy

Scikit-learn

Streamlit

Joblib
