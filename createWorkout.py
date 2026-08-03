from data import exercises

def generate_workout(goal, intensity):
    workout = []

    for i in exercises:
        if i['goal'] == goal:
            single_exercise = {"name": i['name'], 'goal': i['goal'], "intensity": i['intensity'][intensity], "needsGym": i['needsGym']}
            workout.append(single_exercise)
    print('-------------- Exercises -------------------')
    for exercise in workout:
        print(f"Exercise : {exercise['name']}")
        # print(f"Goal     : {exercise['goal']}")
        print(f"Intensity: {exercise['intensity']}")
        # print(f"Gym      : {'Yes' if exercise['needsGym'] else 'No'}")
        print("-" * 30)