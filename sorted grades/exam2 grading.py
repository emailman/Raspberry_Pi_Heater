from guizero import *

# Global variables
lstGradeList = []
lstSortList = []
tbxGrade1 = tbxGrade2 = tbxGrade3 = tbxGrade4 = tbxGrade5 = None
Grade1 = Grade2 = Grade3 = Grade4 = Grade5 = None
txtSort1 = txtSort2 = txtSort3 = txtSort4 = txtSort5 = None
txtLowestGrade = txtHighestGrade = txtAverageGrade = None


# Push button CALC event handler
def calc():
    global lstGradeList
    global lstSortList
    global tbxGrade1, tbxGrade2, tbxGrade3, tbxGrade4, tbxGrade5
    global txtSort1, txtSort2, txtSort3, txtSort4, txtSort5
    global txtLowestGrade, txtHighestGrade, txtAverageGrade
    global Grade1, Grade2, Grade3, Grade4, Grade5

    lstSortList.clear()
    lstGradeList.clear()
    Grade1 = float(tbxGrade1.get())
    Grade2 = float(tbxGrade2.get())
    Grade3 = float(tbxGrade3.get())
    Grade4 = float(tbxGrade4.get())
    Grade5 = float(tbxGrade5.get())

    for sortOne in [Grade1, Grade2, Grade3, Grade4, Grade5]:
        lstGradeList.append(sortOne)
        lstSortList.append(sortOne)

    max_value = max(lstSortList)
    min_value = min(lstSortList)

    # Checks if the GradeList has something in it and if so, gives output
    if len(lstGradeList) != 0:
        txtLowestGrade.set(min_value)
        txtHighestGrade.set(max_value)
        txtAverageGrade.set(Grade1 + Grade2 + Grade3 + Grade4 + Grade5) / len(lstGradeList)


# Push Button CLEAR event handler to clear the form
def clear():
    global lstGradeList
    global tbxGrade1, tbxGrade2, tbxGrade3, tbxGrade4, tbxGrade5
    global txtSort1, txtSort2, txtSort3, txtSort4, txtSort5
    global txtLowestGrade, txtHighestGrade, txtAverageGrade

    lstGradeList.clear()
    tbxGrade1.focus()

    tbxGrade1.clear()
    tbxGrade2.clear()
    tbxGrade3.clear()
    tbxGrade4.clear()
    tbxGrade5.clear()

    txtSort1.clear()
    txtSort2.clear()
    txtSort3.clear()
    txtSort4.clear()
    txtSort5.clear()

    txtLowestGrade.set("")
    txtHighestGrade.set("")
    txtAverageGrade.set("")


def main():
    global tbxGrade1, tbxGrade2, tbxGrade3, tbxGrade4, tbxGrade5
    global txtSort1, txtSort2, txtSort3, txtSort4, txtSort5
    global txtLowestGrade, txtHighestGrade, txtAverageGrade

    window = App(title="Grade Analysis",
                 width=450, height=450,
                 layout="grid")

    Text(window, grid=[0, 0])  # Spacer

    Text(window, text="Enter Grades", grid=[0, 2])
    Text(window, text="  Sorted Grades", grid=[0, 3])

    Text(window, text="Grade 1 ", grid=[1, 1])
    tbxGrade1 = TextBox(window, grid=[1, 2])
    txtSort1 = Text(window, text="", grid=[1, 3])

    Text(window, grid=[2, 0])  # Spacer

    Text(window, text="Grade 2 ", grid=[3, 1])
    tbxGrade2 = TextBox(window, grid=[3, 2])
    txtSort2 = Text(window, text="", grid=[3, 3])

    Text(window, grid=[4, 0])  # Spacer

    Text(window, text="Grade 3 ", grid=[5, 1])
    tbxGrade3 = TextBox(window, grid=[5, 2])
    txtSort3 = Text(window, text="", grid=[5, 3])

    Text(window, grid=[6, 0])  # Spacer

    Text(window, text="Grade 4 ", grid=[7, 1])
    tbxGrade4 = TextBox(window, grid=[7, 2])
    txtSort4 = Text(window, text="", grid=[7, 3])

    Text(window, grid=[8, 0])  # Spacer

    Text(window, text="Grade 5 ", grid=[9, 1])
    tbxGrade5 = TextBox(window, grid=[9, 2])
    txtSort5 = Text(window, text="", grid=[9, 3])

    Text(window, grid=[10, 0])  # Spacer

    Text(window, text="Lowest ", grid=[11, 2])
    txtLowestGrade = Text(window, text="", grid=[11, 3])

    Text(window, grid=[12, 0])  # Spacer

    Text(window, text="Highest ", grid=[13, 2])
    txtHighestGrade = Text(window, grid=[13, 3])

    Text(window, grid=[14, 0])  # Spacer

    Text(window, text="Average ", grid=[15, 2])
    txtAverageGrade = Text(window, grid=[15, 3])

    # Text(window, grid=[16, 0])  # Spacer

    PushButton(window, text=" CALC ", command=calc,
               grid=[18, 1])

    Text(window, text=" ", grid=[17, 4])  # Spacer

    PushButton(window, text="CLEAR", command=clear,
               grid=[18, 2])

    Text(window, text="    ", grid=[17, 6])  # Spacer

    PushButton(window, text=" QUIT ", command=quit,
               grid=[18, 4])

    window.display()

main()
