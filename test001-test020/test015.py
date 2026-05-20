# 单分支示例：判断一个数是否为正数

num = 15
if num > 0:
    print(f"{num} 是正数")

print("===============================")

# 双分支示例：判断一个数是正数还是非正数
num = -5
if num > 0:
    print(f"{num} 是正数")
else:
    print(f"{num} 是非正数")

print("===============================")

"""
多分支结构用于处理多种情况，通过 elif 关键字添加更多条件分支。
del score is in 0 to 120
elif = else if
执行流程：
1. 依次计算每个条件表达式
2. 一旦某个条件为 True，执行对应的代码块，然后跳过剩余分支
3. 如果所有条件都为 False，执行 else 后的代码块（如果有 else 的话）
"""

score = 121
if score < 60:
    print("成绩不合格")
elif 60 <= score < 76:
    print("成绩合格")
elif 76 <= score < 86:
    print("成绩良好")
elif 86 <= score < 96:
    print("成绩优秀")
elif 96 <= score <= 120:
    print("成绩优秀+")
else:
    print("成绩格式不正确")

print("===============================")

#嵌套选择结构是在一个条件分支内部再嵌套其他条件判断。

#需求  判断年龄
#年龄 判断是否成年 18岁
# 如果未成年 则继续判断 1-3岁婴儿 4-6岁 幼儿园 7-12岁小学  13-15岁初中 16-17 高中
# 如果成年 则继续判断 18-21 大学  22-30岁 努力工作挣钱   31-45岁青年 46-60岁中年  61-75 老年

age = 99
if age<18:
    print("年龄是未成年")
    if 1 <= age <= 3:
        print("是为婴儿")
    elif 4 <= age <= 6:
        print("上幼儿园")
    elif 7 <= age <= 12:
        print("上小学")
    elif 13 <= age <= 15:
        print("上初中")
    elif 16 <= age <= 17:
        print("上高中")
else:
    print("年龄是为成年")
    if 18 <= age <= 21:
        print("上大学")
    elif 22 <= age <= 30:
        print("努力工作挣钱")
    elif 31 <= age <= 45:
        print("青年")
    elif 46 <= age <= 59:
        print("中年人")
    elif 60 <= age <= 75:
        print("老年人")
    else:
        print("长命百岁")

print("===============================")
