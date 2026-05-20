"""
NO.1:

    题目:编写一个 Python 程序：
        1.定义一个列表 nums，里面包含任意 8 个整数（可重复）
        2.输出这个列表
        3.计算并输出列表中所有偶数的和
        4.输出列表中大于平均值的所有元素

    输出:原列表：[1, 2, 3, 4, 5, 6, 7, 8]
        偶数和：20
        平均值：4.5
        大于平均值的元素： [5, 6, 7, 8]
"""
nums = []
even_nums = []
above_avg_nums = []

while len(nums) < 8:
    elements = input("请输入任意 8 个整数（可重复）：")
    nums.append(int(elements))

print("原列表:",nums)

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        even_nums.append(nums[i])

print("偶数和:",sum(even_nums))

average =sum(nums) / len(nums)

print("平均值:",average)

for j in range(len(nums)):
    if nums[j] > average:
        above_avg_nums.append(nums[j])

print("大于平均值的元素:",above_avg_nums)