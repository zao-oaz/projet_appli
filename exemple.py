import pandas as pd
import streamlit as st

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)

df.isnull().sum().plot(kind='hist', figsize=(12,7), color="orange")
plt.title('Distribution of NaNs')
plt.xlabel('NaNs')
plt.show()
