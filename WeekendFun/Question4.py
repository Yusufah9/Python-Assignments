# 1. Ask the user for weight and height
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# 2. Compute BMI
bmi = weight / (height * height)

# 3. Determine and print the BMI category
if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")

