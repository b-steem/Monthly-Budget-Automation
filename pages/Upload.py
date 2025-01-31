import streamlit as st

st.title("Upload")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Read the file as csv
    pass
    