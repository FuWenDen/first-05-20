#字符串是由零个或多个字符组成的序列，可以使用单 引号、双 引号或三 引号表示
# 字符串示例
name = "Alice"
message = 'Hello, world!'
paragraph = """这是一个多行字符串，
可以包含多个段落。"""

print("===============================================")

# 字符串索引和切片
s = "Python"
print(s[0])       # 索引: 'P'
print(s[-1])      # 负索引: 'n'
print(s[2:5])     # 切片: 'tho'
print(s[:3])      # 从头开始: 'Pyt'
print(s[3:])      # 到末尾: 'hon'

print("===============================================")
# 字符串操作
a = "Hello"
b = "World"
print(a + " " + b)  # 字符串连接: 'Hello World'
print(a * 3)        # 字符串重复: 'HelloHelloHello'
print(len(a))       # 字符串长度: 5

print("===============================================")

# 字符串方法
text = "   Hello, Python!   "
print(text.strip())     # 去除空白: 'Hello, Python!'
print(text.upper())     # 转为大写: '   HELLO, PYTHON!   '
print(text.lower())     # 转为小写: '   hello, python!   '
print(text.replace("Python", "World"))  # 替换: '   Hello, World!   '
print(text.split(","))  # 分割: ['   Hello', ' Python!   ']

print("===============================================")

# 字符串格式化
age = 25
print(f"{name} 今年 {age} 岁。")  # f-string: 'Alice 今年 25 岁。'
print("{} 今年 {} 岁。".format(name, age))  # format 方法: 'Alice 今年 25 岁。'