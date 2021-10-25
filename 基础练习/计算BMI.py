print('----欢迎使用BMI计算程序----')
name=input('请键入您的姓名:')
height=eval(input('请键入您的身高(m):'))
weight=eval(input('请键入您的体重(kg):'))
BMI=float(float(weight)/(float(height)**2))
#公式
if BMI<=18.4:
    print('姓名:',name,'身体状态:偏瘦')
elif BMI<=23.9:
    print('姓名:',name,'身体状态:正常')
elif BMI<=27.9:
    print('姓名:',name,'身体状态:超重')
elif BMI>=28:
    print('姓名:',name,'身体状态:肥胖')

print('感谢',name,'使用本程序,祝您身体健康!')
