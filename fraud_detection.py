import streamlit as st
import pandas as pd
import joblib


model = joblib.load("fraud_detection_pipeline_updated.pkl")

st.set_page_config(page_title="Financial Fraud Detection", page_icon="💰")

st.title("💳 Financial Fraud Detection App")
st.markdown("Enter transaction details below and click **Predict** to check for potential fraud.")

st.divider()

transaction_type = st.selectbox(
    "Transaction Type", 
    ["PAYMENT", "TRANSFER", "CASH_OUT", "CASH_IN", "DEBIT"]
)
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "balanceDiffOrig": oldbalanceOrg - newbalanceOrig,
        "balanceDiffDest": newbalanceDest - oldbalanceDest,
        "amount_to_oldbalance_ratio": amount / (oldbalanceOrg + 1),
        "balance_change_ratio": newbalanceOrig / (oldbalanceOrg + 1),
        "high_risk_type": int(transaction_type in ['TRANSFER','CASH_OUT']),
        # Default frequencies for unknown users
        "sender_freq": 0.001,
        "receiver_freq": 0.001
    }])

    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    st.subheader(f"Prediction: {int(pred)}")
    st.write(f"Fraud Probability: {prob:.2%}")

    if pred == 1:
        st.error("⚠️ This transaction is likely fraudulent!")
        st.warning(f"High-risk features detected: Type={transaction_type}, Amount={amount}, Balance changes.")
    else:
        st.success("✅ This transaction appears safe.")

