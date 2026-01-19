Car Price Prediction (Machine Learning)

This project predicts the selling price of used cars using supervised machine learning regression models.
It implements the complete ML pipeline from data preprocessing and feature engineering to model training, hyperparameter tuning, and deployment using Streamlit.

📌 Project Overview (30-Second Explanation)

I built an end-to-end car price prediction project using supervised machine learning.
I cleaned the dataset, removed unnecessary columns, and handled categorical variables using One-Hot Encoding. Numerical features were scaled using StandardScaler and combined with categorical features using a ColumnTransformer.
I trained Linear Regression, Ridge Regression, and Support Vector Regression (SVR) models and optimized their hyperparameters using GridSearchCV with R² score as the evaluation metric.
The best-performing model was saved using joblib and deployed using a Streamlit web application, where users can input car details and get the predicted selling price.

🔍 Problem Statement

Predict the selling price of a used car based on vehicle specifications and seller-related features.

🧠 Models Used

Linear Regression

Ridge Regression

Support Vector Regression (SVR)

📊 Model Selection Criteria

R² Score

RMSE (Root Mean Squared Error)

Hyperparameter tuning was performed using GridSearchCV.

⚙️ Data Preprocessing

Removed missing and unnecessary columns

Categorical features encoded using OneHotEncoder

Numerical features scaled using StandardScaler

Preprocessing pipeline created using ColumnTransformer

🧪 Features

Input Features

brand

model

vehicle_age

km_driven

seller_type

fuel_type

transmission_type

mileage

engine

max_power

seats

Target Variable

selling_price

🛠️ Tech Stack->Python,Pandas, NumPy,Scikit-learn,Streamlit

Joblib
How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/rajan7838/Car-Price-Prediction
cd Car-Price-Prediction

2️⃣ (Optional) Create a Virtual Environment
python -m venv venv
source venv/bin/activate    # Linux / Mac
venv\Scripts\activate       # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Streamlit App
streamlit run app.py

