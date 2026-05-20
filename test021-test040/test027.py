#示例：跳过偶数,输出1到100的奇数
for i in range(1,100):
    if i %2 == 0:
        continue
    print(i)
