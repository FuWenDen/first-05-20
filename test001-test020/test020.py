##需求：通过input函数来接收管理员用户输入的账户名称和密码，来判断是否登录成功，
##     如果都是admin则提示登陆成功，否则提示账号名称或密码错误。
Account_Name = input("请输入账户名称： ")
Account_Password = input("请输入账户密码： ")
if Account_Name == 'admin':
    if Account_Password == 'admin':
        print("登陆成功！")
    else:
        print("登陆失败！密码错误。")
else:
    print("登陆失败！账户名称或密码错误。")
print("========================================")

'''
if Account_Name ==‘admin’ and Account_Password == ‘admin’:
    print("登陆成功！")
else：
    print("登陆失败！")
'''

print("==================end======================")
