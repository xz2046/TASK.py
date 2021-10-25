import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)
# r 表示拟合度，拟合度越高，线性回归预测越好，太低则不适合使用。
print(r)


def myfunc(x):
    return slope * x + intercept


print(myfunc(10))  # 预测10时候的值

mymodel = list(map(myfunc, x))
 
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()
