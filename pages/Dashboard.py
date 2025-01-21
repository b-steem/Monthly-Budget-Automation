import streamlit as st

st.title("Dashboard")

# accessing sessoin state in other pages
st.write("You have entered", st.session_state["my_input"])