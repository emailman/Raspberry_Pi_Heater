from guizero import App, Text, TextBox, PushButton


def pushed():
    txt2.set("Welcome " + tbx1.get())
    tbx1.set("")


window1 = App("Simple Form")
txt1 = Text(window1, "Enter your name below")
tbx1 = TextBox(window1)
pb1 = PushButton(window1, text="Push for greeting",
                 command=pushed)
txt2 = Text(window1)


window1.display()
