import streamlit as st

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.title("🏋️ BMI Calculator")
st.write("Calculate your Body Mass Index (BMI) easily.")

with st.sidebar:
    st.write("### Enter Your Details")
    weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1, format="%.1f")
    height = st.number_input("Height (m)", min_value=0.5, step=0.01, format="%.2f")
    calculate = st.button("Calculate BMI")

if calculate:
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        st.success(f"Your BMI is: {bmi}")
        st.info(f"Category: {category}")
    else:
        st.error("Please enter valid weight and height values.")
