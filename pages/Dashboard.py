import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

st.title("Dashboard")

# Amount of money spent monthly from transactional data
# TODO: Pickup from here - https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/
# try:
if True:
    df = pd.read_csv('data/transactions.csv')

    # Line Chart
    by_date = df.groupby("Date").sum()
    st.line_chart(by_date, y="Amount")
    
    st.table(df)
    # Bar Chart 
    df["Month"] = pd.to_datetime(df["Date"]).dt.month
    
    # implemented this way so we can see monthly names
    sum_monthly_spend = alt.Chart(df).mark_bar().encode(
        x=alt.X('month(Date):O', title='Month'),
        y=alt.Y('sum(Amount):Q', 
                title='Total Amount Spent',
                axis=alt.Axis(grid=True)),
        tooltip=[
            alt.Tooltip('month(Date):O', title='Month'),
            alt.Tooltip('sum(Amount):Q', title='Total Amount Spent', format='.1f')
        ]
    ).properties(
        width=600,
        height=300,
        title='Total Amount Spent Per Month'
    )
    sum_monthly_spend
    
    # Average monthly bar chart
    avg_monthly_spend = alt.Chart(df).mark_bar().encode(
        x=alt.X('month(Date):O', title='Month'),
        y=alt.Y('mean(Amount):Q', 
                title='Total Amount Spent',
                axis=alt.Axis(grid=True)),
        tooltip=[
            alt.Tooltip('month(Date):O', title='Month'),
            alt.Tooltip('sum(Amount):Q', title='Average Amount Spent', format='.1f')
        ]
    ).properties(
        width=600,
        height=300,
        title='Average Amount Spent Per Month'
    )
    avg_monthly_spend

    # Average daily bar chart (broken down by avg amount spend per day of the month)
    avg_daily_per_month_df = df
    avg_daily_per_month_df["Day of Month"] = pd.to_datetime(df["Date"]).dt.day
    avg_daily_per_month_df = avg_daily_per_month_df.groupby("Day of Month").agg(
        Mean_Spend = ("Amount", "mean")
    )
    st.bar_chart(avg_daily_per_month_df, y_label="Average Daily Spend Per Month", x_label="Day of the Month")

    # Average weekly bar chart (broken down by avg amount spend per day of the week)
    avg_daily_per_week_df = df
    avg_daily_per_week_df["Day of Week"] = pd.to_datetime(df["Date"]).dt.day_of_week
    avg_daily_per_week_df = avg_daily_per_week_df.groupby("Day of Week").agg(
        Mean_Spend = ("Amount", "mean")
    )
    st.bar_chart(avg_daily_per_week_df, y_label="Average Daily Spend by Week", x_label="Day of the Week")


# except:
#     st.text("Please upload some data to get started!!!")



# maybe useful for other cases
# accessing session state in other pages
# st.write("You have entered", st.session_state["my_input"])