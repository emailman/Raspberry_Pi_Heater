from time import sleep

from gpiozero import *

led = PWMOutputDevice(pin=27)
led.frequency = 800

while True:
    led.value = .5
    print("on")
    sleep(4)

    led.off()
    print("off")
    sleep(4)
