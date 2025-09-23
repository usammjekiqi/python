import streamlit as st
import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 30, 22, 35],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]  


})

st.write(df)


boolks_df = pd.read_csv("books.csv")
st.titile("Best Selling Books")
st.write("This is a list of best selling books")

st.subheader("summary statistics")

total_books = boolks_df.shape[0]
unique_titles = boolks_df["Title"].nunique()
average_rating = boolks_df["User Rating"].mean()
average_price = boolks_df["Price"].mean()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col4.metric("Average Price", f"${average_price:.2f}")
