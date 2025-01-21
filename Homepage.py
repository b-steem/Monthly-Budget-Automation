""" This page is displays the homepage """

import streamlit as st

st.set_page_config(page_title="AutoDash", page_icon="😎")

st.title("AutoDash")
st.sidebar.success("Select a page")

# Saving items to session state
if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Input a text here", st.session_state["my_input"])
submit = st.button("Submit")
if submit:
    st.session_state["my_input"] = my_input
    st.write("You have entered: ", my_input)