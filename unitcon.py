import tkinter as tk
from tkinter import ttk

# Conversion functions
def cm_to_feet(cm):
    return cm / 30.48

def feet_to_inches(feet):
    return feet * 12

def sqft_to_sqm(sqft):
    return sqft * 0.092903

def sqft_to_hectares(sqft):
    return sqft * 0.0000092903

def sqft_to_acres(sqft):
    return sqft * 0.00002296

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

# Create the main window
root = tk.Tk()
root.title("Unit Conversion")
root.geometry("400x450")  # Set the window size

# Set background color for the entire window
root.configure(bg="lightblue")

# Create input label and entry
input_label = tk.Label(root, text="Enter Value:", font=("Arial", 12), bg="lightblue")
input_label.pack()

value_entry = tk.Entry(root, font=("Arial", 12))
value_entry.pack()

# Create "From" unit label and combo box
from_unit_label = tk.Label(root, text="From Unit:", font=("Arial", 12), bg="lightblue")
from_unit_label.pack()

from_unit_combo = ttk.Combobox(root, values=["Centimeter", "Feet", "Square Feet", "Kilograms", "Pounds", "Celsius", "Kelvin"], font=("Arial", 12))
from_unit_combo.set("Centimeter")
from_unit_combo.pack()

# Create "To" unit label and combo box
to_unit_label = tk.Label(root, text="To Unit:", font=("Arial", 12), bg="lightblue")
to_unit_label.pack()

to_unit_combo = ttk.Combobox(root, values=["Feet", "Inches", "Square Meters", "Hectares", "Acres", "Pounds", "Kilograms", "Kelvin", "Celsius"], font=("Arial", 12))
to_unit_combo.set("Feet")
to_unit_combo.pack()

# Create result label
result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightblue")
result_label.pack()

# Conversion function
def convert():
    from_unit = from_unit_combo.get()
    to_unit = to_unit_combo.get()
    value = float(value_entry.get())
    result = ""

    if from_unit == to_unit:
        result = "Units must be different for conversion."
    elif from_unit == "Centimeter" and to_unit == "Feet":
        result = f"{value} cm is {cm_to_feet(value):.2f} feet."
    elif from_unit == "Feet" and to_unit == "Inches":
        result = f"{value} feet is {feet_to_inches(value):.2f} inches."
    elif from_unit == "Square Feet" and to_unit == "Square Meters":
        result = f"{value} sqft is {sqft_to_sqm(value):.2f} square meters."
    elif from_unit == "Square Feet" and to_unit == "Hectares":
        result = f"{value} sqft is {sqft_to_hectares(value):.6f} hectares."
    elif from_unit == "Square Feet" and to_unit == "Acres":
        result = f"{value} sqft is {sqft_to_acres(value):.6f} acres."
    elif from_unit == "Kilograms" and to_unit == "Pounds":
        result = f"{value} kg is {kg_to_pounds(value):.2f} pounds."
    elif from_unit == "Pounds" and to_unit == "Kilograms":
        result = f"{value} pounds is {pounds_to_kg(value):.2f} kg."
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        result = f"{value} °C is {celsius_to_kelvin(value):.2f} K."
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        result = f"{value} K is {kelvin_to_celsius(value):.2f} °C."
    else:
        result = "Invalid Conversion"

    result_label.config(text=result)

# Create the conversion button
convert_button = tk.Button(root, text="Convert", command=convert, font=("Arial", 14), bg="blue", fg="white")
convert_button.pack()

# Start the GUI main loop
root.mainloop()
