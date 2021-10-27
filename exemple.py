import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Bienvenue sur notre appli Nutri-Sport !")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)

#Visualisations
st.header('Répartition du sucre')
fig, ax = plt.subplots()
df.hist(
  bins=8,
  column="salt_100g",
  grid=False,
  figsize=(7, 7),
  color="Orange",
  zorder=2,
  rwidth=0.9,
  ax=ax,
)
st.write(fig)
