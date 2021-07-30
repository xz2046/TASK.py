from matplotlib import pyplot as plt
from matplotlib import font_manager

x = ["你好，李焕英", "唐人街探案3", "哥斯拉大战金刚", "送你一朵小红花", "悬崖之上", "速度与激情9", "刺杀小说家", "我的姐姐", "你的婚礼", "人潮汹涌"]
y = [54.14, 45.15, 12.31, 11.96, 10.77, 10.57, 10.35, 8.60, 7.89, 7.62]

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
plt.figure(figsize=(20, 9), dpi=100)

plt.barh(range(len(x)), y, height=0.5, color="cyan")  # bar为竖， barh为横
plt.xlabel("片名", fontproperties=my_font)
plt.ylabel("票房/亿", fontproperties=my_font)
plt.title("2021年票房前十电影", fontproperties=my_font)
plt.yticks(range(len(x)), x, fontproperties=my_font, rotation=0)
plt.xticks(range(0, 60, 5))

plt.grid(alpha=0.6)
plt.savefig("./m05.png")

plt.show()
