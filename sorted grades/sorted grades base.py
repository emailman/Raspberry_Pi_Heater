from guizero import *

# Global variables
txtWidgets = []
tbxWidgets = []
tbxValues = []

txt_lowest = txt_highest = txt_average = None


def calc():
    global tbxValues

    # Clear the list of values
    tbxValues = []

    # Build a list of values from the text boxes
    for each in tbxWidgets:
        value = each.get()
        if value != "":
            try:
                tbxValues.append(float(value))
            except ValueError:
                error(title="Input Error",
                      text="Non-numerical value" +
                      " found and ignored")
    display()


def display():
    if len(tbxValues) != 0:
        # Sort the values
        tbxValues.sort(reverse=True)

        # Load the sorted list into the text widgets
        load_values(tbxValues)

        # Show the lowest value
        txt_lowest.set(min(tbxValues))

        # Show the highest value
        txt_highest.set(max(tbxValues))

        # Show the lowest value
        txt_lowest.set(min(tbxValues))

        # Show the average value
        average = sum(tbxValues) / len(tbxValues)
        txt_average.set(round(average, 1))


def load_values(values):
    # Clear the text widgets
    clear_text_widgets()

    # Show each value in the list
    for i in range(len(values)):
        txtWidgets[i].set(values[i])

        if values[i] < 75:
            txtWidgets[i].color("Red")
        else:
            txtWidgets[i].color("Green")


def clear():
    clear_text_widgets()
    clear_textbox_widgets()


def clear_text_widgets():
    for each in txtWidgets:
        each.clear()


def clear_textbox_widgets():
    for each in tbxWidgets:
        each.clear()


def main():
    global tbxWidgets, txtWidgets
    global txt_lowest, txt_highest, txt_average

    window = App(title="Grade Analysis", height=470, width=300, layout="grid")

    Text(window, text="  ", grid=[0, 0])  # spacer
    Text(window, text="Enter Grades", grid=[0, 2])
    Text(window, text=" Sorted Grades", grid=[0, 3])

    Text(window, text="Grade 1", grid=[1, 1])
    tbx_grade1 = TextBox(window, grid=[1, 2])
    txt_sort1 = Text(window, text="txt 1", grid=[1, 3])

    Text(window, grid=[2, 0])  # spacer

    Text(window, text="Grade 2", grid=[3, 1])
    tbx_grade2 = TextBox(window, grid=[3, 2])
    txt_sort2 = Text(window, text="txt 2", grid=[3, 3])

    Text(window, grid=[4, 0])  # spacer

    Text(window, text="Grade 3", grid=[5, 1])
    tbx_grade3 = TextBox(window, grid=[5, 2])
    txt_sort3 = Text(window, text="txt 3", grid=[5, 3])

    Text(window, grid=[6, 0])  # spacer

    Text(window, text="Grade 4", grid=[7, 1])
    tbx_grade4 = TextBox(window, grid=[7, 2])
    txt_sort4 = Text(window, text="txt 4", grid=[7, 3])

    Text(window, grid=[8, 0])  # spacer

    Text(window, text="Grade 5", grid=[9, 1])
    tbx_grade5 = TextBox(window, grid=[9, 2])
    txt_sort5 = Text(window, text="txt 5", grid=[9, 3])

    Text(window, size=18, grid=[10, 0])  # spacer

    Text(window, text="Lowest", grid=[11, 2])
    txt_lowest = Text(window, text="txt low", grid=[11, 3])

    Text(window, grid=[12, 0])  # spacer

    Text(window, text="Highest", grid=[13, 2])
    txt_highest = Text(window, text="txt high", grid=[13, 3])

    Text(window, grid=[14, 0])  # spacer

    Text(window, text="Average", grid=[15, 2])
    txt_average = Text(window, text="txt aver", grid=[15, 3])

    Text(window, grid=[16, 0])  # spacer

    PushButton(window, text="  CALC  ", align="left",
               command=calc, grid=(17, 1))
    PushButton(window, text=" CLEAR ", align="right",
               command=clear, grid=(17, 2))
    PushButton(window, text="  QUIT  ", align="right",
               command=quit, grid=(17, 3))

    # Create a list of textbox widgets
    tbxWidgets = [tbx_grade1, tbx_grade2, tbx_grade3,
                  tbx_grade4, tbx_grade5]

    # Create a list of text widgets
    txtWidgets = [txt_sort1, txt_sort2, txt_sort3,
                  txt_sort4, txt_sort5,
                  txt_lowest, txt_highest, txt_average]

    window.display()


main()
