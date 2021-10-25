import pandas
from sklearn import linear_model

# 多元回归就像线性回归一样，但是具有多个独立值，可以基于两个或多个变量来预测一个值。
df = pandas.read_csv("E:\Python Pycharm\练习\机器学习基础\练习数据\cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']

regr = linear_model.LinearRegression()
regr.fit(X, y)

# 预测重量为 2300kg、排量为 1300ccm 的汽车的二氧化碳排放量：

predictedCO2 = regr.predict([[2300, 1300]])

print(predictedCO2)
print(regr.coef_)  # 系数，X每增长1，y增长多少
'''
在 sklearn 模块中，用 LinearRegression() 方法创建一个线性回归对象。

该对象有一个名为 fit() 的方法，该方法将独立值和从属值作为参数，并用描述这种关系的数据填充回归对象'''