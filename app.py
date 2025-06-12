import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Apply custom styles to the dashboard
st.markdown("""
    <style>
        .header {
            font-size: 35px;
            color: #009639;  /* UAE Green */
            font-weight: bold;
            text-align: center;
        }
        .subheader {
            font-size: 24px;
            color: #C8102E;  /* UAE Red */
            font-weight: bold;
        }
        .tables-container {
            display: flex;
            justify-content: space-between;
            gap: 20px;  /* Space between tables */
        }
        .table-box {
            width: 32%;  /* Ensuring equal width for all tables */
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .table-box table {
            width: 100%;
            border-collapse: collapse;
        }
        .table-box th {
            background-color: #C8102E; /* UAE Red */
            color: white;
            padding: 12px;
            text-align: center;
        }
        .table-box td {
            text-align: center;
            padding: 10px;
            background-color: #ffffff;
        }
        .prediction-box {
            background-color: #009639; /* UAE Green */
            color: white;
            padding: 25px;
            border-radius: 10px;
            margin-top: 20px;
            font-size: 18px;
        }
        .prediction-box h3 {
            font-size: 30px;
        }
        .column-container {
            display: flex;
            justify-content: space-between;
        }
        .column-container div {
            width: 48%;
        }
        .main-container {
            max-width: 1400px;
            margin: 0 auto;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("Health Prediction Dashboard for Somalia")

# Sidebar for User Inputs
st.sidebar.title("Prediction Settings")
region = st.sidebar.selectbox("Select Region", ['Banadir', 'Hargeisa', 'Kismayo', 'Mogadishu', 'Jowhar', 'Bosaso', 'Garowe', 'Burao', 'Berbera', 'Jilib'])
year = st.sidebar.selectbox("Select Year", [2020, 2021, 2022, 2023, 2024])
quarter = st.sidebar.selectbox("Select Quarter", ['Q1', 'Q2', 'Q3', 'Q4'])

# Input Sliders for Prediction Features
st.sidebar.subheader("Input Prediction Parameters")
vaccination_coverage = st.sidebar.slider("Vaccination Coverage (%)", 50, 100, 80)
rainfall = st.sidebar.slider("Rainfall (mm)", 100, 1000, 500)
temperature = st.sidebar.slider("Temperature (°C)", 25, 35, 30)
mosquito_density = st.sidebar.slider("Mosquito Density (per m²)", 10, 200, 100)
bed_net_usage = st.sidebar.slider("Bed Net Usage (%)", 50, 80, 65)
nutritional_intake = st.sidebar.slider("Nutritional Intake (%)", 50, 90, 70)
healthcare_access = st.sidebar.slider("Healthcare Access (%)", 50, 100, 75)
wealth_index = st.sidebar.slider("Wealth Index", 30, 70, 50)
population_density = st.sidebar.slider("Population Density (per km²)", 500, 1500, 1000)

# Prediction Button
if st.sidebar.button("Predict Measles Cases"):
    # Preparing input for prediction
    X_input = np.array([[vaccination_coverage, rainfall, temperature, mosquito_density, bed_net_usage,
                         nutritional_intake, healthcare_access, wealth_index, population_density]])

    # Load the saved models
    try:
        model_measles = joblib.load('measles_model.joblib')
        model_malaria = joblib.load('malaria_model.joblib')
        model_sam = joblib.load('sam_model.joblib')

        # Predictions
        measles_prediction = model_measles.predict(X_input)
        malaria_prediction = model_malaria.predict(X_input)
        sam_prediction = model_sam.predict(X_input)

        # Displaying Predictions in a Stylish Box
        st.markdown(f'<div class="prediction-box"><h3>Predictions:</h3>'
                    f'<p><strong>Measles Cases:</strong> {measles_prediction[0]}</p>'
                    f'<p><strong>Malaria Cases:</strong> {malaria_prediction[0]}</p>'
                    f'<p><strong>SAM Cases:</strong> {sam_prediction[0]}</p></div>',
                    unsafe_allow_html=True)

        # Create Three Tables for Data Display (Table 1, Table 2, Table 3)

        # Table 1: Feature Inputs
        table_1 = pd.DataFrame({
            "Feature": ['Vaccination Coverage (%)', 'Rainfall (mm)', 'Temperature (°C)', 'Mosquito Density (per m²)', 'Bed Net Usage (%)'],
            "Value": [vaccination_coverage, rainfall, temperature, mosquito_density, bed_net_usage]
        })

        # Table 2: Predictions
        table_2 = pd.DataFrame({
            "Prediction": ['Measles Cases', 'Malaria Cases', 'SAM Cases'],
            "Value": [measles_prediction[0], malaria_prediction[0], sam_prediction[0]]
        })

        # Table 3: Additional Inputs (Healthcare and Wealth)
        table_3 = pd.DataFrame({
            "Feature": ['Nutritional Intake (%)', 'Healthcare Access (%)', 'Wealth Index', 'Population Density (per km²)'],
            "Value": [nutritional_intake, healthcare_access, wealth_index, population_density]
        })

        # Display Tables Horizontally (using Flexbox CSS)
        st.markdown('<div class="main-container">', unsafe_allow_html=True)
        st.markdown('<div class="tables-container">', unsafe_allow_html=True)

        # Table 1: Feature Inputs
        st.markdown('<div class="table-box">', unsafe_allow_html=True)
        st.subheader("Table 1: Feature Inputs")
        st.write(table_1)
        st.markdown('</div>', unsafe_allow_html=True)

        # Table 2: Predictions
        st.markdown('<div class="table-box">', unsafe_allow_html=True)
        st.subheader("Table 2: Predictions")
        st.write(table_2)
        st.markdown('</div>', unsafe_allow_html=True)

        # Table 3: Additional Inputs
        st.markdown('<div class="table-box">', unsafe_allow_html=True)
        st.subheader("Table 3: Additional Inputs")
        st.write(table_3)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # Layout using columns for predictions overview
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Measles Prediction Overview")
            st.write(f"Predicted Measles Cases: {measles_prediction[0]}")
            st.write(f"Region: {region}")
            st.write(f"Year: {year}")
            st.write(f"Quarter: {quarter}")

        with col2:
            st.subheader("Malaria and SAM Prediction Overview")
            st.write(f"Predicted Malaria Cases: {malaria_prediction[0]}")
            st.write(f"Predicted SAM Cases: {sam_prediction[0]}")

        # Visualization: Display a chart (optional)
        st.write("### Data Visualization")
        df = pd.DataFrame({
            "Feature": ['Vaccination Coverage (%)', 'Rainfall (mm)', 'Temperature (°C)', 'Mosquito Density (per m²)', 'Bed Net Usage (%)'],
            "Value": [vaccination_coverage, rainfall, temperature, mosquito_density, bed_net_usage]
        })
        st.bar_chart(df.set_index('Feature'))

    except Exception as e:
        st.write(f"Error during prediction: {e}")
