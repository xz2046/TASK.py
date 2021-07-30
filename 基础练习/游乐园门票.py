'''
按照以下要求定义一个游乐园门票的类，并尝试计算2个成人+1个小孩平日票价。
平日票价100元
周末票价为平日的120%
儿童半票

答：面向对象编程的难点在于思维的转换。
'''


class Ticket:
    def __init__(self, weekend=False, child=False):
        self.exp = 100  # 定义正常票价
        if weekend:  # 定义周末票价算法
            self.inc = 1.2
        else:
            self.inc = 1
        if child:  # 定义儿童票价算法
            self.discount = 0.5
        else:
            self.discount = 1

    def calcPrice(self, num):  # 定义计算方法
        return self.exp * self.inc * self.discount * num  # 正常票价 * 是否为周末的价格倍数 * 是否有儿童的价格倍数


adult = Ticket()  # 实例化
child = Ticket(child=True)  # 调用方法  参数：周末默认False  儿童定义为True
print("2个成人 + 1个小孩平日票价为：%.2f" % (adult.calcPrice(2) + child.calcPrice(1)))
# 输出 成人（2） + 小孩（1）的结果
