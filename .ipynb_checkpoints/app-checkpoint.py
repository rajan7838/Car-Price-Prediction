import streamlit as st
import pandas as pd
import joblib

# ================= LOAD MODEL =================
model = joblib.load("model.pkl")

st.title("🚗 Car Price Prediction")

st.write("Enter realistic car details to get accurate price prediction")

# ================= USER INPUT =================
brand = st.selectbox(
    "Brand",
    ["maruti", "hyundai", "honda", "toyota", "tata", "mahindra", "ford"]
)

model_name = st.text_input("Model (e.g., swift, city, i20)")

vehicle_age = st.number_input(
    "Vehicle Age (years)", min_value=0, max_value=30, value=5
)

km_driven = st.number_input(
    "KM Driven", min_value=500, value=40000
)

seller_type = st.selectbox(
    "Seller Type", ["Dealer", "Individual", "Trustmark Dealer"]
)

fuel_type = st.selectbox(
    "Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
)

transmission = st.selectbox(
    "Transmission", ["Manual", "Automatic"]
)

mileage = st.number_input(
    "Mileage (km/l)", min_value=5.0, value=18.0
)

engine = st.number_input(
    "Engine (cc)", min_value=800, value=1200
)

max_power = st.number_input(
    "Max Power (bhp)", min_value=40.0, value=80.0
)

seats = st.number_input(
    "Seats", min_value=2, max_value=10, value=5
)

# ================= PREDICTION =================
if st.button("Predict Price"):
    input_df = pd.DataFrame({
        "brand": [brand],
        "model": [model_name],
        "vehicle_age": [vehicle_age],
        "km_driven": [km_driven],
        "seller_type": [seller_type],
        "fuel_type": [fuel_type],
        "transmission_type": [transmission],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats]
    })

    price = model.predict(input_df)[0]

    st.success(f"Estimated Price: ₹ {price:,.0f}")