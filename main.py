from createWorkout import generate_workout

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


# Find Intensity
print('''
Are You:
1. Beginner
2. Intermidiate
3. Expert
''')


intensity_num = int(input('Enter Here: '))
intensity = ''

if intensity_num == 1:
    intensity = 'beginner'
elif intensity_num == 2:
    intensity = 'intermediate'
elif intensity_num == 3:
    intensity = 'expert'
else:
    print('Try Again')
    intensity_num = int(input('Enter Here: '))

# Find Goal

print('''
Whats your Goal

1. Gain Muscle
2. Lose Weight

''')

goal_num = int(input('Enter Here: '))
goal = ''

if goal_num == 1:
    goal = 'gain muscle'
elif goal_num == 2:
    goal = 'lose weight'

else:
    print('Try Again')
    goal_num = int(input('Enter Here: '))

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

generate_workout(goal, intensity)

