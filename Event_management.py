import pandas as pd
import streamlit as st
import openpyxl as op

def save_name(name) :
    path="C:\\Users\\Administrator\\Documents\\23CS069\\project1\\Events.xlsx"
    workbook=op.load_workbook(path)
    sheet=workbook.active
    sheet.append([name])
    workbook.save(path)


# Title of the web page
st.title("Name Input and Display")

# Prompt the user to enter their name
name = st.text_input("Please enter your name:")

# Display the entered name
if name:
    save_name(name)
    st.write(f"Hello, {name}! Welcome to the Streamlit app.")
else:
    st.write("Please enter your name to be greeted.")