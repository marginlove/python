print('管理员登陆界面'.center(50,'*'))
# 初始会员信息
users = ['make','tom','johnson']
passwds = ['123','abc','123abc']

# 接收用户输入的用户名和密码
inuser = input("用户名:")
inpasswd = input("密码:")

if inuser == 'admin':
    if inpasswd == 'admin':
        print("管理员%s登陆成功" % (inuser))
        while True:
            print("""
            **********操作目录**********
            1.添加会员信息
            2.删除会员信息
            3.查看会员信息
            4.退出
            """)
            option = input('请输入你想执行的操作:')
            if option == '1':
                print('添加会员信息'.center(50,'*'))
                adduser = input('用户名:')
                addpasswd = input('密码:')
                if adduser in users:
                    print('添加失败，该会员信息已经存在!')
                else:
                    users.append(adduser)
                    passwds.append(addpasswd)
                    print('添加信息成功!')
            elif option == '2':
                print('删除会员信息'.center(50,'*'))
                deluser = input('用户名:')
                if deluser not in users:
                    print('删除失败，该会员信息不存在!')
                else:
                    # 找出想删除的用户对应的索引值
                    delindex = users.index(deluser)
                    # 删除用户,remove表示删除列表中的元素
                    users.remove(deluser)
                    # 按照索引值删除密码,pop也表示删除列表中的元素,区别在于,它可以按索引值来删除
                    passwds.pop(delindex)
                    print('删除信息成功!')
            elif option == '3':
                print('查看会员信息'.center(50,'*'))
                # 记录users列表的长度（即列表中元素的个数）
                count = len(users)
                for i in range(0,count):
                    print('用户名: %s   密码: %s' %(users[i],passwds[i]))
            elif option == '4':
                exit()
            else:
                print('请输入正确的操作指令')
    else:
        print("%s登陆失败: 密码错误!" % (inuser))
else:
    print("用户%s不存在" % (inuser))