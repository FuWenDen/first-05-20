m = 2025
n = 2025.2024
k = 'ABCDEFG'
l = True
print(type(m))
print(type(n))
print(type(k))
print(type(l))
print('=================================')
new_type_01 = str(m)
print(type(new_type_01))
new_type_02 = str(n)
print(type(new_type_02))
new_type_03 = str(k)
print(type(new_type_03))
new_type_04 = str(l)
print(type(new_type_04))
print(new_type_04+" or false")
print('=================================')
new_type_05 = int(l)
print(type(new_type_05))
print(new_type_05) #输出1,既false
print('=================================')
print('=================================')

#浮点数（float）类型转换整型（int）会丢失精度
print(n)
NEW_N = new_type_06 = int(n)
print(NEW_N)
print('=================================')
q = 2025.6
Q = int(q)
print(q)
print(Q)   # 2025
QQ = float(Q)
print(QQ)  # 2025.0

print('=================================')
'''
注意不是所有数据类型都可以随便转！！！
如果不符合转换的话，输出会报错！！！
'''
print(bool(0))     # false
print(bool(1))     # True
print(bool(""))    # false
print(bool([]))    # false
print(bool("abc")) # True
print(bool([0]))   # True
