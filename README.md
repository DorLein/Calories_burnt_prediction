# Calories Burnt Prediction

## Overview

The **Calories Burnt Prediction** app, built with Streamlit, estimates calories burned based on user input using a pre-trained XGBoost model. It helps users track their fitness goals.

## Features

- **User Input:** Collects age, gender, height, weight, exercise duration, heart rate, and body temperature.
- **Model Prediction:** Provides calorie estimates using XGBoost.
- **Interactive Interface:** User-friendly design with Streamlit.

## How It Works

1. **Load Model:** Uses joblib to load the pre-trained XGBoost model.
2. **Preprocess Data:** Converts user input into a model-compatible format.
3. **Predict & Display:** Shows the estimated calories burnt.
