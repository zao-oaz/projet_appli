import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)
 
@st.cache
def random_data():
	return random.sample(range(100), 50), random.sample(range(100), 50)

st.subheader("Plotly interactive scatterplot")
x, y = random_data()
fig = px.scatter(x=x, y=y, title="My fancy plot")
v = st_scatterplot(fig)
st.write(v)
