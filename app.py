import streamlit as st

def calculate_body_fat(age, gender, weight, height_feet):
   
    height_meters = height_feet * 0.3048
    if gender == 'Male':
        body_fat_percentage = (1.20 * (weight / (height_meters ** 2))) + (0.23 * age) - 16.2
    else:  
        body_fat_percentage = (1.20 * (weight / (height_meters ** 2))) + (0.23 * age) - 5.4
    return body_fat_percentage


st.title("BMI Calculator")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.selectbox("Gender", options=["Male", "Female"])
weight = st.number_input("Weight", min_value=1.0, value=70.0)
height_feet = st.number_input("Height (in feet)", min_value=1.0, value=5.5)

if st.button("Calculate"):
    body_fat = calculate_body_fat(age, gender, weight, height_feet)
    st.success(f"Estimated Body Fat Percentage: {body_fat:.2f}%")
