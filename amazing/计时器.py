import time


class Timer:
    def __init__(self):
        self.list1 = ["年", "月", "日", "小时", "分钟", "秒"]
        self.upshot = '计时未开始'
        self.lists = []
        self.begin = 0
        self.lasted = 0

    def __str__(self):
        return self.upshot

    __repr__ = __str__

    def __add__(self, other):
        uspshot = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lists[index] + other.lists[index])
            if result[index]:
                uspshot += (str(result[index])+self.list1[index])
        return uspshot

    # 定义开始计时时间
    def start(self):
        if self.begin:
            print("计时未结束。")
        else:
            self.begin = time.localtime()
            print("计时开始...")

    # 定义结束时间
    def stop(self):
        if not self.begin:
            print("计时未开始。")
        else:
            self.lasted = time.localtime()
            self.result()
            print("计时结束。")

    # 计算运行时间
    def result(self):
        self.lists = []
        self.upshot = "总共运行了"
        for index in range(6):
            self.lists.append(self.lasted[index] - self.begin[index])
            if self.lists[index]:
                self.upshot += (str(self.lists[index]) + self.list1[index])
        self.begin = 0
        self.lasted = 0
