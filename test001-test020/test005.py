from test004 import user_name
from test004 import age_01
k = 'guang dong qing gong'
print(len(k))
print(k[1])
print(k[len(k)-1])
print(len(' '))  #长度为一
print(len(''))   #长度为零
print(len('s'))  #长度为一
print(len('!'))  #长度为一
print(len('6'))  #长度为一
print(len('长度为一'))   #长度为四
print(len("\n"))  #长度为一
print("hello"[3]) #打印字符串第三位，首字母为0，依次排序
print("hi "+user_name)
print("hi "+user_name[0]+" "+user_name[3])
print(type("hello"))
print("==========================================")
b1 = True
b2 = False
c1 = None
print(type(b1))
print(type(b2))
print(type(c1))
print(type(age_01))   #age_01=20.26
print(type(1))