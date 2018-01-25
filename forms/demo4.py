from guizero import App, Text, TextBox, PushButton


def calc():
    # Catch a ValueError if the score is not an integer
    try:
        score = int(tbxScore.get())

        # Check for a valid score
        if 0 <= score <= 100:

            txtError.set("")
            # Apply DTCC grading rules
            if score >= 92:
                grade = "A"
            elif score >= 83:
                grade = "B"
            elif score >= 75:
                grade = "C"
            else:
                grade = "F"

            # Display the grade
            txtGrade.set(grade)
        else:
            txtError.set("Score is outside of range 0 - 100")

    except ValueError:
        txtError.set("Score is non-numeric")


window1 = App("Grade Calculator", layout="grid",
              width=400, height=200)

Text(window1, "    ", grid=[0, 0])  # Filler

Text(window1, "Score", grid=[1, 1])
tbxScore = TextBox(window1, grid=[1, 2])

Text(window1, grid=[2, 0])  # Filler

Text(window1, "Grade", grid=[3, 1])
txtGrade = Text(window1, grid=[3, 2])

Text(window1, grid=[4, 0])  # Filler

PushButton(window1, text="CALC", command=calc,
           grid=[5, 1])
PushButton(window1, text="QUIT", command=quit,
           grid=[5, 2])

Text(window1, grid=[6, 0])  # Filler

txtError = Text(window1, color="red",
                grid=[7, 3])

window1.display()
