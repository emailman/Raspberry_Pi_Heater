from guizero import App, Text, TextBox, PushButton


def hello():
    print("You clicked the button")
    print("Name entered =", tbx1.get())
    txt2.set("Hello " + tbx1.get())


window1 = App("Form  1",
              height=150, width=250,
              bgcolor="yellow")

txt1 = Text(window1, "Enter your name")
tbx1 = TextBox(window1)
btn1 = PushButton(window1, text="Click for Greeting",
                  command=hello)
txt2 = Text(window1)

window1.display()
