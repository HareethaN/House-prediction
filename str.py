import streamlit as st
import requests

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Loan Approval Prediction")

st.write("Enter the applicant details to predict loan approval.")

income = st.number_input(
    "Income",
    min_value=0.0,
    value=50000.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0.0,
    max_value=900.0,
    value=700.0
)

employment_type = st.selectbox(
    "Employment Type",
    ["Salaried", "Self-Employed", "Unemployed"]
)

region = st.selectbox(
    "Region",
    ["Chennai", "Bangalore", "coimbatore", "Madurai","Salem"]
)

if st.button("🔍 Predict Loan Approval"):

    data = {
        "income": income,
        "creditscore": credit_score,
        "employment_type": employment_type,
        "region": region
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        result = response.json()

        st.subheader("Prediction Result")

        if result["prediction"] == "Approve":
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

        probability = result["probability"]

        st.write(
            f"Approval Probability: **{probability * 100:.1f}%**"
        )

        st.progress(probability)

    except Exception:

        st.error(
            "Unable to connect to Flask API. "
            "Make sure the Flask server is running."
        )