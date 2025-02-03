import tkinter as tk
from tkinter import messagebox

# File to store BMI history
HISTORY_FILE = "bmi_history.txt"

def save_bmi_history(weight, height, bmi, category):
    """Save BMI details in a file."""
    with open(HISTORY_FILE, "a") as file:
        file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}, Category: {category}\n")

def calculate_bmi(weight, height):
    """Calculate BMI and return result with category."""
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category

def on_calculate():
    """Handle button click to calculate BMI."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        # Convert height from cm to meters if necessary
        if height > 3:  
            height = height / 100  # Convert cm to meters
        
        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and height must be positive numbers.")
            return

        bmi, category = calculate_bmi(weight, height)
        result_label.config(text=f"Your BMI: {bmi:.2f}\nCategory: {category}")

        # Save to history
        save_bmi_history(weight, height, bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# Create GUI window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x300")
root.configure(bg="#f2f2f2")

# Labels and input fields
tk.Label(root, text="Enter Weight (kg):", bg="#f2f2f2").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack(pady=5)

tk.Label(root, text="Enter Height (cm or m):", bg="#f2f2f2").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack(pady=5)

# Calculate button
calc_button = tk.Button(root, text="Calculate BMI", command=on_calculate, bg="#4CAF50", fg="white", padx=10, pady=5)
calc_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f2f2f2", fg="#333")
result_label.pack(pady=10)

# Run the application
root.mainloop()
