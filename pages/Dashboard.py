import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

st.title("Dashboard")

# Amount of money spent monthly from transactional data
# TODO: Pickup from here - https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
# try:
df = pd.read_csv('data/transactions.csv')
st.line_chart(df, x="Date", y="Amount")

df["Month"] = pd.to_datetime(df["Date"]).dt.month
# st.bar_chart(df, x=alt.X('month(Date):0', title='Month'), y="Amount")

basic_chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('month(Date):O', title='Month'),
    y=alt.Y('sum(Amount):Q', 
            title='Total Amount Spent',
            axis=alt.Axis(grid=True)),
    tooltip=[
        alt.Tooltip('month(date):O', title='Month'),
        alt.Tooltip('sum(Amount):Q', title='Total Amount Spent', format='.1f')
    ]
).properties(
    width=600,
    height=300,
    title='Total Amount Spent Per Month'
)
basic_chart

# except:
#     st.text("Please upload some data to get started!!!")




# accessing session state in other pages
# st.write("You have entered", st.session_state["my_input"])