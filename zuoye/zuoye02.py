# BMI = 体重 / (身高 ** 2)    注意 ：kg  / (m ** 2)
user_weight = float(input("请输入体重（kg）： "))
user_height = float(input("请输入身高（m）："))
user_BMI = user_weight / user_height ** 2
print("你的BMI是: "+str(user_BMI))
'''
低于18.5为体重过轻；
18.5~24.9为健康体重；
25.0~29.9为超重；
30.0及以上为肥胖
'''
"""
if 条件语句:
    执行语句
    执行语句
    执行语句
    ......
else:
    执行语句
    执行语句
    执行语句
    ......
    注意执行语句前必须缩进以此判断是否是属于if 或者 else 的语句
"""
print("======================")
if user_BMI < 18.5:
    print("体重过轻!")
if 18.5 <= user_BMI <= 24.9:
    print("健康体重！")
if 25.0 <= user_BMI <= 29.9:
    print("超重！")
if user_BMI >= 30.0:
    print("肥胖！")