from guizero import App, Text, TextBox, PushButton


def hello():
    if tbxEnterNameField.get() != "":
        txtGreetingOutput.set("Hello " + tbxEnterNameField.get())
        tbxEnterNameField.set("")
    else:
        txtGreetingOutput.set("You forgot to enter a name")


window1 = App("Form  1",
              height=150, width=340,
              layout="grid")

Text(window1, "    ", grid=[0, 0])  # Spacer

Text(window1, "Enter your name", grid=[1, 1])

tbxEnterNameField = TextBox(window1, grid=[1, 2], align="left")

Text(window1, grid=[2, 0])  # Spacer

PushButton(window1, text="Click for Greeting",
           command=hello, grid=[3, 1])

txtGreetingOutput = Text(window1, grid=[3, 2])

window1.display()
