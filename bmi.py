from flask import Flask, render_template, request
app = Flask(__name__)

HISTORY_FILE = "bmi_history.txt"

def save_bmi_history(weight, height, bmi, category):
    with open(HISTORY_FILE, "a") as file:
        file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}, Category: {category}\n")

def calculate_bmi(weight, height):
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

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            if height > 3:  # Convert cm to meters
                height = height / 100

            if weight <= 0 or height <= 0:
                result = "Weight and height must be positive."
            else:
                bmi, category = calculate_bmi(weight, height)
                result = f"Your BMI is {bmi:.2f}. Category: {category}"
                save_bmi_history(weight, height, bmi, category)
        except:
            result = "Please enter valid numbers."

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
