import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# ------------------------------
# Load Dataset
# ------------------------------
df = pd.read_csv("usa_rain_prediction_dataset_2024_2025.csv")

# Features & Target
X = df[["Humidity", "Temperature", "Wind Speed", "Pressure"]]
y = df["Rain Tomorrow"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train Naïve Bayes
model = GaussianNB()
model.fit(X_train, y_train)

# Evaluate Accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🌦️ Rainfall Prediction App")

st.write("Predict whether it will rain tomorrow based on weather conditions.")

st.subheader("🔧 Input Weather Features")

humidity = st.number_input("Humidity (%)", min_value=0, max_value=100, value=75)
temperature = st.number_input("Temperature (°C)", min_value=-10, max_value=100, value=28)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0, max_value=150, value=12)
pressure = st.number_input("Pressure (hPa)", min_value=950, max_value=1050, value=1010)

features = np.array([[humidity, temperature, wind_speed, pressure]])

if st.button("🌤️ Predict Rainfall"):
    prediction = model.predict(features)[0]
    if prediction == 0:
        st.info("☀️ No, it is unlikely to rain tomorrow.")
    else:
        st.success("🌧️ Yes, it is likely to rain tomorrow!")

# Show model accuracy
st.sidebar.header("📊 Model Performance")
st.sidebar.write(f"Model Accuracy: **{accuracy*100:.2f}%**")
