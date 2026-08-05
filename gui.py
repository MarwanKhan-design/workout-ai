from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PySide6.QtWidgets import QApplication, QWidget


def show_gui(workout):
    app = QApplication([])

    window = QWidget()
    window.setWindowTitle("Workout Generator")
    window.resize(800, 600)

    title = QLabel('<h1>Workout Generator</h1>')
    layout = QVBoxLayout(window)
    layout.addWidget(title)

    for exercise in workout:

        if "duration" in exercise["intensity"]:
            exercise_label = QLabel(
                f"""
                {exercise['name']}
                Duration: {exercise['intensity']['duration']} {exercise['intensity']['unit']}
                Gym: {"Yes" if exercise['needs_gym'] else "No"}
                """
            )
            layout.addWidget(exercise_label)


        elif "sets" in exercise["intensity"]:
            exercise_label = QLabel(
                f"""
                {exercise['name']}
                Sets: {exercise['intensity']['sets']}
                Reps: {exercise['intensity']['reps']}
                Gym: {"Yes" if exercise['needs_gym'] else "No"}
                """
            )

            layout.addWidget(exercise_label)






    window.show()

    app.exec()