"""列表（List）：Python 最常用的数组形式"""
my_shopping_list = ['orange', 'banana', 'mango', 'strawberry', 'apple']

print(my_shopping_list)                     # 打印全数组                 NO.1

print("====================================================")

for i in range(0,len(my_shopping_list)):    # for 循环遍历打印全数组      NO.2
    print(my_shopping_list[i],end="\t")

print("\n====================================================")

i = 0
while i < len(my_shopping_list):            # while 循环打印全数组       NO.3
    print(my_shopping_list[i],end="\t")
    i += 1

print("\n====================================================")

for element in my_shopping_list:            # 通过迭代器遍历数组         NO.4(最优)
    print(element,end="\t")

print("\n====================================================")

print(my_shopping_list[0],end="\t")         # 索引打印全数组            NO.5
print(my_shopping_list[1],end="\t")
print(my_shopping_list[2],end="\t")
print(my_shopping_list[3],end="\t")
print(my_shopping_list[4],end="\t")

print("\n====================================================")

del my_shopping_list[0]                 # 删除索引为0的元素            NO.6
print(my_shopping_list)

my_shopping_list.clear()                # 清处数组
print(my_shopping_list)                 # 输出： []