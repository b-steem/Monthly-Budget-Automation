import streamlit as st
import pandas as pd

st.title("Upload")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the file as csv
    df = pd.read_csv(uploaded_file)
    st.dataframe(df, width=1800, height=1200)
    