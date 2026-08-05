from data import exercises

def generate_cardio_workout(intensity="beginner", cardio_exercises=None):
    if cardio_exercises is None:
        cardio_exercises = []

    workout = []

    target_duration = {
        "beginner": 30,
        "intermediate": 45,
        "expert": 60
    }

    total_duration = 0

    while total_duration < target_duration[intensity]:

        for exercise in cardio_exercises:

            if total_duration >= target_duration[intensity]:
                break

            single_exercise = {
                "name": exercise["name"],
                "goal": exercise["goal"],
                "intensity": exercise["intensity"][intensity],
                "needs_gym": exercise["needs_gym"],
            }

            workout.append(single_exercise)

            total_duration += single_exercise["intensity"]["duration"]

    return workout

def generate_strength_workout(intensity, strength_exercises=None):
    if strength_exercises is None:
        strength_exercises = []

    if not strength_exercises:
        return []

    workout = []

    target_sets = {
        "beginner": 25,
        'intermediate': 40,
        'expert': 50
    }

    total_sets = 0

    while total_sets < target_sets[intensity]:
        for exercise in strength_exercises:
            if total_sets >= target_sets[intensity]:
                break
            single_exercise = {
                "name": exercise["name"],
                "goal": exercise["goal"],
                "intensity": exercise["intensity"][intensity],
                "needs_gym": exercise["needs_gym"],
            }

            workout.append(single_exercise)

            total_sets += single_exercise["intensity"]["sets"]
    return workout

def generate_workout(type_of, intensity):
    type_exercises = []

    for exercise in exercises:
        if exercise["type"] == type_of:
            type_exercises.append(exercise)

    if type_of == "cardio":
        workout = generate_cardio_workout(intensity, type_exercises)
    elif type_of == "strength":
        workout = generate_strength_workout(intensity, type_exercises)
    else:
        return []

    return workout

def print_workout(workout):
    print("\n" + "=" * 40)
    print("        YOUR WORKOUT PLAN")
    print("=" * 40)

    for number, exercise in enumerate(workout, start=1):
        print(f"\n{number}. {exercise['name']}")

        if "duration" in exercise["intensity"]:
            print(
                f"   Duration : {exercise['intensity']['duration']} "
                f"{exercise['intensity']['unit']}"
            )
        else:
            print(f"   Sets     : {exercise['intensity']['sets']}")
            print(f"   Reps     : {exercise['intensity']['reps']}")

        print(f"   Gym      : {'Yes' if exercise['needs_gym'] else 'No'}")

    print("\n" + "=" * 40)