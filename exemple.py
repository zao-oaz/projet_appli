conda install matplotlib

import pandas as pd
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)
import matplotlib.pyplot as plt
import matplotlib
import time 

#
@st.cache(hash_funcs={matplotlib.figure.Figure: hash})
def plot():
    time.sleep(2)
    arr = np.random.normal(1, 1, size=(100,horizontal_size))
    fig, ax = plt.subplots()
    ax.imshow(arr)
    
    return fig

horizontal_size = st.slider("horizontal size", 50,150,step=50)
st.write(plot())
