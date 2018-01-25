from guizero import App, Text, TextBox, PushButton


def calc():
    try:
        score = float((tbxScore.get()))
        if 0 <= score <= 100:
            txtError.set("")
            if score < 75:
                txtGrade.set("F")
            elif score < 83:
                txtGrade.set("C")
            elif score < 92:
                txtGrade.set("B")
            else:
                txtGrade.set("A")
        else:
            txtError.set("Score is out of range 0 - 100")
    except ValueError:
        txtError.set("Score is missing or non-numeric")


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
                align="left", grid=[7, 3])

window1.display()
