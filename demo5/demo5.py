from guizero import App, Text, Slider


def cruise(speed):
    # "speed" holds the value of the slider
    txtSpeed.set("Speed set to " + speed + " mph")


window = App(title="Slider Demo",
             width=270, height=150,
             layout="grid")

Text(window, text="   ", grid=[0, 0])  # filler

Text(window, text="\nSet Speed  ", grid=[1, 1])
Slider(window, start=0, end=75, command=cruise,
       grid=[1, 2], align="left")

Text(window, text="   ", grid=[2, 0])  # filler

txtSpeed = Text(window, grid=[3, 2], align="left")
txtSpeed.set("Speed set to 0 mph")

window.display()
