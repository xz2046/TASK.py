from tkinter import *

root = Tk()

lab1 = Label(root, text="用户名:").grid(row=0, column=0)
lab2 = Label(root, text="密码:").grid(row=1, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1, padx=10, pady=5)
e1.insert(0, "张三")
e2 = Entry(root, show="*")
e2.insert(0, "123")
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print("用户名：%s" % e1.get())
    print("密码：%s" % e2.get())


b1 = Button(root, text="登录", width=10, command=show)\
    .grid(row=2, column=0, sticky=W, padx=10, pady=5)
b2 = Button(root, text="取消", width=10, command=root.quit)\
    .grid(row=2, column=1, sticky=E, padx=10, pady=5)

mainloop()
