from matplotlib import font_manager, pyplot as plt

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")

x = range(11, 31)
y_1 = [1, 0, 1, 2, 6, 5, 4, 3, 2, 1, 1, 3, 2, 4, 1, 3, 2, 0, 2, 3]
y_2 = [1, 0, 1, 3, 4, 2, 3, 0, 2, 0, 3, 1, 4, 2, 0, 1, 0, 2, 0, 0]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y_1, label="1号", color="m", linewidth=2)
plt.plot(x, y_2, label="2号", color="cyan")

plt.xticks(x, rotation=45, fontproperties=my_font)
plt.yticks(range(min(y_1 and y_2), max(y_1 and y_2) + 2))
plt.ylabel("年龄", fontproperties=my_font)
plt.xlabel("人数", fontproperties=my_font)
plt.title("11至30岁身高增长高度", fontproperties=my_font)
plt.grid(alpha=0.6, linestyle="-.")  # 透明度

plt.legend(prop=my_font)
plt.savefig("./m03.png")
plt.show()
