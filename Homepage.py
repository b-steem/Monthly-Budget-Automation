""" This page is displays the homepage """

import streamlit as st

# Config
st.set_page_config(page_title="AutoDashly", page_icon="😎")

# Side bar
st.sidebar.success("Select a page")

# \/ Body 
st.title("Welcome to AutoDashly!!! 👋")

st.text("An intuitive automation dashboard designed to show users visualizations of their net worth")

st.subheader("Getting Started")
st.text("To get started you have two options.")

st.subheader("Option 1")
st.text("To see how the dashboard works - using test data - go to Dashboard.")
st.page_link('pages/Dashboard.py')
st.text("You can add files using the upload csv button.")
st.page_link('pages/Upload.py')

st.subheader("Option 2")
st.text("To use your own transactions, clone my github repo and run the server on your local machine.")


# Saving items to session state
# if "my_input" not in st.session_state:
#     st.session_state["my_input"] = ""

# my_input = st.text_input("Input a text here", st.session_state["my_input"])
# submit = st.button("Submit")
# if submit:
#     st.session_state["my_input"] = my_input
#     st.write("You have entered: ", my_input)
