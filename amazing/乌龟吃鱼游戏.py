"""
1. 游戏编程：按以下要求定义一个乌龟类和鱼类并尝试编写游戏。
假设游戏场景为范围（x, y）为0<=x<=10，0<=y<=10
游戏生成1只乌龟和10条鱼
它们的移动方向均随机
乌龟的最大移动能力是2（Ta可以随机选择1还是2移动），鱼儿的最大移动能力是1
当移动到场景边缘，自动向反方向移动
乌龟初始化体力为100（上限）
乌龟每移动一次，体力消耗1
当乌龟和鱼坐标重叠，乌龟吃掉鱼，乌龟体力增加20
鱼暂不计算体力
当乌龟体力值为0（挂掉）或者鱼儿的数量为0游戏结束
"""

import random as r

range_x = [0, 10]
range_y = [0, 10]


class Tortoise:
    def __init__(self):
        # 初始体力
        self.power = 100
        # 初始位置
        self.x = r.randint(range_x[0], range_y[1])
        self.y = r.randint(range_x[0], range_y[1])

    def move(self):
        # 随机移动位置
        new_x = self.x + r.choice([1, 2, -1, -2])
        new_y = self.y + r.choice([1, 2, -1, -2])
        # 检查是否超出边界
        if new_x > range_x[1]:
            self.x = range_x[1] - (new_x - range_x[1])
        elif new_x < range_x[0]:
            self.x = range_x[0] - (new_x - range_x[0])
        else:
            self.x = new_x
        if new_y > range_y[1]:
            self.y = range_y[1] - (new_y - range_y[1])
        elif new_y < range_y[0]:
            self.y = range_y[0] - (new_y - range_y[0])
        else:
            self.y = new_y
        self.power -= 1
        return self.x, self.y

    def eat(self):
        self.power += 20
        if self.power > 100:
            self.power = 100


class Fish:
    def __init__(self):
        self.x = r.randint(range_x[0], range_y[1])
        self.y = r.randint(range_x[0], range_y[1])

    def move(self):
        new_x = self.x + r.choice([1, -1])
        new_y = self.y + r.choice([1, -1])
        if new_x > range_x[1]:
            self.x = range_x[1] - (new_x - range_x[1])
        elif new_x < range_x[0]:
            self.x = range_x[0] - (new_x - range_x[0])
        else:
            self.x = new_x
        if new_y > range_y[1]:
            self.y = range_y[1] - (new_y - range_y[1])
        elif new_y < range_y[0]:
            self.y = range_y[0] - (new_y - range_y[0])
        else:
            self.y = new_y
        return self.x, self.y


tortoise = Tortoise()
fish = []
for i in range(0, 10):
    new_fisc = Fish()
    fish.append(new_fisc)

count = 0
while True:
    if len(fish) == 0:
        print("鱼儿被吃完了，游戏结束！")
        break
    elif tortoise.power == 0:
        print("乌龟体力没了，游戏结束。")
        break

    sums = tortoise.move()
    for each_fisc in fish[:]:
        if each_fisc.move() == sums:
            tortoise.eat()
            fish.remove(each_fisc)
            print("鱼儿被吃掉了")
            count += 1
print("乌龟吃了%s条鱼儿" % count)
