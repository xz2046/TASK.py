symbols = r'''!@#$%^&*_-+=~`'''
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
passed = input("请输入您的密码：")
length = len(passed)
while (passed.isspace() or length == 0):
       passed = input("您输入的密码为空（或空格），请重新输入：")
       length = len(passed)
       
       # 单纯想打个备注
if length <= 8:
    flag_led = 1
elif 8 < length <= 12:
    flag_led = 2
else:
    flag_led = 3

flag_con= 0
for each in passed:
    if each in symbols:
        flag_con += 1
        break
for each in passed:
    if each in chars:
        flag_con += 1
        break
for each in passed:
    if each in nums:
        flag_con += 1
        break

while 1:
    if length == 1 or flag_con < 2:
        print("您的密码等级为“低”，建议重新设置。",end=" ")
    elif flag_led == 3 and flag_con == 3 and (passed[0] in  chars):
        print("您的密码等级为“高”，请继续保持。")
        break
    else:
        print("您的密码等级为“中”。")

    print("请按以下方式提升您的密码安全级别：\n\
    \t1. 密码必须由数字、字母及特殊字符三种组合\n\
    \t2. 密码只能由字母开头\n\
    \t3. 密码长度不能低于16位")
    break
