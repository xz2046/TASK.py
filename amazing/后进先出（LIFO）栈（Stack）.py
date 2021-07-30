'''
 定义一个栈（Stack）类，用于模拟一种具有后进先出（LIFO）特性的数据结构。至少需要有以下方法：
方法名	     含义
isEmpty()	 判断当前栈是否为空（返回 True 或 False）
push()	     往栈的顶部压入一个数据项
pop()	     从栈顶弹出一个数据项（并在栈中删除）
top()	     显示当前栈顶的一个数据项
bottom()	 显示当前栈底的一个数据项
'''


class Stack:
    def __init__(self, list=[]):
        self.stack = []
        for i in list:
            self.push(i)

    def isEmpty(self):
        return not self.stack

    def push(self, obj):
        self.stack.append(obj)

    def pop(self):
        if not self.stack:
            print("栈值为空")
        else:
            self.stack.pop()

    def top(self):
        if not self.stack:
            print("栈值为空")
        else:
            return self.stack[-1]

    def bottom(self):
        if not self.stack:
            print("栈值为空")
        else:
            return self.stack[0]


import easygui as g

s = Stack()

while True:
    msg = "请输入你的指令"
    title = "LIFO"
    strs = g.buttonbox(msg, title, choices=("添加", "删除", "显示顶部数据", "显示底部数据"))
    if strs == "测试栈是否为空":
        s.isEmpty()
    elif strs == "添加":
        msg = "请输入您要添加的数据："
        title = "添加"
        q = g.enterbox(msg, title)
        s.push(obj=q)
    elif strs == "删除":
        s.pop()
    elif strs == "显示顶部数据":
        g.msgbox(s.top())
    elif strs == "显示底部数据":
        g.msgbox(s.bottom())
    else:
        break
