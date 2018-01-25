from guizero import *

# Global variables
dictFinishNamesTimes = {}
tbxTime1 = tbxTime2 = tbxTime3 = tbxTime4 = tbxTime5 = TextBox
tbxName1 = tbxName2 = tbxName3 = tbxName4 = tbxName5 = TextBox
txtFastestName = txtFastestTime = txtNumFinished = None


# Push button CALC event handler
def calc():
    # Start with an empty dictionary
    dictFinishNamesTimes.clear()

    build_dict(tbxName1, tbxTime1)
    build_dict(tbxName2, tbxTime2)
    build_dict(tbxName3, tbxTime3)
    build_dict(tbxName4, tbxTime4)
    build_dict(tbxName5, tbxTime5)
    print(dictFinishNamesTimes)

    # If the dictionary is empty, don't display any results
    if len(dictFinishNamesTimes) != 0:
        txtFastestName.set(min(dictFinishNamesTimes,
                               key=dictFinishNamesTimes.get))
        txtFastestTime.set(min(dictFinishNamesTimes.values()))
        txtNumFinished.set(len(dictFinishNamesTimes))


# Function to build the list of finish times
def build_dict(finish_name, finish_time):
    try:
        time = float(finish_time.get())
        name = finish_name.get()
        dictFinishNamesTimes[name] = time
    except ValueError:
        finish_time.set("")


# Push Button CLEAR event handler to clear the form
def clear():
    global tbxTime1, tbxTime2, tbxTime3, tbxTime4, tbxTime5
    global tbxName1, tbxName2, tbxName3, tbxName4, tbxName5
    global txtFastestTime, txtFastestName, txtNumFinished

    dictFinishNamesTimes.clear()
    tbxTime1.focus()

    tbxTime1.clear()
    tbxTime2.clear()
    tbxTime3.clear()
    tbxTime4.clear()
    tbxTime5.clear()

    tbxName1.clear()
    tbxName2.clear()
    tbxName3.clear()
    tbxName4.clear()
    tbxName5.clear()

    txtFastestName.set("")
    txtFastestTime.set("")
    txtNumFinished.set("")


def main():
    global tbxTime1, tbxTime2, tbxTime3, tbxTime4, tbxTime5
    global tbxName1, tbxName2, tbxName3, tbxName4, tbxName5
    global txtFastestTime, txtFastestName, txtNumFinished

    window = App(title="Off to the Races",
                 width=450, height=450,
                 layout="grid")

    Text(window, grid=[0, 0])  # Spacer

    Text(window, text="Name", grid=[0, 2])
    Text(window, text="    Time    ", grid=[0, 3])

    Text(window, text="Horse 1 ", grid=[1, 1])
    tbxName1 = TextBox(window, grid=[1, 2])
    tbxTime1 = TextBox(window, grid=[1, 3])

    Text(window, grid=[2, 0])  # Spacer

    Text(window, text="Horse 2 ", grid=[3, 1])
    tbxName2 = TextBox(window, grid=[3, 2])
    tbxTime2 = TextBox(window, grid=[3, 3])

    Text(window, grid=[4, 0])  # Spacer

    Text(window, text="Horse 3 ", grid=[5, 1])
    tbxName3 = TextBox(window, grid=[5, 2])
    tbxTime3 = TextBox(window, grid=[5, 3])

    Text(window, grid=[6, 0])  # Spacer

    Text(window, text="Horse 4 ", grid=[7, 1])
    tbxName4 = TextBox(window, grid=[7, 2])
    tbxTime4 = TextBox(window, grid=[7, 3])

    Text(window, grid=[8, 0])  # Spacer

    Text(window, text="Horse 5 ", grid=[9, 1])
    tbxName5 = TextBox(window, grid=[9, 2])
    tbxTime5 = TextBox(window, grid=[9, 3])

    Text(window, grid=[10, 0])  # Spacer

    Text(window, text="Winner ", grid=[11, 1])
    txtFastestName = Text(window, grid=[11, 2])

    Text(window, grid=[12, 0])  # Spacer

    Text(window, text="Winning Time ", grid=[13, 1])
    txtFastestTime = Text(window, grid=[13, 2])

    Text(window, grid=[14, 0])  # Spacer

    Text(window, text="Finished ", grid=[15, 1])
    txtNumFinished = Text(window, grid=[15, 2])

    # Text(window, grid=[16, 0])  # Spacer

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
