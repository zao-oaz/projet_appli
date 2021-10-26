
import streamlit as st

st.title("nutrition_app")

import pandas as pd

df = pd.read_csv("C:\Users\zaome\Documents\Alisson\Flask\database_clean.csv", sep="|")

import plotly.express as px

corr = df.corr()
px.imshow(corr)
