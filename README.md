Universal Unit Converter - Explanation Document
Introduction

The Universal Unit Converter is an online application programmed with Streamlit, a library in Python that allows for web interactive app generation. The app provides the capacity to convert data between different units in many classes, including Length, Weight, Temperature, Speed, Time, Volume, Area, Pressure, Energy, and Power. It has a futuristic dark mode app interface, contributing to both usefulness and aesthetic sense. This paper describes the app's functionality, how it works, and outlines its code organization.
Features

The Universal Unit Converter has the following main features:

    Supported Categories and Units:
        Length: Meters, Kilometers, Centimeters, Millimeters, Miles, Yards, Feet, Inches
        Weight: Kilograms, Grams, Milligrams, Pounds, Ounces
Temperature: Celsius, Fahrenheit, Kelvin
        Speed: Meters per second, Kilometers per hour, Miles per hour, Feet per second
        Time: Seconds, Minutes, Hours, Days, Weeks
        Volume: Liters, Milliliters, Cubic meters, Cubic feet, Gallons (US)
Area: Square meters, Square kilometers, Square feet, Square yards, Acres, Hectares
        Pressure: Pascals, Kilopascals, Bars, PSI
        Energy: Joules, Kilojoules, Calories, Kilowatt-hours
        Power: Watts, Kilowatts, Horsepower
Dark Mode Theme: A dark background with contrasting text and elements is applied using a custom CSS stylesheet for improved readability.
Interactive Interface: Streamlit widgets are used to build the app, giving it an intuitive interface with dropdowns, input fields, and a conversion button.

How It Works

The app takes the user through an easy conversion process:

Select a Category: The user selects a category (e.g., "Length") from a drop-down list.
Choose Units: Two drop-downs enable the user to choose the "From" unit (source) and "To" unit (target) depending on the selected category.
Enter a Value: The user enters a numeric value to convert via a number input field.
Perform Conversion: Pressing the "Convert" button initiates the calculation, and the answer is shown.

Conversion Logic

    Most Categories: For categories such as Length, Weight, and Speed, the conversion employs a ratio-based approach. Every unit has a conversion factor in relation to a base unit (e.g., Meters = 1 for Length). The formula is:
    text

Result = Value * (Target Unit Factor / Source Unit Factor)
Temperature: Temperature conversions are treated in isolation since they include offsets (e.g., Fahrenheit to Celsius involves multiplication and addition). An isolated function controls these calculations.
