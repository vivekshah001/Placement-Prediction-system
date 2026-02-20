import streamlit as st
import pandas as pd
import joblib
import os

# HEADING
# st.set_page_config(page_title="India Engineering Student Placement Prediction", page_icon="🎓")

# st.set_page_config(page_title="India Engineering Student Placement Prediction")
# st.markdown(
#     """
#     <div style="
#         background-color:#fff3cd;
#         padding:20px;
#         border-radius:10px;
#         margin-bottom:25px;
#         text-align:center;
#     ">
#         <h1 style="
#             color:#856404;
#             font-weight:800;
#             margin:0;
#         ">
#             India Engineering Student Placement Prediction
#         </h1>
#         <p style="
#             color:#856404;
#             margin-top:10px;
#             font-size:16px;
#         ">
#             Predict placement outcomes using academic, skill, and lifestyle factors
#         </p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )





import streamlit as st

# 1. Injecting 2026 Premium CSS
st.markdown("""
<style>
    /* Deep midnight gradient background */
    .stApp {
        background: radial-gradient(circle at top left, #0f172a, #020617);
        font-family: 'Inter', sans-serif;
    }
    
    /* Liquid Glass Header Card */
    .premium-header {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 24px;
        padding: 40px;
        text-align: center;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        margin-bottom: 3rem;
        margin-top: 1rem;
    }
    
    /* Gradient Text for Title */
    .premium-title {
        background: linear-gradient(135deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 15px;
        line-height: 1.2;
        letter-spacing: -1px;
    }
    
    /* Sleek Subtitle */
    .premium-subtitle {
        color: #94a3b8;
        font-size: 1.15rem;
        font-weight: 400;
        letter-spacing: 0.5px;
    }

    /* Neumorphic/Glassy Dropdown Menus */
    div[data-baseweb="select"] > div {
        background-color: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        transition: all 0.3s ease;
    }
    
    /* Glowing Hover Effect for Inputs */
    div[data-baseweb="select"] > div:hover {
        border-color: #818cf8;
        box-shadow: 0 0 15px rgba(129, 140, 248, 0.2);
        background-color: rgba(255, 255, 255, 0.08);
    }

    /* Clean Input Labels */
    .stSelectbox label {
        color: #cbd5e1 !important;
        font-weight: 500;
        font-size: 0.95rem;
        padding-bottom: 5px;
    }
</style>
""", unsafe_allow_html=True)

# 2. Render the new Liquid Glass Header
st.markdown("""
<div class="premium-header">
    <div class="premium-title">India Engineering Student<br>Placement Prediction</div>
    <div class="premium-subtitle">Predict placement outcomes using academic, skill, and lifestyle factors</div>
</div>
""", unsafe_allow_html=True)

# 3. Your standard Streamlit inputs go here
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
branch = st.selectbox("Branch", ["CSE", "ECE", "Mechanical", "Civil"])
# ... rest of your code ...























# ============================
# MODEL LOADING
# ============================
@st.cache_resource
def load_artifacts():
    model = joblib.load("model (1).pkl")
    ct = joblib.load("enc_transformer.pkl")
    return model, ct

model, ct = load_artifacts()

# ---- collect RAW inputs only ----

# ======================
# CATEGORICAL INPUTS
# =======================
gender = st.selectbox("Gender", ["Male", "Female"])
branch = st.selectbox("Branch", ["CSE", "ECE", "ME", "CE", "EEE"])
city_tier = st.selectbox("City Tier", ["Tier 1", "Tier 2", "Tier 3"])
part_time_job = st.selectbox("Part Time Job", ["Yes", "No"])
internet_access = st.selectbox("Internet Access", ["Yes", "No"])
family_income_level = st.selectbox("Family Income Level", ["Low", "Medium", "High"])
extracurricular_involvement = st.selectbox("Extracurricular Involvement", ["High", "Medium", "Low"])


# ======================
# NUMERICAL INPUTS
# =======================

student_id = st.number_input("Student ID")
cgpa = st.number_input("CGPA", 0.0, 10.0, 7.0)
tenth_percentage = st.number_input("10th Percentage", 0.0, 100.0, 75.0)
twelfth_percentage = st.number_input("12th Percentage", 0.0, 100.0, 72.0)
backlogs = st.number_input("Backlogs", 0, 10, 0)
study_hours_per_day = st.number_input("Study Hours per Day", 0, 24, 2)
attendence_percentage = st.number_input("Attendance Percentage", 0.0, 100.0, 80.0)
projects_completed = st.number_input("Projects Completed", 0, 10, 2)
internships_completed = st.number_input("Internships", 0, 10, 1)
coding_skills_rating = st.number_input("Coding Skills Rating (1-10)", 1, 10, 5)
communication_skills_rating = st.number_input("Communication Skills Rating (1-10)", 1, 10, 5)
aptitude_skills_rating = st.number_input("Aptitude Skills Rating (1-10)", 1, 10, 5)
hackathon_participation = st.number_input("Hackathon Participation", 0, 10, 0)
certifications_count= st.number_input("Certifications Completed", 0, 10, 0)
sleep_hours_per_night = st.number_input("Sleep Hours per Night", 0, 24, 7)
stress_level = st.number_input("Stress Level (1-10)", 1, 10, 5)


# =============
# total inputs(24)
#==============

df = pd.DataFrame({
    "gender": [gender],
    "branch": [branch],
    "city_tier": [city_tier],
    "part_time_job": [part_time_job],
    "internet_access": [internet_access],
    "family_income_level": [family_income_level],
    "extracurricular_involvement": [extracurricular_involvement],

    "Student_ID": [student_id],  # CASE FIXED
    "cgpa": [cgpa],
    "tenth_percentage": [tenth_percentage],
    "twelfth_percentage": [twelfth_percentage],
    "backlogs": [backlogs],
    "study_hours_per_day": [study_hours_per_day],
    "attendance_percentage": [attendence_percentage],  # SPELLING FIXED

    "projects_completed": [projects_completed],
    "internships_completed": [internships_completed],

    "coding_skill_rating": [coding_skills_rating],  # NAME FIXED
    "communication_skill_rating": [communication_skills_rating],  # NAME FIXED
    "aptitude_skill_rating": [aptitude_skills_rating],  # NAME FIXED

    "hackathons_participated": [hackathon_participation],  # NAME FIXED
    "certifications_count": [certifications_count],
    "sleep_hours": [sleep_hours_per_night],  # NAME FIXED
    "stress_level": [stress_level]
})


# ==================================
#  prediction
# ==================================

if st.button("Predict Placement"):
    try:
        # Preprocess the input data
        df_encoded = ct.transform(df)
        
        # Make prediction
        prediction = model.predict(df_encoded)
        
        # Display the result
        if prediction[0] == 1:
            st.success("The student is likely to get placed.")
        else:
            st.error("The student is unlikely to get placed.")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        









