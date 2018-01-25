from guizero import *

# Global variables
lstFinishTimes = []
tbxTime1 = tbxTime2 = tbxTime3 = tbxTime4 = tbxTime5 = None
txtFastestTime = txtSlowestTime = txtNumFinished = txtAverage = None


# Push button CALC event handler
def calc():
    global lstFinishTimes
    global tbxTime1, tbxTime2, tbxTime3, tbxTime4, tbxTime5
    global txtFastestTime, txtSlowestTime, txtNumFinished, txtAverage

    # Start with an empty list
    lstFinishTimes.clear()

    build_list(tbxTime1)
    build_list(tbxTime2)
    build_list(tbxTime3)
    build_list(tbxTime4)
    build_list(tbxTime5)

    # If the list is empty, don't display any results
    if len(lstFinishTimes) != 0:
        txtSlowestTime.set(max(lstFinishTimes))
        txtFastestTime.set(min(lstFinishTimes))
        txtNumFinished.set(len(lstFinishTimes))
        average = sum(lstFinishTimes) / len(lstFinishTimes)
        txtAverage.set(round(average, 2))


# Function to build the list of finish times
def build_list(finish_time):
    global lstFinishTimes
    try:
        time = float(finish_time.get())
        lstFinishTimes.append(time)
    except ValueError:
        finish_time.set("")


# Push Button CLEAR event handler to clear the form
def clear():
    global lstFinishTimes
    global tbxTime1, tbxTime2, tbxTime3, tbxTime4, tbxTime5
    global txtAverage, txtFastestTime, txtSlowestTime, txtNumFinished

    lstFinishTimes.clear()
    tbxTime1.focus()
    tbxTime1.clear()
    tbxTime2.clear()
    tbxTime3.clear()
    tbxTime4.clear()
    tbxTime5.clear()
    txtSlowestTime.set("")
    txtFastestTime.set("")
    txtNumFinished.set("")
    txtAverage.set("")


def main():
    global tbxTime1, tbxTime2, tbxTime3, tbxTime4, tbxTime5
    global txtAverage, txtFastestTime, txtSlowestTime, txtNumFinished

    window = App(title="Off to the Races",
                 width=450, height=450,
                 layout="grid")

    Text(window, grid=[0, 0])  # Spacer

    Text(window, text="Horse 1 ", grid=[1, 1])
    tbxTime1 = TextBox(window, grid=[1, 2])

    Text(window, grid=[2, 0])  # Spacer

    Text(window, text="Horse 2 ", grid=[3, 1])
    tbxTime2 = TextBox(window, grid=[3, 2])

    Text(window, grid=[4, 0])  # Spacer

    Text(window, text="Horse 3 ", grid=[5, 1])
    tbxTime3 = TextBox(window, grid=[5, 2])

    Text(window, grid=[6, 0])  # Spacer

    Text(window, text="Horse 4 ", grid=[7, 1])
    tbxTime4 = TextBox(window, grid=[7, 2])

    Text(window, grid=[8, 0])  # Spacer

    Text(window, text="Horse 5 ", grid=[9, 1])
    tbxTime5 = TextBox(window, grid=[9, 2])

    Text(window, grid=[10, 0])  # Spacer

    Text(window, text="Fastest Time ", grid=[11, 1])
    txtFastestTime = Text(window, grid=[11, 2])

    Text(window, grid=[12, 0])  # Spacer

    Text(window, text="Slowest Time ", grid=[13, 1])
    txtSlowestTime = Text(window, grid=[13, 2])

    Text(window, grid=[14, 0])  # Spacer

    Text(window, text="Average Time ", grid=[15, 1])
    txtAverage = Text(window, grid=[15, 2])

    Text(window, grid=[16, 0])  # Spacer

    Text(window, text="Finished ", grid=[17, 1])
    txtNumFinished = Text(window, grid=[17, 2])

    PushButton(window, text=" CALC ", command=calc,
               grid=[17, 3])

    Text(window, text="    ", grid=[17, 4])  # Spacer

    PushButton(window, text="CLEAR", command=clear,
               grid=[17, 5])

    Text(window, text="    ", grid=[17, 6])  # Spacer

    PushButton(window, text=" QUIT ", command=quit,
               grid=[17, 7])

    window.display()


main()
