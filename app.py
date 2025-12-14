import pickle
import streamlit as st
import numpy as np

# -------------------- Page Config --------------------
st.set_page_config(
    page_title="Salary Predictor",
    page_icon="💼",
    layout="centered"
)

# -------------------- Custom CSS --------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #f8f9fa, #e9ecef);
}
h1 {
    text-align: center;
    color: #343a40;
}
.salary-box {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    text-align: center;
}
.result {
    font-size: 28px;
    font-weight: bold;
    color: #198754;
}
.footer {
    text-align: center;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)

# -------------------- Load Model --------------------
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# -------------------- Header --------------------
st.markdown("<h1>💼 Smart Salary Predictor</h1>", unsafe_allow_html=True)
st.write("### Predict your salary using Machine Learning")
st.divider()

# -------------------- Sidebar --------------------
st.sidebar.header("📌 Input Details")
years_exp = st.sidebar.slider(
    "Years of Experience",
    min_value=0.0,
    max_value=40.0,
    step=0.5
)

st.sidebar.info("This model predicts salary based on experience using Linear Regression.")

# -------------------- Main Card --------------------
st.markdown("<div class='salary-box'>", unsafe_allow_html=True)
st.write("### 🔍 Prediction Result")

if st.button("🚀 Predict Salary"):
    prediction = model.predict([[years_exp]])
    st.markdown(
        f"<div class='result'>₹ {prediction[0]:,.2f}</div>",
        unsafe_allow_html=True
    )
else:
    st.write("👈 Adjust the slider and click **Predict Salary**")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------- Footer --------------------
st.markdown(
    "<div class='footer'>Built with ❤️ using Streamlit & Machine Learning</div>",
    unsafe_allow_html=True
)
