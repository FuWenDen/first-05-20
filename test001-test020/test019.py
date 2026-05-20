# 需求：给一个数据类型，判断该数据类型是奇数还是偶数？
num = float(input("请输入一个要判断的数： "))
if num % 2 == 0:
    print(f"该数{num}是偶数")
else:
    print(f"该数{num}是奇数")
