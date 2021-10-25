import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
from sklearn import linear_model

df = pd.read_excel(r'E:\Python Pycharm\练习\fenxi\collect.xlsx', )  # 读取保存数据
df = df.set_index("日期")  # 设置索引
df = df.dropna(axis=0, how="any", inplace=False)  # 删除缺失数据行
print(df.info())

my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\STKAITI.TTF")


# 制作天气与营业额关系图
def paint_data1():
    data1 = df.groupby(by="天气")
    datax_1 = data1["订单笔数"].mean()
    datax_2 = data1["营业收入"].mean()

    x_1 = datax_1.values
    x_2 = datax_2.values
    x_2 = [i / 1000 for i in x_2]
    y_ = datax_1.index

    plt.figure(figsize=(20, 9), dpi=100)

    plt.bar(y_, range(len(x_1)), color="cyan", label="订单笔数")
    plt.plot(y_, x_2, color='orange', label="平均每天营业额")

    plt.title("天气与营业额关系图", fontproperties=my_font, fontsize=20)
    plt.xticks(range(len(x_1)), y_, fontproperties=my_font)
    plt.yticks(range(0, 22, 2))
    plt.ylabel("千元/笔数", fontproperties=my_font, rotation=90)
    plt.xlabel("天气", fontproperties=my_font)
    plt.legend(prop=my_font)

    plt.grid(alpha=0.6, linestyle="-")
    plt.savefig("./天气与营业额关系图.png")
    plt.show()


# 制作温度与营业额关系图
def paint_df():
    y_1 = df["最高温度"].values
    y_2 = df["营业收入"].values
    x_ = df.index
    fig = plt.figure(figsize=(20, 9), dpi=80)
    ax1 = fig.add_subplot(111)  # 制作双纵轴图表
    ax2 = ax1.twinx()  # 镜像

    l1 = ax1.plot(x_, y_1, label="温度", color="red")
    l2 = ax2.plot(x_, y_2, label="收入", color="cyan")

    ax1.set_xticks(x_[::7])
    ax1.set_yticks(range(-2, 42, 2))
    ax2.set_yticks(range(500, 11500, 500))
    ax1.set_ylabel("温度/℃", fontproperties=my_font)
    ax2.set_ylabel("收入/元", fontproperties=my_font)
    ax1.set_xlabel("时间", fontproperties=my_font)
    plt.title("温度与营业额关系图", fontproperties=my_font, fontsize=20)

    for tl in ax1.get_xticklabels():
        tl.set_rotation(45)  # 标签旋转

    lns = l1 + l2  # 双图标
    labs = [l.get_label() for l in lns]
    ax1.legend(lns, labs, prop=my_font, loc=2)

    plt.savefig("./温度与营业额关系图.png")
    plt.show()


# 制作周末营业额统计图
def paint_data_week(df_):
    df2 = df_
    bins = [0, 4, 8]
    lables = ["工作日", "周末"]
    df2["weekend"] = pd.cut(df2["week"], bins=bins, labels=lables)
    data2 = df2.groupby("weekend").resample("W")
    data2 = data2[["订单笔数", "营业收入"]].mean()
    df_week = data2.loc["工作日"]
    df_weekend = data2.loc["周末"]
    df_weekend.fillna(0, inplace=True)
    df_weekend.drop("2021-01-03", inplace=True)

    x1 = df_weekend.index
    x1 = [i.strftime("%m-%d") for i in x1]

    bar_width = 0.4
    x_1 = list(range(len(x1)))  # 图像在x轴显示位置
    x_2 = [i + bar_width for i in x_1]

    y_1 = df_weekend["营业收入"].values
    y_2 = df_week["营业收入"].values

    plt.figure(figsize=(23, 9), dpi=100)

    l1 = plt.bar(x_2, y_2, width=bar_width, label="工作日")
    l2 = plt.bar(x_1, y_1, width=bar_width, label="周末")

    plt.xlabel("时间", fontproperties=my_font)
    plt.ylabel("收入/元", fontproperties=my_font)
    plt.xticks(x_2, x1, rotation=45)
    plt.yticks(range(0, 9001, 500))
    plt.title("周末与工作日收入比关系图", fontproperties=my_font, fontsize=20)

    plt.legend([l1, l2], ["工作日", "周末"], loc=2, prop=my_font)

    plt.savefig("./周末与工作日收入比关系图.png")
    plt.show()


# 利用多元回归分析天气与是否周末对营业额的影响
def predict():
    d = {1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1}
    df["week"] = df["week"].map(d)  # 将week数据转换为周内：0，周末：1
    X = df[["最高温度", "week"]]
    y = df["营业收入"]

    regr = linear_model.LinearRegression()
    regr.fit(X, y)

    predicted_include = regr.predict([[32, 1]])  # 预测最高温度为32时，周末的营业额

    print(predicted_include)
    print(regr.coef_)  # 温度，是否周末与营业收入的关系


def main():
    paint_data1()
    paint_df()
    paint_data_week(df)
    predict()


if __name__ == "__main__":
    main()
