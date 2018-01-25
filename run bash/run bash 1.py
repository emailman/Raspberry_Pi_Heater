import subprocess
from guizero import *


def update():
    output = subprocess.getoutput('eric.sh')
    txtUpdate.set(output)
    window.after(1000, update)


window = App(title="Auto Display",
             width=300, height=100)
txtUpdate = Text(window)
window.after(1000, update)
window.display()
