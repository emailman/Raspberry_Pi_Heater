# CIS120
# Rectangle Calculator Lab
# Eric Mailman
# September/2017

from guizero import App, Text, TextBox, PushButton

def calculate_p():
        txtOutputErr.set("")
        if tbxEnterLength.get() != "" or tbxEnterWidth.get() != "":
            #throw an error when an input is characters
            try:
                length = float(tbxEnterLength.get())
                width = float(tbxEnterWidth.get())
                #check length n width cannot be negative number
                if length < 0 or width < 0:
                    txtOutputErr.set("Error: Negative number entered")
                    txtOutputArea.set("")
                    txtOutputPerimeter.set("")
                else:
                    area = length * width
                    perimeter = 2 * (length + width)
                    txtOutputArea.set(str(area))
                    txtOutputPerimeter.set(str(perimeter))
            except ValueError:
                txtOutputErr.set("Error: non-numberic text entered")
                txtOutputArea.set("")
                txtOutputPerimeter.set("")
        else:
            txtOutputErr.set("Error: No number entered")
            txtOutputArea.set("")
            txtOutputPerimeter.set("")

window1 = App("Rectangle Calculator", height=450, width=380,
              layout="grid")

Text(window1, "  ", grid=[0, 0])#spacer
Text(window1, "Length:", grid=[1, 1])
Text(window1, "  ", grid=[2, 0])#spacer
Text(window1, "  ", grid=[3, 0])#spacer
Text(window1, "Width:", grid=[3, 1] )
Text(window1, "  ", grid=[4, 0])#spacer
Text(window1, "  ", grid=[7, 0])#spacer
Text(window1, "     Area:", grid=[8, 1])
Text(window1, "  ", grid=[9, 0])#spacer
Text(window1, "Perimeter:", grid=[10, 1])
Text(window1, "  ", grid=[11, 0])#spacer
Text(window1, "  ", grid=[13,0])#spacer

tbxEnterLength = TextBox(window1, grid=[1, 2], align="left")
tbxEnterWidth = TextBox(window1, grid=[3,2], align="left")
txtOutputArea = Text(window1, grid =[8,2], align="left")
txtOutputPerimeter = Text(window1, grid =[10,2], align="left")
txtOutputErr= Text(window1, grid=[14 ,2], align="left")

PushButton(window1, text="Calculate",
           command=calculate_p, grid=[6, 2], align="center")
PushButton(window1, text=" Exit ",
           command=quit, grid=[12, 2], align="center")

window1.display()