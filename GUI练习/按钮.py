from tkinter import *

root = Tk()

f1 = LabelFrame(root, text="请选择你的英雄：", bd=5, fg="red", labelanchor=NW)
f1.pack()

List = [("成浪", 1),
        ("魏文博", 2),
        ("王子航", 3),
        ("鲁启航", 4),
        ("杜金龙", 5),
        ("杜金龙", 6)]
v = IntVar()
for lang, num in List:
    b1 = Radiobutton(f1, text=lang, variable=v, value=num, indicatoron=False).pack(anchor=W, v = IntVar()
v.set(2)

Radiobutton(master, text="One", variable=v, value=1).pack(anchor=W)
Radiobutton(master, text="Two", variable=v, value=2).pack(anchor=W))

mainloop()


