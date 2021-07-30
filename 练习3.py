import random
import easygui as g

g.msgbox("欢迎进入小游戏")
times = 3

secret = random.randint(1, 10)
title = "猜数字小游戏"
msg = "猜一猜我心中的数字吧(1~10)："
guess = g.integerbox(msg, title, lowerbound=0, upperbound=10)

while times > 0:

    if guess == secret:
        g.msgbox("牛啊！牛啊，猜对了！")
        g.msgbox("但是，猜中了也没有奖励！")
        break
    else:
        if guess > secret:
            g.msgbox("大了大了~~~")
            guess = g.integerbox(msg, title, lowerbound=0, upperbound=10)
        else:
            g.msgbox("小了，小了~~~")
            guess = g.integerbox(msg, title, lowerbound=0, upperbound=10)
        if times > 1:
            g.msgbox("再试一次吧：")
        else:
            g.msgbox("机会用光咯T_T")

    times = times - 1  # 用户每输入一次，可用机会就-1

g.msgbox("游戏结束，不玩啦^_^")
