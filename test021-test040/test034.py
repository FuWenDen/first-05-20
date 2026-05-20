"""
NO.2:

    题目：给定一个整数列表，完成：
        1.新建列表 nums，包含至少 10 个任意整数
        2.找出列表中所有奇数，存到新列表 odds 并输出
        3.找出列表中最小的数并输出（不许用内置函数 min ()）
        4.把列表里所有负数都变成 0，其他数不变
        5.输出修改后的列表
        6.计算修改后列表的总和
        7.统计列表里大于 50的数有多少个
        8.把这些大于 50 的数放到新列表 big_nums
        9.输出处理后的所有结果
"""
nums = []
odds = []
new_nums = []
big_nums = []
count = 0

while True:
    quantity = int(input("请输入元素个数（至少 10 个任意整数）："))
    if quantity >= 10:
        break
    print("请输入至少为6的任意整数！请重新输入!")

while len(nums) != quantity:
    elements = int(input(f"请输入{quantity}个数"+f",当前是{len(nums)+1}个："))
    nums.append(elements)
print("原列表:",nums)

for i in range(len(nums)):
    if nums[i] % 2 != 0:
        odds.append(nums[i])
print("原奇数：", odds)

min_elements = nums[0]

for i in range(len(nums)):
    if nums[i] < min_elements:
        min_elements = nums[i]
print("列表中修改前最小的元素是:",min_elements)

for j in range(len(nums)):
    if nums[j] < 0:
        new_nums.append(nums[0])
    else:
        new_nums.append(nums[j])
print("修改后的列表:",new_nums)
print("修改后列表的和：",sum(new_nums))

for k in range(len(new_nums)):
    if new_nums[k] > 50:
        big_nums.append(new_nums[k])
        count += 1
print("大于 50 的数:",big_nums)
print(f"大于 50的数有{count}个")