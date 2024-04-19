import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt


st.set_page_config(layout="wide")

st.title('Timo data analysis - Duong Thi Huyen Tran report')


add_navigation_app = st.sidebar.page_link("app.py", label="Data Analyst")


st.header('Transactions vs Age groups', divider='rainbow')

st.subheader('Data table')

# Import CSV file
transactions_per_age_group = pd.read_csv('./data/transactions_per_age_group.csv')

transactions_per_age_group

st.subheader('Charts')

col1, col2, col3 = st.columns(3)

with col1:
    number_accounts_chart = alt.Chart(transactions_per_age_group, title='Number accounts').mark_bar().encode(
        x='age_group', y='Number accounts')
    st.altair_chart(number_accounts_chart, use_container_width=True)

with col2:
    number_transactions_chart = alt.Chart(transactions_per_age_group, title='Number transactions').mark_bar().encode(
        x='age_group', y='Number transactions')
    st.altair_chart(number_transactions_chart, use_container_width=True)

with col3:
    transaction_per_account_chart = alt.Chart(transactions_per_age_group, title='Transactions per account').mark_bar().encode(
        x='age_group', y='Transactions per account')
    st.altair_chart(transaction_per_account_chart, use_container_width=True)


st.header('Transactions time series', divider='rainbow')
st.subheader('Data table')


transactions_time_series_col1, transactions_time_series_col2 = st.columns(2)

# Import CSV file
transactions_per_date = pd.read_csv('./data/transactions_per_date.csv')
transactions_per_month = pd.read_csv('./data/transactions_per_month.csv')

with transactions_time_series_col1:
    st.subheader('Transactions per Date')
    transactions_per_date

with transactions_time_series_col2:
    st.subheader('Transactions per Month')
    transactions_per_month

st.subheader('Charts')

st.subheader('Transactions per Date')
transactions_per_date_col1, transactions_per_date_col2 = st.columns(2)

with transactions_per_date_col1:
    transactions_count_per_date_chart = alt.Chart(transactions_per_date, title='Transactions count').mark_line().encode(
        x='Date', y='Total Transactions')
    st.altair_chart(transactions_count_per_date_chart, use_container_width=True)

with transactions_per_date_col2:
    transactions_amount_per_date_chart = alt.Chart(transactions_per_date, title='Transactions amount').mark_line().encode(
        x='Date', y='Total Amount')
    st.altair_chart(transactions_amount_per_date_chart, use_container_width=True)


st.subheader('Transactions per Month')
transactions_per_month_col1, transactions_per_month_col2 = st.columns(2)

with transactions_per_month_col1:
    transactions_count_per_month_chart = alt.Chart(transactions_per_month, title='Transactions count').mark_line().encode(
        x='Month', y='Total Transactions')
    st.altair_chart(transactions_count_per_month_chart, use_container_width=True)

with transactions_per_month_col2:
    transactions_amount_per_month_chart = alt.Chart(transactions_per_month, title='Transactions amount').mark_line().encode(
        x='Month', y='Total Amount')
    st.altair_chart(transactions_amount_per_month_chart, use_container_width=True)


st.header('Transactions vs transaction types', divider='rainbow')

st.subheader('Data table')

transactions_per_type = pd.read_csv('./data/transactions_per_type.csv')

transactions_per_type

st.subheader('Charts')

transactions_per_type_col1, _, _ = st.columns(3)

with transactions_per_type_col1:
    pie_chart_data = transactions_per_type
    fig, ax = plt.subplots(figsize = (20,12))
    plt.pie(pie_chart_data['Transaction count'], labels=pie_chart_data['Transaction type'], explode=[0.05, 0.05, 0, 0, 0, 0, 0], textprops={ 'fontsize': 24})
    st.pyplot( plt )