print("=== BMI Calculator ===")

# Get weight
while True:
    try:
        weight = float(input("Enter your weight (kg): "))

        if weight <= 0:
            print("Weight must be greater than 0.\n")
            continue

        break

    except ValueError:
        print("Please enter a valid number.\n")


# Get height
while True:
    try:
        height = float(input("Enter your height (cm): "))

        if height <= 0:
            print("Height must be greater than 0.\n")
            continue

        break

    except ValueError:
        print("Please enter a valid number.\n")


# Convert cm to meters
height = height / 100

# Calculate BMI
bmi = weight / (height ** 2)

# Display BMI
print(f"\nYour BMI is: {bmi:.2f}")

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")