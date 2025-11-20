import streamlit as st

st.sidebar.title("Navigation")
option = st.sidebar.selectbox("Choose a page:", ["Home", "About", "Contact"])

if option == "Home":
    st.write("Welcome to the Home Page!")
elif option == "About":
    st.write("This is the About Page!")
elif option == "Contact":
    st.write("This is the contact page!")