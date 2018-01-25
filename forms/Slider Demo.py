from guizero import App, Text, Slider, PushButton


def control():
    print()
    print("Room Temperature", sldRoomTemperature.get())
    print("Desired Temperature", sldDesiredTemperature.get())
    print("Deadband", sldDeadBand.get())


def handler(value):
    print(value)
    control()


window = App(title="Temperature Control",
             height=320, width=320, layout="grid")

Text(window, text="   ", grid=[0, 0])  # Filler

Text(window, text="\nRoom Temperature: ",
     align="right", grid=[1, 1])
sldRoomTemperature = Slider(window, command=handler,
                            start=50, end=100, grid=[1, 2])

Text(window, grid=[2, 0])  # Filler

Text(window, text="\nDesired Temperature: ",
     align="right", grid=[3, 1])
sldDesiredTemperature = Slider(window, command=handler,
                               start=65, end=80, grid=[3, 2])

Text(window, grid=[4, 0])  # Filler

Text(window, text="\nDead Band: ",
     align="right", grid=[5, 1])
sldDeadBand = Slider(window, command=handler,
                     start=0, end=2, grid=[5, 2])

Text(window, size=20, grid=[6, 0])  # Filler

Text(window, text="Action: ", align="right", grid=[7, 1])
txtAction = Text(window, grid=[7, 2])

Text(window, grid=[8, 0])  # Filler

PushButton(window, text="QUIT", command=quit, grid=[9,2])

# Initial conditions
sldRoomTemperature.set(75)
sldDesiredTemperature.set(75)
sldDeadBand.set(1)

window.display()
