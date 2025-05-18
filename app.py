import streamlit as st

def convert_units(value:float, unit_from: str, unit_to:str):
    
    # 1 kilometers = 1000 meters
    # 1 meter = 0.001 kilometer
    # 1 meter = 100 centimeters
    #  1 centimeter = 0.01 meter
    if unit_from == "kilometre" and unit_to == "metre":
        return value * 1000
    elif unit_from == "metre" and unit_to == "kilometre":
        return value * 0.001
    elif unit_from == "metre" and unit_to == "centimetre":
        return value * 100
    elif unit_from == "centimetre" and unit_to == "metre":
        return value * 0.01
    elif unit_from == "kilometre" and unit_to == "centimetre":
        return value * 100000
    elif unit_from == "centimetre" and unit_to == "kilometre":
        return value * 0.00001
    else:
        return "Conversion is not supported"

def main():
    st.title("Unit Converter")
    st.write("Welcome to Unit Converter!")
    value = st.number_input("Enter the value you want to be converted:", min_value=0.0)
    unit_from = st.selectbox("Convert from:", ["metre", "kilometre", "centimetre"])
    unit_to = st.selectbox("Convert to:", ["metre", "kilometre", "centimetre"])
    if st.button("Convert"):
        result = convert_units(value, unit_from, unit_to)
        st.write("Result", result)

main()