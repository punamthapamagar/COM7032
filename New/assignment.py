import tkinter as tk
from tkinter import messagebox
from owlready2 import *

# Load ontology
onto_path.append(r"C:\Users\Lenovo\Desktop\New\GeometryOntology.owl")
onto = get_ontology(r"C:\Users\Lenovo\Desktop\New\GeometryOntology.owl").load()

def calculate_area(shape_name, measurements):
    shape = onto.search_one(iri=f"*{shape_name}")
    
    if shape is None:
        return None
    
    # Get measurements based on shape type
    if shape_name == "Circle":
        radius = measurements['radius']
        area_value = round(3.14 * radius * radius, 2)
        return area_value
    
    elif shape_name == "Rectangle":
        length = measurements['length']
        width = measurements['width']
        area_value = length * width
        return area_value
    
    elif shape_name == "Triangle":
        base = measurements['base']
        height = measurements['height']
        area_value = (base * height) / 2
        return area_value

def show_area():
    shape_name = shape_var.get()
    measurements = {}
    
    # Gather input based on selected shape
    if shape_name == "Circle":
        try:
            radius = float(radius_entry.get())
            measurements['radius'] = radius
            area_value = calculate_area("Circle", measurements)
            result_label.config(text=f"The area of the circle is {area_value}.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for radius.")
    
    elif shape_name == "Rectangle":
        try:
            length = float(length_entry.get())
            width = float(width_entry.get())
            measurements['length'] = length
            measurements['width'] = width
            area_value = calculate_area("Rectangle", measurements)
            result_label.config(text=f"The area of the rectangle is {area_value}.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for length and width.")
    
    elif shape_name == "Triangle":
        try:
            base = float(base_entry.get())
            height = float(height_entry.get())
            measurements['base'] = base
            measurements['height'] = height
            area_value = calculate_area("Triangle", measurements)
            result_label.config(text=f"The area of the triangle is {area_value}.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers for base and height.")

# Set up GUI
root = tk.Tk()
root.title("Area Calculator")
root.geometry("500x600")  # Increased width and height to accommodate all elements
root.config(bg="#e3f2fd")

# Header
header_label = tk.Label(root, text="Area Calculator", font=("Arial", 20, "bold"), bg="#42a5f5", fg="white", padx=10, pady=10, relief="groove")
header_label.pack(pady=10, fill="x")

# Frame for shape selection
shape_frame = tk.Frame(root, bg="#bbdefb", padx=10, pady=10, relief="groove", bd=2)
shape_frame.pack(pady=10, fill="x")

shape_var = tk.StringVar(value="Circle")  # Default selection

shape_label = tk.Label(shape_frame, text="Select Shape:", font=("Arial", 14, "bold"), bg="#bbdefb", fg="#1e88e5")
shape_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

circle_radio = tk.Radiobutton(shape_frame, text="Circle", variable=shape_var, value="Circle", font=("Arial", 12), bg="#bbdefb", activebackground="#90caf9", command=lambda: show_inputs("Circle"))
circle_radio.grid(row=0, column=1, sticky="w", padx=10)

rectangle_radio = tk.Radiobutton(shape_frame, text="Rectangle", variable=shape_var, value="Rectangle", font=("Arial", 12), bg="#bbdefb", activebackground="#90caf9", command=lambda: show_inputs("Rectangle"))
rectangle_radio.grid(row=0, column=2, sticky="w", padx=10)

triangle_radio = tk.Radiobutton(shape_frame, text="Triangle", variable=shape_var, value="Triangle", font=("Arial", 12), bg="#bbdefb", activebackground="#90caf9", command=lambda: show_inputs("Triangle"))
triangle_radio.grid(row=0, column=3, sticky="w", padx=10)

# Frame for input fields
input_frame = tk.Frame(root, bg="#e3f2fd")
input_frame.pack(pady=20)

radius_label = tk.Label(input_frame, text="Radius:", font=("Arial", 12), bg="#e3f2fd")
radius_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#f1f8e9", relief="groove")

length_label = tk.Label(input_frame, text="Length:", font=("Arial", 12), bg="#e3f2fd")
length_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#f1f8e9", relief="groove")

width_label = tk.Label(input_frame, text="Width:", font=("Arial", 12), bg="#e3f2fd")
width_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#f1f8e9", relief="groove")

base_label = tk.Label(input_frame, text="Base:", font=("Arial", 12), bg="#e3f2fd")
base_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#f1f8e9", relief="groove")

height_label = tk.Label(input_frame, text="Height:", font=("Arial", 12), bg="#e3f2fd")
height_entry = tk.Entry(input_frame, font=("Arial", 12), bg="#f1f8e9", relief="groove")

def show_inputs(shape):
    for widget in input_frame.winfo_children():
        widget.grid_forget()
    
    if shape == "Circle":
        radius_label.grid(row=0, column=0, padx=5, pady=5)
        radius_entry.grid(row=0, column=1, padx=5, pady=5)
    elif shape == "Rectangle":
        length_label.grid(row=0, column=0, padx=5, pady=5)
        length_entry.grid(row=0, column=1, padx=5, pady=5)
        width_label.grid(row=1, column=0, padx=5, pady=5)
        width_entry.grid(row=1, column=1, padx=5, pady=5)
    elif shape == "Triangle":
        base_label.grid(row=0, column=0, padx=5, pady=5)
        base_entry.grid(row=0, column=1, padx=5, pady=5)
        height_label.grid(row=1, column=0, padx=5, pady=5)
        height_entry.grid(row=1, column=1, padx=5, pady=5)

show_inputs("Circle")  # Default inputs

# Calculate button
calculate_button = tk.Button(root, text="Calculate Area", font=("Arial", 14, "bold"), bg="#1e88e5", fg="white", relief="raised", activebackground="#1565c0", command=show_area)
calculate_button.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#e3f2fd", fg="#1e88e5")
result_label.pack(pady=10)

root.mainloop()
