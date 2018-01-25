from guizero import App, Text, TextBox, PushButton


def calc():
    try:
        if tbxNumber.get() != "":
            number = int(tbxNumber.get())
            output = number * 2
            txtOutput.set(str(number) + " doubled is " + str(output))
            tbxNumber.set("")
        else:
            txtOutput.set("Error: No number entered")
    except ValueError:
        txtOutput.set("Error: Invalid number entered")


window1 = App("Doubler",
              height=180, width=340,
              layout="grid")

Text(window1, "    ", grid=[0, 0])  # Spacer

Text(window1, " Enter a number ", grid=[1, 1])

tbxNumber = TextBox(window1, grid=[1, 2], align="left")

Text(window1, grid=[2, 0])  # Spacer

PushButton(window1, text="Click to Double",
           command=calc, grid=[3, 1])

txtOutput = Text(window1, grid=[3, 2])

Text(window1, grid=[4, 0])  # Spacer

PushButton(window1, text="  Exit  ",
           command=quit, grid=[5, 1])

window1.display()
