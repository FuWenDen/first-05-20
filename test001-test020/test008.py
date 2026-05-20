"""

python里的逻辑运算符有 and or 和 not
分别表示：
与（and。全真才真，一假全假）
或（or。有真就真，全假才假）
非（not）（取反）（对单）（真变假，假变真）
同一行的优先级：not > and > or
可通过括号改变顺序：先算括号里面的，再算括号外面的。

"""


print("==============================================")
'''
数值类型：整数 (int)、浮点数 (float)
布尔类型：True(真)/False（否）
文本类型：字符串 (str)
序列类型：列表 (list)、元组 (tuple)
映射类型：字典 (dict)
集合类型：集合 (set)
python use type() to cheek the form
'''

x = 10 #int
y = 3
user = 'deng fu wen' #str
print('hi '+user)
is_student = True  #bool
know = not is_student  #bool 取反
print(know) #False
print(is_student) #Ture
print("===============================================")

print(x+y)  #10+3=13
print(x*y)  #10X3=30
print(x/y)  #10除3=3.3333....
print(x//y) #10整除3=3
print(x%y)  #10除3的余数是1,因为3X3=9,10除3=3余1.
k = 10
j = 2
print(k/j)  #10除2=5,5是整数，但能整除的一般会输出为5.0,  5.0是浮点数
print("===============================================")

#1.23X10**6(1.23乘10的6次方)被打印出来是以1.23e6表示的，其表示1230000.0(是浮点数)
#采用的是科学计数法来表示浮点数,e 代表 10 的幂次方
# 浮点数示例
pi = 3.14
temperature = -273.15
large_number = 1.23e6  # 等同于 1.23 * 10^6 = 1230000.0
print(large_number)
print(type(large_number))
print(temperature)
print("===============================================")

# 浮点数运算
x = 1.5
y = 2.7
print(x + y)  # 加法: 4.2
print(x * y)  # 乘法: 4.050000000000001

# 浮点数精度问题
a = 0.1
b = 0.2
print(a + b)  # 输出: 0.30000000000000004 (浮点数精度限制)
print("===============================================")

#布尔值 ture(真) or false(假)
#0为真 非0为假
user_man = True  # 0,定义为男
user_woman= False  # 非0（一般为1），定义为女
print(type(user_man))
print(user_man)
print(user_woman)

print("===============================================")
#布尔值运算
small = 10
large = 20
print(small < large)   # 0
print(small <= large)  # 0
print(small > large)   # 1
print(small == large)  # 1
print(small != large)  # 0
print("===============================================")

small = 20
large = 20
print(small <= large) # 0
print(small >= large) # 0
print(small == large) # 0
print(small != large) # 1
print("===============================================")

# 逻辑运算
a = True
b = False
c = False
print(a and b)       # 逻辑与: False   (结果为真，必须要and左右两边都为真)
print(a and c)       # 逻辑与: False   (两边为假，结果也为假)
print(a or b)        # 逻辑或: True    (结果为真，只需or左右两边有真)
print(b or c)        # 逻辑或: False   (两边都为假，没有真)
print(not a)         # 逻辑非: False   (取反，真变假，假变真)
print(not b)         # 逻辑非: True    (取反，真变假，假变真)
print(a and not c)   # 逻辑与: Ture  (结果为真，必须要and左右两边都为真)
print(type(a), type(b),type(c))
                  # 都是布尔值，可以布尔值运算,一般比较是否相等.
print(b == c)
print(b != c)
# "and" != "=="
# print(a == not b )表达是错的！！
