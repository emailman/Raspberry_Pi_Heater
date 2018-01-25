from guizero import App, Text, TextBox, PushButton


def say_hello():
    txtGreeting.set("Hello " + tbxFirst.get() + " " + tbxLast.get())


window = App(title="Name Thingy")

Text(window, text="Enter your first name below")

tbxFirst = TextBox(window)

Text(window, text="Enter your last name below")

tbxLast = TextBox(window)

PushButton(window, command=say_hello, text="Push to say hello")

txtGreeting = Text(window, text="Greeting here")

window.display()
