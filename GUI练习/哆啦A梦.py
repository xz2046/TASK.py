from tkinter import *

root = Tk()
root.geometry('410x410+500+200')

# 绘制幕布
w = Canvas(root, width=400, height=400, bg='white')
w.pack()

# 绘制坐标系
w.create_line(0, 200, 400, 200, fill='green', dash=(4, 4))
w.create_line(200, 0, 200, 400, fill='green', dash=(4, 4))

# 绘制头部
w.create_oval(100, 40, 300, 240, fill='blue')
w.create_oval(115, 70, 285, 240, fill='white')

# 绘制眼睛
w.create_oval(165, 50, 200, 90, fill='white')
w.create_oval(200, 50, 235, 90, fill='white')
w.create_oval(185, 62, 195, 77, fill='black')
w.create_oval(205, 62, 215, 77, fill='black')
w.create_oval(189, 65, 192, 75, fill='white')
w.create_oval(208, 65, 211, 75, fill='white')

# 绘制鼻子
w.create_oval(193, 83, 207, 97, fill='red')

# 绘制嘴巴
w.create_line(200, 97, 200, 177)
w.create_arc(130, 67, 270, 177, start=-45, extent=-90, style=ARC)

# 绘制胡须
w.create_line(180, 127, 130, 127)
w.create_line(220, 127, 270, 127)

w.create_line(180, 107, 140, 97)
w.create_line(220, 107, 260, 97)

w.create_line(180, 147, 140, 157)
w.create_line(220, 147, 260, 157)

# 绘制身体
w.create_rectangle(120, 200, 280, 350, fill='blue')
w.create_oval(130, 180, 270, 320, fill='white')

w.create_arc(130, 180, 270, 320, outline='white', start=45, extent=90, style=ARC)

# 绘制铃铛
w.create_rectangle(125, 195, 275, 205, fill='red')
w.create_arc(118, 195, 132, 205, fill='red', start=90, extent=180)
w.create_arc(268, 195, 282, 205, fill='red', start=90, extent=-180)
w.create_line(125, 195, 125, 205, fill='red')
w.create_line(275, 195, 275, 205, fill='red')

w.create_oval(188, 200, 212, 224, fill='yellow')
w.create_line(188, 212, 212, 212)
w.create_line(190, 209, 211, 209)
w.create_oval(197, 215, 203, 221, fill='red')
w.create_line(200, 221, 200, 224)

# 绘制口袋

w.create_arc(155, 205, 245, 295, style=PIESLICE, start=0, extent=-180)

# 绘制手脚
# 脚
w.create_arc(180, 330, 220, 370, style=PIESLICE, start=0, extent=180, fill='white', outline='white')
w.create_oval(100, 332, 190, 368, fill='white')
w.create_oval(210, 332, 300, 368, fill='white')

# 手
points1 = [
    (120, 205),
    (120, 265),
    (90, 280),
    (80, 260)
]

w.create_polygon(points1, fill='blue', outline='black')
w.create_oval(55, 260, 95, 300, fill='white')

points2 = [
    (280, 205),
    (280, 265),
    (310, 280),
    (320, 260)
]
w.create_polygon(points2, fill='blue', outline='black')
w.create_oval(345, 260, 305, 300, fill='white')

mainloop()
