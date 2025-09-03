import streamlit as st
st.title("Welcome to streamlit app")
name = st.text_input("Enter your name")
st.write(f"Hello,{name}!")
