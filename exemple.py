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

#
option = st.selectbox(
  'How would you like to be contacted?',
  ('Sucre', 'Sel', 'Fibres', 'proteins_100g'))

st.write('You selected:', option)  
  
#Visualisations1
st.header('Répartition du sel')
fig, ax = plt.subplots()
df.hist(
  column="salt_100g",
  grid=False,
  figsize=(5, 5),
  color="Orange",
  ax=ax,
)
st.write(fig)

#Visualisations2
st.header('Répartition du sucre')
fig, ax = plt.subplots()
df.hist(
  column="sugars_100g",
  grid=False,
  figsize=(5, 5),
  color="Orange",
  ax=ax,
)
st.write(fig)

#Visualisations3
st.header('Répartition des proteines')
fig, ax = plt.subplots()
df.hist(
  column="proteins_100g",
  grid=False,
  figsize=(5, 5),
  color="Orange",
  ax=ax,
)
st.write(fig)

#Visualisations4
st.header('Répartition des fibres')
fig, ax = plt.subplots()
df.hist(
  column="fiber_100g",
  grid=False,
  figsize=(5, 5),
  color="Orange",
  ax=ax,
)
st.write(fig)
