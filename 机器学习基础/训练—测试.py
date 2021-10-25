import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

numpy.random.seed(2)

x = numpy.random.normal(3, 1, 100)
y = numpy.random.normal(150, 40, 100) / x

train_x = x[:80]
train_y = y[:80]

test_x = x[80:]
test_y = y[80:]
# plt.scatter(train_x, train_y)
# plt.scatter(test_x, test_y) #比较训练集和测试集图形
# plt.scatter(x, y)

mymodel = numpy.poly1d(numpy.polyfit(train_x, train_y, 4))

myline = numpy.linspace(0, 6, 100)
# sklearn 模块 rs_score() 的方法,测量 x 轴和 y 轴之间的关系，取值范围从 0 到 1，其中 0 表示没有关系，而 1 表示完全相关。
r1 = r2_score(train_y, mymodel(train_x))
print(r1)  # 先确定训练集相关性
r2 = r2_score(test_y, mymodel(test_x))
print(r2)  # 训练集关系高则引入测试集测试，如果同样适用则可使用。

print(mymodel(5))  # 预测y为5时的值

plt.scatter(train_x, train_y)
plt.plot(myline, mymodel(myline))
plt.show()
