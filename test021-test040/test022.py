# 计数器,求1到100的和.
Total = 0                        # 定义Total = 0,用于累计总和
num = 1                          # 定义num = 1,用于计数，同时计算循环次数(num-1)
while num <= 100:
      Total += num               #  Total = Total + num
      num   += 1                 #  num = num + 1
print("总和:", Total)             #  输出:“总和:5050”
print("循环次数:",num - 1)         #  输出:“循环次数:100”
print("循环结束！")                #  输出:“循环结束！”
                                #对比 test025.py 中的计数器写法

print("===========================================")

"""
break 语句的作用:
● 立即终止整个循环
● 跳出循环体，执行循环后的代码
● 请与test026.py中的continue用法一起学
"""

count = 0
while True:
    print(f"第{count}次循环！")
    count += 1
    if count == 10:             # 如果 count 自增到 10 时
        break                   # 用 break 语句来终止 while 循环
print("输出结束！！")

"""
输出结果:
    第0次循环！
    第1次循环！
    第2次循环！
    第3次循环！
    第4次循环！
    第5次循环！
    第6次循环！
    第7次循环！
    第8次循环！
    第9次循环！
"""