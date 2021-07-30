from matplotlib import pyplot as plt, font_manager
import random

y_1 = []
for i in range(0, 201):
    y_1.append(random.randint(123, 215))
print(y_1)

# 计算组距
d = 10
num_bins = (max(y_1) - min(y_1)) // d + 1
print(num_bins)

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")
plt.figure(figsize=(20, 9), dpi=100)

plt.hist(y_1, num_bins)
plt.xticks(range(min(y_1), max(y_1)+d, d))

plt.grid()

plt.show()