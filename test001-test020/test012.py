#字符串索引学习
#计算机程序编号是从零到一开始的！！
#正向索引是从0开始的，从左到右数来编号
from test004 import user_name
#user_name = "DengFuWen"
print(user_name[0])     #  ‘D’
print(user_name[1])     #  ‘e’
print(user_name[2])     #  ‘n’
print(user_name[3])     #  ‘g’
print(user_name[4])     #  ‘F’
print(user_name[5])     #  ‘u’
print(user_name[6])     #  ‘W’
print(user_name[7])     #  ‘e’
print(user_name[8])     #  ‘n’
print("===================================")
#负向索引是从-1开始的，从右到左数来编号
print(user_name[-1])    #  ‘n’
print(user_name[-2])    #  ‘e’
print(user_name[-3])    #  ‘W’
print(user_name[-4])    #  ‘u’
print(user_name[-5])    #  ‘F’
print(user_name[-6])    #  ‘g’
print(user_name[-7])    #  ‘n’
print(user_name[-8])    #  ‘e’
print(user_name[-9])    #  ‘D’
print("===================================")
#用索引可以截取字符串
print(user_name[-9:-7]) #  ‘De’，就是从-9到-7（不包含-7）
print(user_name[-7:-9]) #   该语句没有起作用，因为字符串是从左到右索引的，-1后面没有东西
print(user_name[-9:])   #   ‘DengFuWen’就是从-9到结束
print(user_name[:-7])   #   ‘De’就是从开头到-7（不包含-7）
print("===================================")
print("===================================")

text = "Hello, World!"
# 索引:   0  1  2  3  4 5 6 7 8 9 10 11 12
#        H  e  l  l  o , W o  r  l  d  !
# [起始索引:结束索引:步长]
# [start  :end   :step]（英文名）
print(text[::2])    # 'Hlo ol!'（每隔一个字符取一个）
print(text[1:6:2])  # 'el,'（从索引 1 到 5，步长为 2）
print(text[::-1])   # '!dlroW ,olleH'（反转字符串）
print("=========================================")
print("=========================================")
print("===========找规律，熟悉步长=================")
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9,0]
print(nums[::-1])   # [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(nums[::1])    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("===================================")

print(nums[::-2])   # [0, 8, 6, 4, 2]
print(nums[::2] )   # [1, 3, 5, 7, 9]
print("===================================")

print(nums[::-3] )  # [0, 7, 4, 1]
print(nums[::3] )   # [1, 4, 7, 0]
print("===================================")

print(nums[::-4])   # [0, 6, 2]
print(nums[::4] )   # [1, 5, 9]