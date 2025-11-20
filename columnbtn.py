import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.header("Column1")
    st.write("This button is the first column.")
    st.button("Button 1")

with col2:
    st.header("Column2")
    st.write("This is the second column")
    st.button("Button 2")