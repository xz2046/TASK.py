from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [12, 16, 18, 22, 26, 15, 19, 18, 26, 23, 14, 17]
fig = plt.figure(figsize=(20, 8), dpi=80)
plt.plot(x, y)
plt.xticks(range(2, 25, 1))
plt.yticks(range(min(y), max(y)+1))
plt.savefig("./m01.png")
plt.show()
