import pandas as pd
import streamlit as st

st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv("C:/Users/zaome/Documents/Alisson/Flask/database_clean.csv")
  st.write(df)
