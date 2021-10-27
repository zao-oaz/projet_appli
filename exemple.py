import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Bienvenue sur Nutri-Sport ! 🥇")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)

#Selections
option = st.selectbox(
  'Sélectionner vos critères alimentaires',
  ('Sucre', 'Sel', 'Fibres', 'Proteines'))
st.write('You selected:', option)  

#text1
txt = st.text_area('Le sel', ''' 4g de sel sont nécessaires au bon fonctionnement de l'organisme : transmission des 
signaux nerveux, contraction musculaire et fonctionnement des reins en assurant une bonne hydratation. Le sel gouverne, avec le potassium, tout l'équilibre hydrique de l'organisme.''')
st.write()

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

#text2
txt = st.text_area('Le sucre', ''' Récemment, l'OMS (Organisation mondiale de la santé) a revu à la baisse ses préconisations 
sur le sucre qui doit constituer, selon ses conseils, 5 % des apports énergétiques quotidiens, c'est-à-dire, l'équivalent de 25 grammes par jour, soit six cuillères à café pour une ration de 2.000 calories.''')
st.write()

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

#text3
txt = st.text_area('Les protéines', '''Les protéines fournissent de l'énergie à l'organisme, environ quatre calories par gramme. Ainsi, tout comme les lipides et les glucides, ces micronutriments sont 
essentiels pour assurer le bon fonctionnement de l'organisme.''')
st.write()

#Visualisations3
st.header('Répartition des protéines')
fig, ax = plt.subplots()
df.hist(
  column="proteins_100g",
  grid=False,
  figsize=(5, 5),
  color="Orange",
  ax=ax,
)
st.write(fig)

#text4
txt = st.text_area('Les fibres', '''Les bienfaits de ces dernières sont attestés dans la prévention de l'obésité, du diabète, du cholestérol et des pathologies induites, mais aussi dans la 
prévention du cancer du côlon.''')
st.write()

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
