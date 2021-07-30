import random
import easygui as g


class Guessnums:

    def __init__(self):
        self.str1 = 10
        self.time = 4
        self.msg = "猜一猜我心中的数字吧(0-10)"
        self.str2 = "简单模式，你有4次机会！"

    def guess(self):
        g.msgbox(self.str2)
        secret = random.randint(0, self.str1)
        title = "猜数字小游戏"
        guess = g.integerbox(self.msg, title, lowerbound=0, upperbound=self.str1)
        while self.time:
            self.time = self.time - 1
            if guess == secret:
                g.msgbox("牛啊！牛啊，猜对了！")
                return True
            elif guess < secret:
                g.msgbox("小了，小了~~~")
                if self.time > 0:
                    msg = ("再试一次吧,还有%d次机会" % self.time)
                    guess = g.integerbox(msg, title, lowerbound=0, upperbound=self.str1)
                else:
                    g.msgbox("机会用光咯T_T")
            else:
                g.msgbox("大了大了~~~")
                if self.time > 0:
                    msg = ("再试一次吧,还有%d次机会" % self.time)
                    guess = g.integerbox(msg, title, lowerbound=0, upperbound=self.str1)
                else:
                    g.msgbox("机会用光咯T_T")
        g.msgbox("游戏结束，不玩啦^_^")


class Guessnum2(Guessnums):
    def __init__(self):
        self.str1 = 30
        self.time = 6
        self.msg = "猜一猜我心中的数字吧(0-30)"
        self.str2 = "中等模式，你有5次机会！"


class Guessnum3(Guessnums):
    def __init__(self):
        self.str1 = 100
        self.time = 9
        self.msg = "猜一猜我心中的数字吧(0-100)"
        self.str2 = "困难模式，你有9次机会！"


g1 = Guessnums()
g2 = Guessnum2()
g3 = Guessnum3()

g.msgbox("欢迎进入小游戏")
if g1.guess():
    if g2.guess():
        g3.guess()
