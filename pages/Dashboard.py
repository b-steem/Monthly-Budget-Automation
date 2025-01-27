import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard")

# Amount of money spent monthly from transactional data
# TODO: Pickup from here - https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
try:
    df = pd.read_csv('data/transactions.csv')
    print(df.head(20))
    st.line_chart(df, x="Date", y="Amount")

except:
    st.text("Please upload some data to get started!!!")




# accessing session state in other pages
# st.write("You have entered", st.session_state["my_input"])