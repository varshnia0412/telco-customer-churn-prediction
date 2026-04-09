import streamlit as st
import pandas as pd
import pickle

# Load the brain
model = pickle.load(open('churn_model.pkl', 'rb'))
cols = pickle.load(open('columns.pkl', 'rb'))

st.title("📊 Customer Churn Predictor")

# Input Fields
tenure = st.number_input("Months stayed with company", 0, 72, 12)
contract = st.selectbox("Contract Type", ['Month-to-month', 'One year', 'Two year'])
internet = st.selectbox("Internet Service Type", ['DSL', 'Fiber optic', 'No']) # Added this!
monthly = st.number_input("Monthly Bill ($)", 0, 200, 70)

if st.button("Predict"):
    # Create a tiny table for the prediction
    df_input = pd.DataFrame(columns=cols)
    df_input.loc[0] = 0 
    
    # Fill in the basics
    df_input['tenure'] = tenure
    df_input['MonthlyCharges'] = monthly
    
    # Fill in the categories (Logic to match your 81% model)
    if f"Contract_{contract}" in df_input.columns:
        df_input[f"Contract_{contract}"] = 1
    if f"InternetService_{internet}" in df_input.columns:
        df_input[f"InternetService_{internet}"] = 1
    
    # Make the prediction
    prediction = model.predict(df_input)[0]
    
    if prediction == 1:
        st.error("⚠️ HIGH RISK: This customer is likely to CHURN.")
    else:
        st.success("✅ LOW RISK: This customer is likely to STAY.")
