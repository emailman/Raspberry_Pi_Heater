from guizero import App, Slider, Text
from math import sqrt

# Global variable
txt_answer = None


def slider_moved(value):
    global txt_answer
    print(value)
    txt_answer.value = round(sqrt(float(value)), 10)


def main():
    global txt_answer

    window = App(title="Square Root Calculator", height=100)

    Slider(window, horizontal=True, end=256, command=slider_moved)

    txt_answer = Text(window, size=16, text_color="blue")

    window.display()


main()
