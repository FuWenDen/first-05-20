#成员运算符 in 和 not in

a =[1,2,3,4,5,6]
print(1 in a)   #Ture
print(9 in a)   #False
#in 判断该元素在数组是否存在该值，存在返回Ture，否则返回False

print("===========================================")

print(1 not in a)   #False
print(9 not in a)   #Ture
#not in 判断该元素在数组是否存在该值，不存在返回Ture，否则返回False

print("===========================================")

#身份运算符 is 和 not is
#is 如果两个对象是同一个对象（即内存地址相同），则返回Ture，否则返回False
b = [1,2,3]
print(a is b)   #False

b = a
print(a is b)   #Ture

print("===========================================")

b = [1,2,3,4,5,6]
print(a is b)   #False,虽然元素相等，但此时 a 和 b 的内存地址是不同的。

print("===========================================")

print(a is not b)   #Ture
#is not 如果两个对象不是同一个对象（即内存地址相同），则返回Ture，否则返回False
