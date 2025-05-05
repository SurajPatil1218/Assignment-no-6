from tkinter import *

window = Tk()
window.geometry('500x400')

e = Entry(window, width=56, borderwidth=5)
e.place(x=0, y=0)

# Click Handler
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

# Buttons
Button(window, text='1', width=12, command=lambda: click(1)).place(x=10, y=60)
Button(window, text='2', width=12, command=lambda: click(2)).place(x=80, y=60)
Button(window, text='3', width=12, command=lambda: click(3)).place(x=170, y=60)
Button(window, text='4', width=12, command=lambda: click(4)).place(x=10, y=120)
Button(window, text='5', width=12, command=lambda: click(5)).place(x=80, y=120)
Button(window, text='6', width=12, command=lambda: click(6)).place(x=170, y=120)
Button(window, text='7', width=12, command=lambda: click(7)).place(x=10, y=180)
Button(window, text='8', width=12, command=lambda: click(8)).place(x=80, y=180)
Button(window, text='9', width=12, command=lambda: click(9)).place(x=170, y=180)
Button(window, text='0', width=12, command=lambda: click(0)).place(x=10, y=240)

# Operation Functions
def add():
    global i, math
    i = int(e.get())
    math = "Addition"
    e.delete(0, END)

def sub():
    global i, math
    i = int(e.get())
    math = "Substraction"
    e.delete(0, END)

def mult():
    global i, math
    i = int(e.get())
    math = "Multiplication"
    e.delete(0, END)

def div():
    global i, math
    i = int(e.get())
    math = "Division"
    e.delete(0, END)

Button(window, text='+', width=12, command=add).place(x=80, y=240)
Button(window, text='-', width=12, command=sub).place(x=170, y=240)
Button(window, text='*', width=12, command=mult).place(x=10, y=300)
Button(window, text='/', width=12, command=div).place(x=80, y=300)

# Equal Function
def equal():
    n2 = int(e.get())
    e.delete(0, END)
    if math == "Addition":
        e.insert(0, i + n2)
    elif math == "Substraction":
        e.insert(0, i - n2)
    elif math == "Multiplication":
        e.insert(0, i * n2)
    elif math == "Division":
        e.insert(0, i / n2)

Button(window, text='=', width=12, command=equal).place(x=170, y=300)

# Clear Function
def clear():
    e.delete(0, END)

Button(window, text='Clear', width=12, command=clear).place(x=10, y=350)

window.mainloop()