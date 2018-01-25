from signal import pause
from time import sleep
from guizero import App, CheckBox
from gpiozero import Button, LED


def flip():
    cbx1.toggle()
    print("flip")
    sleep(2)
    cbx1.toggle()
    print("flop")


button1 = Button(4)
led1 = LED(17)

app = App("try it")
cbx1 = CheckBox(app, "look here", command=flip)

app.display(c)

while True:
    if button1.is_pressed:
        print("closed")
    else:
        print("open")
    sleep(2)
