from tkinter import *

root = Tk()
f1 = Frame(root)
f1.pack()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()


def test(content):
    return content.isdigit()


variable = StringVar()
variable.set("+")

tests = f1.register(test)
e1 = Entry(f1, textvariable=v1, validate="key",
           validatecommand=(tests, "%P")).grid(row=0, column=0, padx=10, pady=10)
w = OptionMenu(f1, variable, "+", "-", "✖", "➗")
w.grid(row=0, column=1)
e2 = Entry(f1, textvariable=v2, validate="key",
           validatecommand=(tests, "%P")).grid(row=0, column=2, padx=10, pady=10)
lab2 = Label(f1, text="=").grid(row=0, column=3)
e3 = Entry(f1, textvariable=v3, state="readonly").grid(row=0, column=4, padx=10, pady=10)


def sum2():
    __sums = int(v1.get()) + int(v2.get())
    v3.set(str(__sums))


def sum1():
    __sums = int(v1.get()) - int(v2.get())
    v3.set(str(__sums))


def sum3():
    __sums = int(v1.get()) * int(v2.get())
    v3.set(str(__sums))


def sum4():
    __sums = int(v1.get()) / int(v2.get())
    v3.set(str(__sums))


def sums():
    if variable.get() == "+":
        sum2()
    elif variable.get() == "-":
        sum1()
    elif variable.get() == "➗":
        sum4()
    else:
        sum3()
    return sums


b1 = Button(f1, text="计算", command=sums).grid(row=1, column=2, pady=10)
mainloop()
