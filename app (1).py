import streamlit as st
import pickle
import numpy as np

# Page config
st.set_page_config(
    page_title="Student Mark Predictor",
    page_icon="🎓",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #0a0a0f;
}

.main-title {
    font-family: 'Syne', sans-serif;
    font-size: 2.8rem;
    font-weight: 800;
    color: #ffffff;
    text-align: center;
    margin-bottom: 0.3rem;
    letter-spacing: -1px;
}

.main-title span {
    color: #00e5ff;
}

.subtitle {
    text-align: center;
    color: #555577;
    font-size: 0.9rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
}

.card-title {
    color: #00e5ff;
    font-size: 0.75rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 1.5rem;
}

.result-box {
    background: linear-gradient(135deg, #00e5ff15, #0077ff15);
    border: 1px solid #00e5ff40;
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    margin-top: 1rem;
}

.result-value {
    font-family: 'Syne', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    color: #00e5ff;
    line-height: 1;
}

.stButton > button {
    background: linear-gradient(135deg, #00e5ff, #0077ff) !important;
    color: #000000 !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 0.8rem 2rem !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    width: 100% !important;
}

.footer {
    text-align: center;
    color: #2a2a3a;
    font-size: 0.75rem;
    letter-spacing: 2px;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Load model
@st.cache_resource
def load_model():
    try:
        model = pickle.load(open('model.pkl', 'rb'))
        return model
    except:
        return None

model = load_model()

# Header
st.markdown('<div class="main-title">Student Mark <span>Predictor</span></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">🎓 AI & Data Science 🎓</div>', unsafe_allow_html=True)

# Inputs
st.markdown('<div class="card-title">Enter Semester Marks (out of 10)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    first = st.number_input("1st Semester", min_value=0.0, max_value=10.0, value=7.0, step=0.01)
    third = st.number_input("3rd Semester", min_value=0.0, max_value=10.0, value=7.0, step=0.01)
with col2:
    second = st.number_input("2nd Semester", min_value=0.0, max_value=10.0, value=7.0, step=0.01)
    fourth = st.number_input("4th Semester", min_value=0.0, max_value=10.0, value=7.0, step=0.01)

st.markdown("<br>", unsafe_allow_html=True)

# Predict
if st.button("PREDICT 5TH SEM MARK 🚀"):
    if model is not None:
        input_data = np.array([[first, second, third, fourth]])
        prediction = model.predict(input_data)[0]

        # Grade
        if prediction >= 8.5:
            grade = "🏆 Outstanding"
            color = "#00e5ff"
        elif prediction >= 7.5:
            grade = "⭐ Excellent"
            color = "#00ff88"
        elif prediction >= 6.5:
            grade = "✅ Good"
            color = "#ffcc00"
        elif prediction >= 5.5:
            grade = "📚 Average"
            color = "#ff8800"
        else:
            grade = "⚠️ Needs Improvement"
            color = "#ff4444"

        st.markdown(f"""
        <div class="result-box">
            <div style="color:#555577;font-size:0.85rem;letter-spacing:2px;">PREDICTED 5TH SEM MARK</div>
            <div class="result-value">{prediction:.2f}</div>
            <div style="color:{color};font-size:1.1rem;margin-top:0.8rem;font-weight:600;">{grade}</div>
        </div>
        """, unsafe_allow_html=True)

        avg = (first + second + third + fourth) / 4
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        c1.metric("Avg Input", f"{avg:.2f}")
        c2.metric("Predicted", f"{prediction:.2f}")
        c3.metric("Difference", f"{prediction-avg:+.2f}")
    else:
        st.error("⚠️ model.pkl not found! Same folder-la irukana check pannunga.")

st.markdown('<div class="footer">BUILT BY VISHVA M | B.TECH AI & DS | THANGAVELU ENGINEERING COLLEGE</div>', unsafe_allow_html=True)
