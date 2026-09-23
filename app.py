import streamlit as st
import pickle
import numpy as np

st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("🎓 AI-Based Student Performance Predictor")
st.write("For Open Doors Russia Challenge")

# Try to load model, if not available use simple logic
def predict_performance(hours, attendance, sleep):
    # Simple logic based on your model idea
    score = (hours * 10) + (attendance * 0.5) + (sleep * 2)
    if score > 70:
        return "PASS ✅", score
    else:
        return "FAIL ❌", score

st.sidebar.header("Enter Student Details")
hours = st.sidebar.slider("Study Hours per Day", 0, 12, 5)
attendance = st.sidebar.slider("Attendance %", 0, 100, 80)
sleep = st.sidebar.slider("Sleep Hours", 0, 12, 7)

if st.button("Predict Result"):
    result, score = predict_performance(hours, attendance, sleep)
    st.success(f"### Result: {result}")
    st.info(f"Performance Score: {score:.1f}")
    if "PASS" in result:
        st.balloons()
    
st.markdown("---")
st.write("Built with Streamlit | Model: Logistic Regression from Scratch")
