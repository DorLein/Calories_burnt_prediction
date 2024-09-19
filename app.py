import streamlit as st
import pandas as pd
import joblib

# Function to load data and model
def load_model():
    # Load the model
    model = joblib.load('xgboost_model.joblib')
    return model

# Function to preprocess input data
def preprocess_data(age, gender, height, weight, duration, heart_rate, body_temp):
    # Convert gender to numeric
    gender = 0 if gender == 'Male' else 1
    
    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        'Gender': [gender],
        'Age': [age],
        'Height': [height],
        'Weight': [weight],
        'Duration': [duration],
        'Heart_Rate': [heart_rate],
        'Body_Temp': [body_temp]
    })

    # Ensure the columns are in the same order as the model expects
    input_data = input_data[['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp']]
    
    return input_data

# Load model
model = load_model()

# Streamlit interface
st.title('Calories Burnt Prediction')

age = st.number_input('Age', min_value=0, max_value=100, value=25)
gender = st.selectbox('Gender', ['Male', 'Female'])
height = st.number_input('Height (cm)', min_value=0, max_value=250, value=170)
weight = st.number_input('Weight (kg)', min_value=0, max_value=200, value=70)
duration = st.number_input('Duration (minutes)', min_value=0, max_value=500, value=30)
heart_rate = st.number_input('Heart Rate (bpm)', min_value=30, max_value=200, value=100)
body_temp = st.number_input('Body Temperature (°C)', min_value=30.0, max_value=45.0, value=36.5)

if st.button('Predict'):
    input_data = preprocess_data(age, gender, height, weight, duration, heart_rate, body_temp)
    prediction = model.predict(input_data)
    st.write(f'Estimated Calories Burnt: {prediction[0]:.2f} kcal')
