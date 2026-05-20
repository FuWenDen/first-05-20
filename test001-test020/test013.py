my_shopping_list = []
print(type(my_shopping_list))           # 此为列表类型
print("================================")

my_shopping_list.append("apple")        # 用 列表名.append("新加入的元素") 方法来写入元素
print(my_shopping_list)                 # ['apple']
print(len(my_shopping_list))            # 将输出元素个数,输出结果是 1

print("================================")

my_shopping_list.append("banana")       # 用 列表名.append("新加入的元素") 方法来写入元素
print(my_shopping_list)                 # ['apple', 'banana']
print(len(my_shopping_list))            # 将输出元素个数,输出结果是 2

print("================================")

my_shopping_list.append("orange")
print(my_shopping_list)                 # ['apple', 'banana', 'orange']

my_shopping_list.remove("apple")        # 用 列表名.remove("要移除的元素") 方法来删除元素
print(my_shopping_list)                 # ['banana', 'orange']

print("================================")

my_shopping_list.append("mango")        # 加入mango
my_shopping_list.append("strawberry")   # 加入strawberry
my_shopping_list.append("apple")        # 加入apple

print("================================")

print(my_shopping_list)                 # ['banana', 'orange', 'mango', 'strawberry', 'apple']
print(len(my_shopping_list))            # 将输出元素个数,输出结果是 5

print("================================")


'''
  此时的 my_shopping_list = ['banana', 'orange', 'mango', 'strawberry', 'apple']
  将输出元素个数,输出结果是 5
'''
print(my_shopping_list[0])
print(my_shopping_list[1])
print(my_shopping_list[2])
print(my_shopping_list[3])
print(my_shopping_list[4])
# 列表的元素可以通过  列表名[编号] 索引,注意列表是从零开始编号的
my_shopping_list[1] = "banana"          # 可以通过索引来替换对应的元素
my_shopping_list[0] = "orange"          # 将banana和orange这两个元素互唤
print(my_shopping_list)
# 此时的 my_shopping_list = ['orange', 'banana', 'mango', 'strawberry', 'apple']
print("================================")

shopping_price_list  = ['7','19','23','14','10']
print(type(shopping_price_list[0]))        # 列表的元素一般为字符串类型


my_shopping_price_list = [int(s) for s in  shopping_price_list]
# 意思是把 shopping_price_list 里的每一个字符串 s 都转成整数,然后组成一个新的列表
# 将类型转换成 int 或 float 类型才能正常运算,否则就会用 ASCII值 来比较

print(max(my_shopping_price_list))         # 打印列表的最大值,输出的是23
print(min(my_shopping_price_list))         # 打印列表的最小值,输出的是7
print(sorted(my_shopping_price_list))      # 打印排好序的列表[7, 10, 14, 19, 23]
# 要运算一般直接用 int 或 float 类型

print("================================new============================")
# 可以直接在列表里输入数字而不用引号
price_list = [123,108,66,140,12,99]
print(max(price_list))                     # 打印列表的最大值,输出的是140
print(min(price_list))                     # 打印列表的最小值,输出的是12
print(sorted(price_list))                  # 打印排好序的列表[12, 66, 99, 108, 123, 140]

print("==================================================================")
list_01 = [66.6,'hello',True,None]
# 列表里可以放不同类型的数据，需要注意用对类型
print(list_01)                              # [66.6, 'hello', True, None]