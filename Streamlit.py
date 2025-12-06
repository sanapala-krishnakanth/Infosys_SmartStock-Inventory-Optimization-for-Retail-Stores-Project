import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv(
    r"E:\Smart stock optimization for retail stores\Data preprocessing\smart-stock.csv",
    on_bad_lines='skip'   
)


st.title("📊 Smart stock optimization")
st.write("Optimising the product and Prices.")

st.write("Data used for the bar chart:")
st.dataframe(df)
st.write("Bar CHart Analysis")
st.bar_chart(df, x="Product ID", y="Price")
st.write("Line CHart Analysis")
st.line_chart(df, x="Product ID", y="Price")

st.title("My First Streamlit App")
st.write("Hello! Streamlit is working.")




