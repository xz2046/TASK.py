import pandas
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

scale = StandardScaler()

df = pandas.read_csv("E:\Python Pycharm\练习\机器学习基础\练习数据\cars.csv")

X = df[['Weight', 'Volume']]
y = df['CO2']
'''缩放方法之一：标准化
标准化方法使用以下公式：z = (x - u) / s
其中 z 是新值，x 是原始值，u 是平均值，s 是标准差。
Python sklearn 模块有一个名为 StandardScaler() 的方法，该方法返回带有转换数据集方法的 Scaler 对象。'''
scaledX = scale.fit_transform(X)
print(scaledX)
regr = linear_model.LinearRegression()
regr.fit(scaledX, y)
# 预测一辆重 2300 公斤的 1.3 升汽车的二氧化碳排放量
scaled = scale.transform([[2300, 1.3]])

predictedCO2 = regr.predict([scaled[0]])
print(predictedCO2)
