student={'num':18,'name':'ccg','addr':'浙江万里学院','tele':13605742148}
print('原来的信息：',student)
print('姓名：',student['name'])
print('地址：',student['addr'])
print('输入你要修改的姓名:')
oldname=input("输入旧姓名：")
if(student['name']==oldname):
    name=input("输入新姓名：")
    student['name']=name
    print('修改后信息：', student)
    print('学生新姓名：', student['name'])
else:
    print('该姓名不存在!无法修改')
