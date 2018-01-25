# Exam 1
# CIS 120 4L3
# Professor Eric Mailman
# Submission from Ryszard S. Bialach II
# Objective: compare two ints from a gui form and display error
# if one occurs

from guizero import App, Text, TextBox, PushButton


def calc():
    try:
        if One_tb.get() and Two_tb.get() != "":
            q = int(One_tb.get())
            w = int(Two_tb.get())
            if q > w:
                l_txt.set(q)
                s_txt.set(w)
            else:
                s_txt.set(q)
                l_txt.set(w)
        else:
            pass
    except ValueError:
        e_txt.set("Error Received")


# Create a window outline
window1 = App("Comparator", width=400, height=400,
              layout="grid")
# Create Text Fields
# spacer
Text(window1, "", grid=[1, 0])
# get integer 1
Text(window1, "Enter an Integer", grid=[2, 1])
One_tb = TextBox(window1, grid=[2, 2])
# spacer
Text(window1, grid=[3, 0])
# get integer 2
Text(window1, "Enter another Integer", grid=[4, 1])
Two_tb = TextBox(window1, "", grid=[4, 2])
# spacer
Text(window1, "", grid=[5, 0])
# command compare pushbutton
Text(window1, "", grid=[6, 1])
PushButton(window1, text="COMPARE", grid=[6, 2], command=calc)
# spacer
Text(window1, "", grid=[7, 1])
# text fields for larger number
Text(window1, "Larger Number", grid=[8, 1])
l_txt = Text(window1, "", grid=[8, 2])
# spacer
Text(window1, "", grid=[9, 0])
# Text fields for smaller number
Text(window1, "Smaller Number", grid=[10, 1])
s_txt = Text(window1, "", grid=[10, 2])
# Exit or quit button
Text(window1, "", grid=[12, 1])
PushButton(window1, text="QUIT", grid=[12, 2], command=quit)
# Error message field
e_txt = Text(window1, "", grid=[14, 9], align="Right", color="Red")

# display window
window1.display()
