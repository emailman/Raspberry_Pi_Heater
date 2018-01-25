from guizero import *
from math import pi

# Global variables
tbx_diameter = txt_area = txt_circumference = None


# Model
def calc_circle(diameter):
    radius = diameter / 2
    area = pi * radius ** 2
    circumference = pi * diameter
    return area, circumference


# Controller
def btn_calc_click():
    try:
        c_diameter = float(tbx_diameter.get())
        c_area, c_circumference = calc_circle(c_diameter)
        txt_area.set(c_area)
        txt_circumference.set(c_circumference)

    except ValueError:
        pass


# View
def main():
    global tbx_diameter, txt_area, txt_circumference
    window = App(layout="grid")
    Text(window, text="   ", grid=[0, 0])

    Text(window, text="Diameter", grid=[1, 1])
    tbx_diameter = TextBox(window, grid=[1, 2])

    Text(window, text="Area", grid=[3, 1])
    txt_area = Text(window, grid=[3, 2])

    Text(window, text="Circumference", grid=[5, 1])
    txt_circumference = Text(window, grid=[5, 2])

    PushButton(window, text="CALC",
               command=btn_calc_click,
               grid=[7, 1])

    PushButton(window, text="CLEAR", command=None,
               grid=[7, 2])

    PushButton(window, text="QUIT", command=quit,
               grid=[7, 3])

    window.display()


main()
