from guizero import App, Text, TextBox, PushButton


def pushed():
    length = float(tbxLength.get())
    width = float(tbxWidth.get())

    area = length * width
    perimeter = 2 * (length + width)

    tbxArea.set(str(area))
    tbxPerimeter.set(perimeter)


window1 = App("Rectangle Calculator",
              layout="grid",
              width=325, height=300)

txtFill = Text(window1, text="        ", grid=[0, 0])

txt1 = Text(window1, "Length", grid=[1, 1])
tbxLength = TextBox(window1, grid=[1, 2])
txtFill1 = Text(window1, grid=[2, 0])

txt2 = Text(window1, "Width", grid=[3, 1])
tbxWidth = TextBox(window1, grid=[3, 2])
txtFill2 = Text(window1, grid=[4, 0])

pb1 = PushButton(window1, text="Calculate",
                 command=pushed, grid=[5, 2])

txt3 = Text(window1, "Area", grid=[7, 1])
tbxArea = TextBox(window1, grid=[7, 2])
txtFill3 = Text(window1, grid=[8, 0])

txt4 = Text(window1, "Perimeter", grid=[9, 1])
tbxPerimeter = TextBox(window1, grid=[9, 2])
txtFill4 = Text(window1, grid=[6, 0])

window1.display()
