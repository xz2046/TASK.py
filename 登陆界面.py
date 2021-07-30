import easygui as g


class Login_interface:
    def __init__(self):
        self.store = {}
        self.name = []
        self.namedict = {}

    def verification(self):
        while True:
            msg = "请输入以下信息："
            title = "账号登录"
            filednames = ["用户名", "密码"]
            word = g.multpasswordbox(msg, title, filednames)
            str1 = word[0]
            if str1 in self.name:
                if self.namedict not in self.store:
                    g.msgbox("密码或用户名错误，请重新输入")
                else:
                    g.msgbox("登陆成功")
            else:
                msg = "用户不存在，是否立即注册！"
                title = "验证"
                strs = g.buttonbox(msg, title, choices=("是", "否"))
                if strs == "是":
                    Login_interface.addword()
                else:
                    break

    def addword(self):
        while True:
            msg = "请输入以下信息："
            title = "注册"
            filedname = ["用户名", "密码", "确认密码"]
            word = g.multenterbox(msg, title, filedname)
            if word[1] == word[2]:
                self.namedict = {word[0]: word[1]}
                self.store.update(self.namedict)
                self.name.append(word[0])
                break
            else:
                g.msgbox("两次密码不同，请重新输入。")

    def rsversed(self):
        self.store.pop(self.namedict)


log = Login_interface()
log.verification()
