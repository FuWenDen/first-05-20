StudentArray=[]###定义一个空的数组容器 来进行存放数据

while True:
    print("=============================")
    print("|  【欢迎您进入学生管理系统】   |")
    print("|   【1】.查询所有学生信息     |")
    print("|   【2】.增加新的学生信息     |")
    print("|   【3】.删除该学生的信息     |")
    print("|   【4】.修改存在学生信息     |")
    print("|   【5】.查询信息是否存在     |")
    print("=============================")

    ##需要将用户输入的数据转化int类型
    number=int(input("请输入以上序号信息选择功能:"))
    StudentArrayLen= len(StudentArray)
    match number:
        case 1: ##查找所有学生信息
            if StudentArrayLen==0:
                print("没有任何学生信息!")
            else:
                for index in range(0,StudentArrayLen):
                     print(f"index：{index},数据：{StudentArray[index]}")
        case 2: ##新增学生信息
           newStuName= input("请输入新增学生信息名称:")
           StudentArray.append(newStuName)
           print(f"学生{newStuName}新增成功!")
        case 3:  ##删除学生信息
            userStuName = input("请输入查找学生的名称:")
            flag = False  ## 标记数组中是否查找到该元素 能够查找到 true 否则false
            for index in range(0, StudentArrayLen):
                stuDentName = StudentArray[index]  ##数组容器元素
                ##数组容器元素用户输入的userStuName相同的
                if stuDentName == userStuName:
                    flag = True
                    break
                ## for循环外面
            if flag:
                print(f"该学生{userStuName}存在!")
                ##删除学生代码
                StudentArray.remove(userStuName)
                print(f"该学生{userStuName}删除成功!")
            else:
                print(f"该学生{userStuName}不存在，删除失败!")
        case 4: #修改学生信息
            userStuName = input("请输入查找学生的名称:")
            flag = False  ## 标记数组中是否查找到该元素 能够查找到 true 否则false
            for index in range(0, StudentArrayLen):
                stuDentName = StudentArray[index]  ##数组容器元素
                ##数组容器元素用户输入的userStuName相同的
                if stuDentName == userStuName:
                    flag = True
                    print(f"该学生{userStuName}存在!")
                    newStudentName=input("请输入修改的学生名称:")
                    StudentArray[index]=newStudentName
                    print(f"该学生原来名称：{userStuName}改为：newStudentName：{newStudentName}成功!")
                    break
                if not flag:
                    print("该学生不存在，修改失败!")
        case 5:  ##根据学生的名称 查找学生是否存在
           userStuName = input("请输入查找学生的名称:")
           flag =False## 标记数组中是否查找到该元素 能够查找到 true 否则false
           for index in range(0, StudentArrayLen):
            stuDentName= StudentArray[index]##数组容器元素
            ##数组容器元素用户输入的userStuName相同的
            if stuDentName==userStuName:
                flag=True
                break
            ## for循环外面
           if flag:
                print(f"该学生{userStuName}存在!")
           else:
                print(f"该学生{userStuName}不存在!")
    print("----------------------------------------")

