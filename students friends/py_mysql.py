from pymysql import *
from tkinter import *


class Data():
    def __init__(self):
        self.conn = connect(host="localhost", port=3306, user='root', password='xingzhu2046', database='friend',
                            charset='utf8')
        self.cs = self.conn.cursor()
        self.sql = ""

    def __del__(self):
        self.cs.close()
        self.conn.close()

    def select_sql(self,sql,l1=[]):
        self.cs.execute(sql,l1)
        for each in self.cs.fetchall():
            print(each)

    def insert_sql(self):
        self.cs.execute(self.sql)

    def do_sql(self):
        self.conn.commit()

    def long(self):
            s1 = e1.get()
            s2 = e2.get()
            sql = "select * from user where name=%s and pwd=%s"
            pwd = self.cs.execute(sql,[s1,s2])
            if pwd:
                print("登陆成功")

    def register(self):
        s3, s4, s5, s6, v1 = e3.get(), e4.get(), e5.get(), e6.get(), v.get()
        if v1 == 1:
            v1 = '男'
        else:
            v1 = '女'

        if s4 != s5:
            print('两次密码不一致，请重新输入')
            register_gui()
        else:       
            sql = "insert into user values(null,%s,%s,%s,%s)"
            pwd = self.cs.execute(sql,[s3,v1,s6,s4])
            self.conn.commit()
            if pwd:
                print("注册成功")



dt = Data()

def logon_gui():
    global e1,e2
    w1 = Toplevel()
    w1.title('登录')
    f1 = Frame(w1)
    f1.pack()
    lab1 = Label(f1, text="用户名:")
    lab1.grid(row=0, column=0)
    lab2 = Label(f1, text="密码:")
    lab2.grid(row=1, column=0)

    e1 = Entry(f1)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2 = Entry(f1, show="*")
    e2.grid(row=1, column=1, padx=10, pady=5)

    b1 = Button(f1, text="登录", width=10, command=lambda: dt.long())
    b1.grid(row=2, column=0, sticky=W, padx=10, pady=5)
    b2 = Button(f1, text="取消", width=10)
    b2.grid(row=2, column=1, sticky=E, padx=10, pady=5)
    

def register_gui():
    global e3, e4, e5, e6, v
    w2 = Toplevel()
    f2 = Frame(w2).grid()
    lab3 = Label(f2, text="用户名:")
    lab3.grid(row=0, column=0)
    lab6 = Label(f2, text="性别:")
    lab6.grid(row=1, column=0)
    lab4 = Label(f2, text="密码:")
    lab4.grid(row=2, column=0)
    lab5 = Label(f2, text="确认密码:")
    lab5.grid(row=3, column=0)
    lab7 = Label(f2, text="电话:")
    lab7.grid(row=4, column=0)

    e3 = Entry(f2)
    e3.grid(row=0, column=1, padx=10, pady=5)

    v = IntVar()
    v.set(1)
    rb1 = Radiobutton(f2, text="男", variable=v, value=1)
    rb1.grid(row=1, column=1, padx=15, pady=5)
    rb2 = Radiobutton(f2, text="女", variable=v, value=2)
    rb2.grid(row=1, column=2, padx=15, pady=5)
    
    e4 = Entry(f2, show="*")
    e4.grid(row=2, column=1, padx=10, pady=5)
    e5 = Entry(f2, show="*")
    e5.grid(row=3, column=1, padx=10, pady=5)
    e6 = Entry(f2)
    e6.grid(row=4, column=1, padx=10, pady=5)

    b3 = Button(f2, text="注册",  width=10, command=lambda: dt.register())
    b3.grid(row=5, column=1, padx=15, pady=10)


root = Tk()
fr1 = Frame(root).grid()
bf1 = Button(fr1, text="登录", command=logon_gui)
bf1.grid(row=0, column=0, sticky=W, padx=10, pady=5)
b2 = Button(fr1, text="注册", width=10, command=register_gui)
b2.grid(row=0, column=1, sticky=E, padx=10, pady=5)

mainloop()