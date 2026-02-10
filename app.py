import streamlit as st
import pandas as pd
import joblib

st.title("Placement Prediction App")

# Load dataset
df = pd.read_csv("data/indian_engineering_student_placement.csv")


# Load model & transformer
model = joblib.load("model/model.pkl")
transformer = joblib.load("model/column_transformer.pkl")

st.success("Data aur model successfully load ho gaye 👍")

st.subheader("Dataset Preview")
st.dataframe(df.head())
