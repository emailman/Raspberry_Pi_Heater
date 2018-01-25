from gpiozero import *

led1 = LED(17)
time_factor = .5


def blink_dot():
    led1.blink(on_time=time_factor,
               off_time=time_factor,
               n=1, background=False)


def blink_dash():
    led1.blink(on_time=time_factor * 3,
               off_time=time_factor,
               n=1, background=False)


def letter_separator():
    led1.blink(on_time=0,
               off_time=time_factor * 2,
               n=1, background=False)


def word_separator():
    led1.blink(on_time=0,
               off_time=time_factor * 4,
               n=1, background=False)


# A = dot dash
blink_dot()
blink_dash()
letter_separator()

# B = dash dot dot dot
blink_dash()
blink_dot()
blink_dot()
blink_dot()
letter_separator()
word_separator()

print("Done")
