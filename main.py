import streamlit as st
import pandas as pd
from PIL import Image

st.title("Housing Price Predictor")
data = pd.read_csv("Bengaluru_House_Data.csv")
nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

if nav == "Home":
    st.write("Home")
    image = Image.open("house-prices-rising-2.jpg")
    st.image(image)
    if st.checkbox("Show Data Table"):
        st.write(data.head(15))
elif nav == "Prediction":
    st.write("Pred")

elif nav == "Contribute":
    st.header("Contribute to our dataset")
    ex = st.number_input("enter your experience",0.0,20.0)
    sal = st.number_input("enter your salary",0.00,1000000.00,step=1000.0)
    if st.button("Submit"):
        to_add = {"Years of Experiece":[ex],"Salary":[sal]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv(r"C:\Users\abc\PycharmProjects\Streamlit_new_demo\Salary_data.csv",mode='a',header=False,index=False)
        st.success("Thank you for your submission")