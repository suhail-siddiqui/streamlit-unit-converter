import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversions = {
        "Length": {
            "Meter": 1,
            "Kilometer": 0.001,
            "Centimeter": 100,
            "Millimeter": 1000,
            "Mile": 0.000621371,
            "Yard": 1.09361,
            "Foot": 3.28084,
            "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1,
            "Gram": 1000,
            "Pound": 2.20462,
            "Ounce": 35.274
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: (x * 9/5) + 32,
            "Kelvin": lambda x: x + 273.15
        }
    }
    
    if category == "Temperature":
        if from_unit == "Celsius":
            if to_unit == "Fahrenheit":
                return (value * 9/5) + 32
            elif to_unit == "Kelvin":
                return value + 273.15
        elif from_unit == "Fahrenheit":
            if to_unit == "Celsius":
                return (value - 32) * 5/9
            elif to_unit == "Kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            if to_unit == "Celsius":
                return value - 273.15
            elif to_unit == "Fahrenheit":
                return (value - 273.15) * 9/5 + 32
    else:
        return value * (conversions[category][to_unit] / conversions[category][from_unit])

st.title("Unit Converter")

category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Units dictionary
unit_options = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Selecting units
from_unit = st.selectbox("From Unit", unit_options[category])
to_unit = st.selectbox("To Unit", unit_options[category])
value = st.number_input("Enter Value", value=0.0)

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.write(f"Converted Value: {result} {to_unit}")
