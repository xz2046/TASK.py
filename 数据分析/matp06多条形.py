from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
movie = ["1921", "革命者", "比得兔2：逃跑计划", "当男人恋爱时", "守岛人"]
plt.figure(figsize=(20, 9), dpi=100)

b_5 = [31514.9, 7810.2, 18190.5, 13890.7, 8079.6]
b_6 = [33372.5, 8533.3, 18561.9, 23995, 8282.4]
b_7 = [34991.6, 9129, 18914.9, 24307, 8478]

bar_width = 0.3
x_5 = list(range(len(movie)))
x_6 = [i + bar_width for i in x_5]
x_7 = [i + bar_width * 2 for i in x_5]

plt.bar(range(len(movie)), b_5, width=bar_width, label="7月5日")
plt.bar(x_6, b_6, width=bar_width, label="7月6日")
plt.bar(x_7, b_7, width=bar_width, label="7月7日")
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("票房/万", fontproperties=my_font)
plt.xticks(x_5, movie, fontproperties=my_font)

plt.legend(prop=my_font)
plt.savefig("./m06.png")
plt.show()
