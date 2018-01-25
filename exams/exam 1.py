from guizero import App, Text, TextBox, PushButton


def compare():
    if int(tbxOne.get()) > int(tbxTwo.get()):
        txtLarger.set(tbxOne.get())
        txtSmaller.set(tbxTwo.get())
    else:
        txtLarger.set(tbxTwo.get())
        txtSmaller.set(tbxOne.get())


window = App(title="Comparator", width=450, height=350,
             layout="grid")

Text(window, text="     ", grid=[0, 0])  # Spacer

Text(window, text="Enter an integer ", align="right",
     grid=[1, 1])
tbxOne = TextBox(window, grid=[1, 2])

Text(window, grid=[2, 0])  # Spacer

Text(window, text="Enter another integer ", align="right",
     grid=[3, 1])
tbxTwo = TextBox(window, grid=[3, 2])

Text(window, grid=[4, 0])  # Spacer

PushButton(window, text="COMPARE", command=compare,
           grid=[5, 2])

Text(window, grid=[6, 0])  # Spacer

Text(window, text="Larger Number ", align="right",
     grid=[7, 1])
txtLarger = Text(window, grid=[7, 2])

Text(window, grid=[8, 0])  # Spacer

Text(window, text="Smaller Number ", align="right",
     grid=[9, 1])
txtSmaller = Text(window, grid=[9, 2])

Text(window, grid=[10, 0])  # Spacer

PushButton(window, text=" QUIT ", command=quit,
           grid=[11, 2])

Text(window, grid=[12, 0])  # Spacer

txtError = Text(window, text="Error Message", color="red",
                grid=[13, 3])

window.display()
