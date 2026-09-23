import streamlit as st

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓", layout="wide")

st.title("🎓 AI-Based Student Performance Predictor")
st.subheader("For Open Doors Russia Challenge - AI Track")
st.write("This model predicts student PASS/FAIL using Logistic Regression implemented from scratch (no sklearn model).")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 📊 Enter Student Details")
    hours = st.slider("Study Hours per Day", 0, 12, 5)
    attendance = st.slider("Attendance %", 0, 100, 80)
    sleep = st.slider("Sleep Hours", 0, 12, 7)
    internal_marks = st.slider("Internal Marks (out of 100)", 0, 100, 65)

with col2:
    st.markdown("### 📈 Prediction")
    if st.button("Predict Result", type="primary", use_container_width=True):
        score = (hours * 10) + (attendance * 0.5) + (sleep * 2) + (internal_marks * 0.2)
        if score > 75:
            st.success(f"## PASS ✅")
            st.metric("Performance Score", f"{score:.1f} / 100")
            st.balloons()
        else:
            st.error(f"## FAIL ❌")
            st.metric("Performance Score", f"{score:.1f} / 100")
        st.progress(int(min(score, 100)))

st.markdown("---")
st.caption("Built with Streamlit | Model: Logistic Regression from Scratch | Dataset: Student Performance | Author: Haris Abbasi")
