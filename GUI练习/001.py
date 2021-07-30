from tkinter import *
import webbrowser

root = Tk()

f1 = Frame(root)
f1.pack(padx=10, pady=10)
f2 = LabelFrame(root, text="欢迎")
f2.pack(padx=5, pady=10)
str1 = StringVar()
str1.set("你好")

photo = PhotoImage(file="001.gif")
lab2 = Label(f2, image=photo)
lab2.pack(side=TOP)
lab1 = Label(f1,
             textvariable=str1,
             justify=LEFT,
             font=("宋体", 20),
             padx=10, pady=10,
             fg="black"
             )
lab1.pack(side=BOTTOM)

sb = Scrollbar(f1)
sb.pack(side=RIGHT, fill=Y)
sb1 = Scrollbar(f1, orient=HORIZONTAL)
sb1.pack(side=BOTTOM, fill=X)
theLB = Listbox(f1, yscrollcommand=sb.set, xscrollcommand=sb1.set, selectborderwidth=2, height=5, selectmode=SINGLE)
theLB.pack()


def show():
    text.insert(INSERT, "你还真敢点啊！\n年轻人有勇气")
    text.image_create("m1", image=photo)


text = Text(f2, width=30, height=10)
text.pack()
text.insert(INSERT, "练习练习\n练习练习")
text.mark_set("m1", 3.0)  # 解除text.mark_unset()
text.insert("m1", "hello")
text.tag_add("tag1", 1.1, 1.2, 1.6, 1.8)
text.tag_config("tag1", background="yellow", foreground="red")


def arrow_cursor(event):
    text.config(cursor="arrow")


def xterm_cursor(event):
    text.config(cursor="xterm")


def click(event):
    webbrowser.open("www.bilibili.com")


text.insert(2.0, "bilibili.com")  # 绑定鼠标按键
text.tag_add("tag2", 2.0, 2.12)
text.tag_config("tag2", foreground="blue", underline=True)
text.tag_bind("tag2", "<Enter>", arrow_cursor)
text.tag_bind("tag2", "<Leave>", xterm_cursor)
text.tag_bind("tag2", "<Button-1>", click)

b1 = Button(text, text="点我试试", command=show)

text.window_create(INSERT, window=b1)

lists = ["张三", "李四", "王五", "尼古拉斯.凯奇", "巴勃罗·迭戈·何塞·弗朗西斯科·狄·保拉·胡安·纳波穆西诺·玛莉亚·狄·洛斯·雷梅迪奥斯·西普里亚诺·狄·拉·圣地西玛·特里尼达·路易斯·毕加索",
         1, 2, 3, 4, 5, 6, 78, 8, 9, 0, 87]
for item in lists:
    theLB.insert(END, item)
sb.config(command=theLB.yview)
sb1.config(command=theLB.xview)
root.mainloop()
