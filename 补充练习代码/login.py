#模拟登录

import random
import string
p="".join([random.choice(string.ascii_letters) for i in range(5)])
q="".join([random.choice(string.ascii_letters+string.hexdigits) for i in range(6)])
print(p)
print(q)
#p,q就是初始化的用户和密码,p是用户名,q是密码，可以打印，可以不打印
 
#flag，count是计数器
flag=0
count=0
while True:
    username=input("输入你的名字")
    if username == p:
        while True:
            passwd=input("输入你的密码")
            if passwd == q:
                print("成功进入")
                break
            else:
                flag+=1
                print('密码错误')
                if flag == 3:
                    print('密码错误三次')
        break
    else:
        count+=1
        print('用户名错误')
    if count == 3:
        print('用户名错误过多')
        break
