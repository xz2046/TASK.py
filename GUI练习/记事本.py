import hashlib
import os
from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.title("小样记事本")

f1 = Frame(root)
f1.pack(padx=10, pady=5, expand=True, fill=BOTH)
sb = Scrollbar(f1)
sb.pack(side=RIGHT, fill=Y)
sb1 = Scrollbar(f1, orient=HORIZONTAL)
sb1.pack(side=BOTTOM, fill=X)
text = Text(f1, undo=True, autoseparators=False, yscrollcommand=sb.set, xscrollcommand=sb1.set)
text.pack(padx=10, pady=10, expand=True, fill=BOTH)
sb.config(command=text.yview)
sb1.config(command=text.xview)


def new_file():  # 新建
    global root, filename, text
    root.title("未命名文件")
    filename = None
    text.delete(1.0, END)


def open_file():  # 打开
    global filename
    filename = askopenfilename(defaultextension=".txt")
    if filename == "":
        filename = None
    else:
        root.title("记事本" + os.path.basename(filename))
        text.delete(1.0, END)
        f = open(filename, 'r')
        text.insert(1.0, f.read())
        f.close()


def save():  # 保存
    global filename
    try:
        f = open(filename, 'w')
        msg = text.get(1.0, 'end')
        f.write(msg)
        f.close()
    except:
        mysaveas()


def mysaveas():
    global filename
    f = asksaveasfilename(initialfile="未命名.txt", defaultextension=".txt")
    filename = f
    fh = open(f, 'w')
    msg = text.get(1.0, END)
    fh.write(msg)
    fh.close()
    root.title("记事本" + os.path.basename(f))


def cut():  # 剪切
    global text
    text.event_generate("<<Cut>>")


def copy():  # 复制
    global text
    text.event_generate("<<Copy>>")


def paste():  # 粘贴
    global text
    text.event_generate("<<Paste>>")


def getindex(text, index):  # 查找
    return tuple(map(int, str.split(text.index(index), ".")))


def show():
    global e1, w1
    w1 = Toplevel()
    e1 = Entry(w1)
    e1.grid(row=0, column=0, padx=10, pady=10)
    b4 = Button(w1, text="搜索", command=pos)
    b4.grid(row=0, column=1, padx=10, pady=10)


def pos():
    s2 = e1.get()
    start = 1.0
    while True:
        pos = text.search(s2, start, stopindex=END)
        if not pos:
            break
        else:
            s = "找到了，位置是:", getindex(text, pos)
            text.insert(INSERT, s)
            start = pos + "+1c"


def replace():  # 替换
    global e3, e4
    w6 = Toplevel()
    e3 = Entry(w6)
    e3.grid(row=0, column=0, padx=10, pady=10)
    e4 = Entry(w6)
    e4.grid(row=1, column=0, padx=10, pady=10)
    l1 = Label(w6, text="输入")
    l1.grid(row=0, column=1, padx=10, pady=10)
    b2 = Button(w6, text="替换", command=substitute)
    b2.grid(row=1, column=1, padx=10, pady=10)


def find_s():
    global list_all
    find_str = e3.get()
    start = 1.0
    list_all = []
    while True:
        find1 = text.search(find_str, start, END)
        if not find1:
            break
        else:
            list_all.append(find1)
            start = find1 + "+1c"


def substitute():
    find_s()
    for each in list_all:
        text.delete(each)
        text.mark_set("m1", each)
        find2 = e4.get()
        text.insert("m1", find2)


def Recanted():  # 撤销
    try:
        text.edit_undo()
    except:
        pass


def callback(event):
    text.edit_separator()


def omit():  # 删除
    text.delete(1.0, END)


def select_all():  # 全选
    text.tag_add("sel", "1.0", "end")


def helps():  # 帮助
    w4 = Toplevel()
    f2 = Frame(w4)
    f2.pack(padx=5, pady=5)
    lb = Label(f2, text="请联系作者：小杨;QQ：2635078557", width=40, anchor=NW)
    lb.pack(padx=10, pady=10)


def feedback():  # 反馈
    w3 = Toplevel()
    f2 = Frame(w3)
    f2.pack(padx=5, pady=5)
    lb = Label(f2, text="邮箱：18392939411@163.com", width=40, anchor=NW)
    lb.pack(padx=10, pady=10)


def particulars():  # 详情
    w5 = Toplevel()
    f2 = Frame(w5)
    f2.pack(padx=5, pady=5)
    m = Message(f2, text="版本：1.10", width=500, justify=LEFT)
    m.pack(padx=10, pady=10)
    m1 = Message(f2, text="后续更新敬请期待！", width=500, justify=LEFT)
    m1.pack(padx=10, pady=10)


contents = text.get(1.0, END)


def gettext(contents):  # 检查
    m = hashlib.md5(contents.encode())
    return m.digest()


s1 = gettext(contents)


def check():
    contents = text.get(1.0, END)
    if s1 != gettext(contents):
        w5 = Toplevel()
        f2 = Frame(w5)
        f2.pack(padx=10, pady=10)
        l1 = Label(f2, text="内容发生变动,是否保存？", width=20, height=2, foreground="red")
        l1.pack(padx=10, pady=10)
        b1 = Button(w5, text="保存")
        b1.pack(side=LEFT, padx=1, pady=10, command=save)
        b2 = Button(w5, text="取消", command=root.quit)
        b2.pack(side=RIGHT, padx=1, pady=10)
    else:
        root.quit()


menubar = Menu(root)  # 菜单
root.config(menu=menubar)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="新建", command=new_file)
filemenu.add_command(label="打开", command=open_file)
filemenu.add_command(label="保存", command=save)
filemenu.add_separator()
filemenu.add_command(label="退出", command=check)
menubar.add_cascade(label="文件", menu=filemenu)

editmenu = Menu(menubar, tearoff=False)
editmenu.add_command(label="撤销", command=Recanted)
editmenu.add_separator()
editmenu.add_command(label="复制", command=copy)
editmenu.add_command(label="粘贴", command=paste)
editmenu.add_command(label="剪切", command=cut)
editmenu.add_command(label="删除", command=omit)
editmenu.add_separator()
editmenu.add_command(label="查找", command=show)
editmenu.add_command(label="替换", command=replace)
editmenu.add_separator()
editmenu.add_command(label="全选", command=select_all)
menubar.add_cascade(label="编辑", menu=editmenu)

helpmenu = Menu(menubar, tearoff=False)
helpmenu.add_command(label="查看帮助", command=helps)
helpmenu.add_command(label="发送反馈", command=feedback)
helpmenu.add_separator()
helpmenu.add_command(label="关于记事本", command=particulars)
menubar.add_cascade(label="帮助", menu=helpmenu)


def dosome(event):
    num = text.index("insert")
    rowcolumn.set("第{}行  第{}列".format(*str(num).split('.')))


def hunhe(event):
    dosome(event)
    callback(event)


text.bind("<Button-1>", dosome)
text.bind("<KeyPress>", hunhe)
rowcolumn = StringVar()
lab = Label(root, textvariable=rowcolumn, fg="#1E90FF")
lab.pack(side=LEFT, padx=30)

mainloop()
