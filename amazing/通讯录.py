import easygui as g

memory = dict()
g.msgbox("欢迎来到通讯录小程序，本程序具有以下功能：" + "\n" + "查询联系人资料" + "\n" + "插入新的联系人" + "\n" + "删除已有联系人" + "\n" + "退出通讯录程序")

while 1:
    msg = "请选择你的操作"
    title = "通讯录"
    strs = g.buttonbox(msg, title, choices=('查询', "添加", "删除", "退出"))
    if strs == "查询":
        msg = "请输入你要查询的姓名："
        title = "查询"
        name = g.enterbox(msg, title)
        try:
            g.msgbox(name + ":" + memory[name])
        except KeyError:

            g.msgbox("您输入的用户名已存在 ---", name + ":" + memory[name])
            g.msgbox("你输入的名字不在通讯录中。")
    if strs == "添加":
        msg = "请输入你要加入的联系人的姓名："
        title = "添加"
        name = g.enterbox(msg, title)
        if name in memory:
            string = g.msgbox("是否修改用户信息：YES/NO")
            if string == "YES" or "yes":
                msg = "请输入更改的用户电话："
                title = "输入"
                memory[name] = g.enterbox(msg, title)
        else:
            msg = "请输入用户电话："
            title = "输入"
            memory[name] = g.enterbox(msg, title)
    if strs == "删除":
        msg = "请输入你要删除的联系人姓名："
        title = "删除"
        name = g.enterbox(msg, title)
        try:
            dict.pop(memory[name])
        except KeyError:
            g.msgbox("你输入的联系人不存在。")
    if strs == "退出":
        break
g.msgbox("感谢你的使用！")
