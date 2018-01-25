from guizero import App, Text, PushButton
import random


def read_sensor():
    # Simulate readings from 320.0 to 531.0
    return random.randrange(3200, 5310, 10) / 10


def update_label():
    txtUpdateLabel.set(read_sensor())
    # Recursive call
    txtUpdateLabel.after(1000, update_label)


window1 = App(title="Sensor Display",
              height=100,
              width=280,
              layout="grid")

Text(window1, "Sensor Value  =", grid=[1, 1])
txtUpdateLabel = Text(window1, grid=[1, 2])

Text(window1, grid=[2, 1])  # Filler

PushButton(window1, text="QUIT", command=quit, grid=[3, 2])

# Setup an event handler to fire after 1000 milliseconds
txtUpdateLabel.after(1000, update_label)

window1.display()
