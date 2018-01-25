from time import sleep

from gpiozero import LED

led = LED(pin=17)

while True:
    led.on()
    print("on")
    sleep(4)

    led.off()
    print("off")
    sleep(4)
