from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

'''font = {"family": "宋体",
        "weight": "bold",
        "size": "larger"}

matplotlib.rc("font", **font)'''

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)

x_list = ["10点{}分".format(i) for i in range(60)]
x_list += ["11点{}分".format(i) for i in range(60)]

plt.xticks(list(x)[::5], x_list[::5], rotation=45, fontproperties=my_font)
plt.ylabel("温度（℃）", fontproperties=my_font)
plt.xlabel(" 时间", fontproperties=my_font)
plt.title("10--12每分钟的温度变化", fontproperties=my_font)
plt.savefig("./m02.png")
plt.show()
