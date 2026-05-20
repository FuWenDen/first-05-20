#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ===================== 任务1：初始化数据（基础数据结构） =====================
# 定义学生列表，存储所有学生信息
# 每个元素为字典，包含学号(id)、姓名(name)、年龄(age)、成绩(score)四个核心字段
students = [
    {"id": "001", "name": "张三", "age": 18, "score": 85},  # 学生1
    {"id": "002", "name": "李四", "age": 19, "score": 92},  # 学生2
    {"id": "003", "name": "王五", "age": 17, "score": 78}  # 学生3
]

# 显示欢迎信息（使用f-string格式化，动态展示学生数量）
# len(students)获取列表长度，即当前学生总数
print(f"欢迎使用学生信息管理系统！当前有{len(students)}名学生。")


# ===================== 任务2：功能函数实现（核心业务逻辑） =====================
def show_menu():
    """
    显示系统主菜单
    功能：为用户提供清晰的操作选项，提升交互体验
    格式：使用等号分隔，菜单居中显示，视觉更美观
    """
    print("=" * 30)                     # 分隔线，提升可读性
    print("1. 显示所有学生")              # 选项1：查询全部
    print("2. 添加学生")                 # 选项2：新增数据
    print("3. 查找学生")                 # 选项3：精准查询
    print("4. 修改学生信息")             # 选项4：更新数据
    print("5. 删除学生")                 # 选项5：删除数据
    print("6. 统计信息")                 # 选项6：数据统计
    print("0. 退出系统")                 # 选项0：退出程序
    print("=" * 30)                     # 分隔线


def show_all_students():
    """
    显示所有学生信息
    逻辑：
    1. 先检查学生列表是否为空，空则提示无数据
    2. 非空则遍历列表，格式化输出每个学生的信息
    格式化：使用format方法，设置字段宽度（如:<4），保证输出对齐
    """
    print("\n【所有学生信息】")             # 功能标题，区分不同操作
    if not students:                     # 等价于 len(students) == 0，检查列表是否为空
        print("暂无学生信息！")            # 空数据提示
        return                          # 结束函数执行

    # 遍历学生列表，逐个输出信息
    for student in students:
        # format格式化：{:<4} 表示左对齐，占4个字符宽度，保证输出整齐
        print("学号:{:<4} 姓名:{:<4} 年龄:{:<3} 成绩:{:<3}".format(
            student["id"],  # 学号字段
            student["name"],  # 姓名字段
            student["age"],  # 年龄字段
            student["score"]  # 成绩字段
        ))
    print()  # 空行分隔，提升视觉效果


def add_student():
    """
    添加学生信息
    核心逻辑：
    1. 输入学号：非空 + 唯一性检查（避免重复）
    2. 输入姓名：非空检查
    3. 输入年龄：非空 + 数字验证 + 合理范围（1-99）
    4. 输入成绩：非空 + 数字验证 + 合理范围（0-100）
    5. 组装字典，添加到学生列表
    """
    print("\n【添加学生】")  # 功能标题

    # 1. 学号输入与验证（核心：唯一性）
    while True:  # 循环直到输入有效学号
        student_id = input("请输入学号：").strip()  # strip()去除首尾空格
        if not student_id:  # 检查是否为空
            print("学号不能为空！请重新输入。")
            continue  # 重新输入

        # 检查学号是否重复：遍历列表，判断是否有相同id
        # any()函数：只要有一个元素满足条件就返回True
        is_duplicate = any(s["id"] == student_id for s in students)
        if is_duplicate:
            print(f"学号{student_id}已存在！请重新输入。")
            continue  # 重新输入

        break  # 学号有效，退出循环

    # 2. 姓名输入与验证（核心：非空）
    while True:
        name = input("请输入姓名：").strip()
        if name:  # 非空即有效
            break
        print("姓名不能为空！请重新输入。")

    # 3. 年龄输入与验证（核心：数字 + 范围）
    while True:
        age_input = input("请输入年龄：").strip()
        try:
            age = int(age_input)  # 转换为整数（非数字会触发ValueError）
            if 0 < age < 100:     # 年龄范围限制（合理值）
                break
            print("年龄应在1-99之间！请重新输入。")
        except ValueError:        # 输入非数字时触发
            print("年龄必须是数字！请重新输入。")

    # 4. 成绩输入与验证（核心：数字 + 范围）
    while True:
        score_input = input("请输入成绩：").strip()
        try:
            score = float(score_input)  # 转换为浮点数（支持小数成绩）
            if 0 <= score <= 100:       # 成绩范围限制（0-100）
                break
            print("成绩应在0-100之间！请重新输入。")
        except ValueError:              # 输入非数字时触发
            print("成绩必须是数字！请重新输入。")

    # 5. 组装新学生字典，添加到列表
    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "score": score
    }
    students.append(new_student)                        # 列表append方法：在末尾添加新元素
    print(f"学生{name}（学号{student_id}）添加成功！\n")   # 成功提示


def find_student():
    """
    查找学生信息
    核心逻辑：
    1. 接收用户输入的关键词（学号/姓名）
    2. 遍历列表，筛选出学号或姓名包含关键词的学生
    3. 展示查找结果（找到/未找到）
    """
    print("\n【查找学生】")  # 功能标题
    keyword = input("请输入要查找的学号或姓名：").strip()
    if not keyword:  # 关键词为空检查
        print("查找关键词不能为空！\n")
        return

    # 列表推导式：筛选匹配的学生
    # 匹配规则：关键词等于学号 或 关键词等于姓名
    found_students = [s for s in students if keyword in (s["id"], s["name"])]

    # 展示结果
    if found_students:  # 找到匹配学生
        print(f"找到{len(found_students)}名匹配的学生：")
        for s in found_students:
            print(f"学号:{s['id']} 姓名:{s['name']} 年龄:{s['age']} 成绩:{s['score']}")
    else:               # 未找到
        print("未找到匹配的学生！")
    print()             # 空行分隔


def update_student():
    """
    修改学生信息
    核心逻辑：
    1. 按学号查找目标学生（学号唯一，作为主键）
    2. 展示当前信息，允许用户修改姓名/年龄/成绩（回车保持原信息）
    3. 直接更新字典对应字段的值
    """
    print("\n【修改学生信息】")  # 功能标题
    student_id = input("请输入要修改的学生学号：").strip()
    if not student_id:        # 学号为空检查
        print("学号不能为空！\n")
        return

    # 查找目标学生：遍历列表，匹配学号
    target_student = None     # 初始化目标学生为None
    for s in students:
        if s["id"] == student_id:
            target_student = s
            break             # 找到后退出循环

    if not target_student:    # 未找到目标学生
        print(f"学号{student_id}不存在！\n")
        return

    # 展示当前信息
    print(
        f"当前信息：学号:{target_student['id']} 姓名:{target_student['name']} 年龄:{target_student['age']} 成绩:{target_student['score']}")

    # 修改姓名：回车则保持原信息
    new_name = input("请输入新姓名（回车保持不变）：").strip()
    if new_name:  # 输入非空则更新
        target_student["name"] = new_name

    # 修改年龄：输入验证 + 回车保持原信息
    while True:
        new_age = input("请输入新年龄（回车保持不变）：").strip()
        if not new_age:  # 回车则退出循环，不修改
            break
        try:
            new_age = int(new_age)
            if 0 < new_age < 100:  # 范围验证
                target_student["age"] = new_age  # 更新年龄
                break
            print("年龄应在1-99之间！请重新输入。")
        except ValueError:
            print("年龄必须是数字！请重新输入。")

    # 修改成绩：输入验证 + 回车保持原信息
    while True:
        new_score = input("请输入新成绩（回车保持不变）：").strip()
        if not new_score:  # 回车则退出循环，不修改
            break
        try:
            new_score = float(new_score)
            if 0 <= new_score <= 100:                # 范围验证
                target_student["score"] = new_score  # 更新成绩
                break
            print("成绩应在0-100之间！请重新输入。")
        except ValueError:
            print("成绩必须是数字！请重新输入。")

    # 展示修改后信息
    print(f"学号{student_id}的学生信息修改成功！")
    print(
        f"修改后：学号:{target_student['id']} 姓名:{target_student['name']} 年龄:{target_student['age']} 成绩:{target_student['score']}\n")


def delete_student():
    """
    删除学生信息（任务2-5）
    核心逻辑：
    1. 按学号查找目标学生的索引（便于删除）
    2. 确认删除操作（防止误删）
    3. 用pop()方法删除列表中指定索引的元素
    """
    print("\n【删除学生】")  # 功能标题
    student_id = input("请输入要删除的学生学号：").strip()
    if not student_id:  # 学号为空检查
        print("学号不能为空！\n")
        return

    # 查找目标学生的索引：enumerate()返回(索引, 元素)
    target_index = -1  # 初始化索引为-1（表示未找到）
    for idx, s in enumerate(students):
        if s["id"] == student_id:
            target_index = idx
            break

    if target_index == -1:  # 未找到目标学生
        print(f"学号{student_id}不存在！\n")
        return

    # 确认删除
    target_student = students[target_index]  # 获取目标学生字典
    confirm = input(f"确定删除{target_student['name']}（学号{student_id}）吗？(y/n)：").strip().lower()
    if confirm == "y":  # 输入y（不区分大小写）则删除
        students.pop(target_index)  # 列表pop方法：删除指定索引的元素
        print(f"学生{target_student['name']}删除成功！\n")
    else:  # 其他输入则取消
        print("删除操作已取消。\n")


def show_statistics():
    """
    学生信息统计（任务2-6）
    核心逻辑：
    1. 统计学生总数（列表长度）
    2. 计算平均成绩（总分/总数）
    3. 找到最高分、最低分（max/min函数）
    格式化：混合使用f-string和format，满足作业要求
    """
    print("\n【学生信息统计】")  # 功能标题
    if not students:          # 空列表检查
        print("暂无学生信息，无法统计！\n")
        return

    # 基础统计
    total_students = len(students)              # 学生总数
    scores = [s["score"] for s in students]     # 提取所有学生的成绩，生成成绩列表
    avg_score = sum(scores) / total_students    # 平均成绩
    max_score = max(scores)                     # 最高分
    min_score = min(scores)                     # 最低分

    # 格式化输出统计结果
    print(f"学生总数：{total_students} 人")           # f-string格式化
    print("平均成绩：{:.2f} 分".format(avg_score))    # format格式化，保留2位小数
    print(f"最高成绩：{max_score} 分")                # f-string格式化
    print(f"最低成绩：{min_score} 分\n")              # f-string格式化


# ===================== 任务3：主循环和菜单（程序入口） =====================
def main():
    """
    主程序循环
    核心逻辑：
    1. 无限循环显示菜单，直到用户输入0退出
    2. 根据用户输入的选项，调用对应功能函数
    3. 输入错误时提示重新输入
    """
    while True:                                     # 无限循环，直到break
        show_menu()                                 # 显示菜单
        choice = input("请选择操作（0-6）：").strip()  # 获取用户选择

        # 分支判断：根据选择调用对应函数
        if choice == "1":
            show_all_students()  # 显示所有学生
        elif choice == "2":
            add_student()       # 添加学生
        elif choice == "3":
            find_student()      # 查找学生
        elif choice == "4":
            update_student()    # 修改学生信息
        elif choice == "5":
            delete_student()    # 删除学生
        elif choice == "6":
            show_statistics()   # 统计信息
        elif choice == "0":
                                # 退出前显示统计信息（任务3-3）
            show_statistics()
            print("感谢使用学生信息管理系统！再见\n")
            break               # 退出循环，结束程序
        else:
            # 输入错误提示
            print("输入错误！请选择0-6之间的数字。\n")


# 程序入口：只有直接运行该脚本时，才执行main()函数
if __name__ == "__main__":
    main()