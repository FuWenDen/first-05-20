#input("里面写提示: ")
#此时将会等待输入如：
year = input("请输入年份：")
print("今年 "+year+" 年了!")
print("----------------------")
#c = year - 10
#print(c)
#这个代码会报错，因为input返回的是字符串。
print("----------------------")
#正确做法：
year_after = int(input("请输入年份："))
#获取输入的年份并转换为整数
c = year_after + 10
#将整数转换为字符串后拼接输出
print("after ten years is "+str(c))

