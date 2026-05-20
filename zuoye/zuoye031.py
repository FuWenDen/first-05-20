while True:
    try:
        use_grade = float(input("请输入成绩(0-100分)： "))
        if 0 <= use_grade <= 100 :
            break
        else:
            print("输入的成绩无效 ")
    except ValueError:
        print("请输入 0-100 之间的数值")
#若成绩超出 0-100 范围，提示 “输入的成绩无效，请重新输入 0-100 之间的数值
#使用条件判断 + 多条件分支 + 逻辑运算，根据成绩范围评定等级
if use_grade >= 90 :
    print("优秀")
    # 90 分及以上 → 优秀
elif 80 <= use_grade <= 89:
    print("良好")
    # 80~89 分   → 良好
elif 70 <= use_grade <= 79 :
    print("中等")
    # 70~79分    → 中等
elif 60 <= use_grade <= 69 :
    print("及格")
    # 60~69分    → 及格
else :
    print("不及格")
    # 60 分以下  → 不及格
    match use_grade:
        case grade if use_grade >= 90:
            print("A")
        case grade if 80 <= use_grade <= 89:
            print("B")
        case grade if 70 <= use_grade <= 79:
            print("C")
        case grade if 60 <= use_grade <= 69:
            print("D")
        case grade if 0 < use_grade < 60:
            print("E")
        case _:
            print("Error_Grade,请输入 0-100 之间的数值")