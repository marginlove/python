#!/usr/lib/env python
#coding:utf-8
import hashlib

def get_md5( data):
    obj = hashlib.md5('good65746532458wl'.encode('utf-8'))#密码初始化，避免密码被反推
    obj.update(data.encode('utf-8'))#更新对象的状态
    result = obj.hexdigest()#以十六进制数字字符串的形式。
    return result #返回加密的信息

def users_create():
    print(" ********************用户的创建**********************")
    print('注册'.center(50,'*'))
    print('*开头为必填项')
    name = input('*输入姓名:')
    custom = input('*输入用户名:')
    if not custom in users:
      passwd = input('*输入密码:')
      gender =eval(input("*0-'女',1-'男':"))
      age = eval(input('输入年龄:'))
      email = input("输入邮箱:")
      if not email:
        email = None
      users[custom] = {'name':name,'passwd':get_md5(passwd),'age':age,'gender':gender,'email':email}
      print("用户创建成功")
    else:
      print("用户已经存在")

def users_login():
    print("登录".center(100,'*'))
    error_num = 0
    while error_num < 3:
        name = input("输入用户名：")
        if not name in users:
            print ("用户不存在")
            error_num+=1
            break
        else:
            mpasswd = input('输入密码：')
            print(mpasswd)
            if get_md5(mpasswd) == users[name]['passwd']:
               print ('登录成功')
               break
            else:
               print ('密码错误，请重新输入：')
               error_num+=1
    else:
           print('输入错误次数超出')

def user_delete():
    print("删除".center(50,'*'))
    name = input('输入要删除的用户名:')
    if name in users:
             users.pop(name)
             print('%s 已删除' %name)
    else:
             print ('未注册的用户')

def user_info():
    for i,j in users.items():
             print('%s %s \n' %(i,j))

info = '''
         *********************用户登录管理模拟系统**********************
         1.注册新用户
         2.用户登录
         3.用户删除
         4.用户信息查询
         5.退出系统
         ***********************************************************
        '''
users = {'root':{'name':'root','passwd': get_md5('root'),'gender':1,'email':'','age':22}}
while 1:
     print(info)
     choice =eval(input("输入选择"))
     if choice == 1:
         users_create()
     elif choice == 2:
         users_login()
     elif choice == 3:
         user_delete()
     elif choice == 4:
         user_info()
     elif choice == 5:
         exit()
     else:
         print("选项不存在，重新输入：")
