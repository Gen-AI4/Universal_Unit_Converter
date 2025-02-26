import streamlit as st
st.set_page_config(page_title="Universal Unit Converter", page_icon="🌍")
st.markdown("""
<style>
/* Dark Mode Background */
body {
    background: #121212 !important; /* Dark background */
    color: white !important;
}

/* Make all text visible */
h1, h2, h3, h4, h5, h6, p, label, span, div {
    color: white !important;
}

/* Fix for Dropdown */
div[data-baseweb="select"] {
    background: #1E1E1E !important; /* Dark background */
    border-radius: 10px;
    border: 2px solid rgba(255, 255, 255, 0.3);
}

/* Dropdown selected text */
div[data-baseweb="select"] * {
    color: white !important;
}

/* Fix dropdown options visibility */
.css-26l3qy-menu {
    background: #1E1E1E !important;
    color: white !important;
    border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Input Fields */
input {
    background: #1E1E1E !important;  /* Dark input background */
    color: white !important;         /* White text */
    border-radius: 10px;
    padding: 10px;
    border: 2px solid rgba(255, 255, 255, 0.5);
}

/* Ensure input text is visible */
input::placeholder {
    color: white !important;
}

/* Fix for Numeric Input Field */
div[data-testid="stNumberInput"] input {
    background: #1E1E1E !important;  /* Dark background */
    color: white !important;         /* White text */
    border-radius: 10px;
    padding: 10px;
}

/* Convert Button */
.stButton > button {
    background: linear-gradient(45deg, #ff416c, #ff4b2b);
    color: white !important;
    border-radius: 10px;
    font-size: 18px;
    padding: 12px;
    width: 100%;
    box-shadow: 0px 0px 10px rgba(255, 71, 92, 0.8);
    font-weight: bold;
    transition: 0.3s;
}

/* Button Hover Effect */
.stButton > button:hover {
    transform: scale(1.05);
    box-shadow: 0px 0px 15px rgba(255, 71, 92, 1);
</style>
""", unsafe_allow_html=True)

conversions = {
    "Length": {
        "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
        "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
    },
    "Weight": {
        "Kilograms": 1, "Grams": 1000, "Milligrams": 1_000_000,
        "Pounds": 2.20462, "Ounces": 35.274
    },
    "Temperature": {
        "Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"
    },
    "Speed": {
        "Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084
    },
    "Time": {
        "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400, "Weeks": 1/604800
    },
    "Volume": {
        "Liters": 1, "Milliliters": 1000, "Cubic meters": 0.001, "Cubic feet": 0.035315, "Gallons (US)": 0.264172
    },
    "Area": {
        "Square meters": 1, "Square kilometers": 0.000001, "Square feet": 10.7639, "Square yards": 1.19599,
        "Acres": 0.000247105, "Hectares": 0.0001
    },
    "Pressure": {
        "Pascals": 1, "Kilopascals": 0.001, "Bars": 0.00001, "PSI": 0.000145038
    },
    "Energy": {
        "Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006, "Kilowatt-hours": 2.77778e-7
    },
    "Power": {
        "Watts": 1, "Kilowatts": 0.001, "Horsepower": 0.00134102
    }
}

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

# Streamlit UI
st.title("🌍 Universal Unit Converter")

category = st.selectbox("Select a category:", list(conversions.keys()))

# Select units
unit_options = list(conversions[category].keys())
from_unit = st.selectbox("From:", unit_options)
to_unit = st.selectbox("To:", unit_options)

# User input
value = st.number_input(f"Enter value in {from_unit}:", format="%.4f")

# Conversion logic
if st.button("Convert"):
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = value * conversions[category][to_unit] / conversions[category][from_unit]
    
    st.success(f"Converted Value: {result:.4f} {to_unit}")
