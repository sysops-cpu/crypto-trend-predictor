import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('xgb_crypto_model.pkl')

st.title('🧠 Crypto Trend Predictor')
st.markdown("Predict whether the crypto price will go **UP** or **DOWN** tomorrow using RSI and Fibonacci signals.")

# Input features
rsi = st.slider('RSI', 0, 100, 50)
fib = st.selectbox('In Fibonacci Golden Zone?', ['Yes', 'No'])
ret = st.number_input('Daily Return (%)', value=0.0)

# Format features
features = pd.DataFrame([[ret, rsi, 1 if fib == 'Yes' else 0]], columns=['Return', 'RSI', 'In_Fib_Zone'])

# Prediction
if st.button('🔮 Predict'):
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("📈 Price will likely go UP!")
    else:
        st.warning("📉 Price will likely go DOWN or stay the same.")
