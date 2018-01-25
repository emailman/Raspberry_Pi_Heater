from guizero import App, Text, TextBox, PushButton


def pushed():
    txt2.set("Welcome " + tbx1.get())
    tbx1.set("")


window1 = App("Simple Form",
              layout="grid",
              width=300, height=200)

txtFill1 = Text(window1, text="        ", grid=[0, 0])

txt1 = Text(window1, "Enter your name", grid=[1, 1])
tbx1 = TextBox(window1, grid=[1, 2])

txtFill2 = Text(window1, grid=[2, 0])

pb1 = PushButton(window1, text="Push for greeting",
                 command=pushed, grid=[3, 1])
txt2 = Text(window1, grid=[3, 2])


window1.display()
