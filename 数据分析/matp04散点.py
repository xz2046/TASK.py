from matplotlib import pyplot as plt, font_manager

y_3 = [16, 10, 12, 16, 16, 18, 20, 16, 16, 17, 18, 19, 17, 17, 19, 17, 21, 24, 25, 25, 23, 24, 25, 25, 27, 20, 11, 14,
       16, 13, 21]
y_6 = [34, 33, 36, 37, 38, 37, 33, 28, 20, 29, 26, 29, 31, 31, 27, 22, 24, 31, 31, 30, 29, 25, 29, 33, 34, 27, 27, 28,
       36, 35]
x_3 = range(1, 32)
x_6 = range(41, 71)

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
plt.figure(figsize=(20, 9), dpi=100)

plt.scatter(x_3, y_3, label="3月份")
plt.scatter(x_6, y_6, label="6月份")
plt.title("西安3月和6月每日最高气温变化表", fontproperties=my_font)

xl = list(x_3) + list(x_6)
xl2 = ["3月{}日".format(i) for i in x_3]
xl2 += ["6月{}日".format(i-40) for i in x_6]
plt.yticks(range(min(y_3 + y_6), max(y_6 + y_3)+4, 2))
plt.xticks(xl[::3], xl2[::3], fontproperties=my_font, rotation=40)
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)

plt.legend(prop=my_font)
plt.savefig("./m04.png")
plt.show()