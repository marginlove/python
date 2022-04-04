user1={'name':'root','passwd':'root','gender':1,'email':'','age':22}
user2={'name':'dctx','passwd':'123','gender':1,'email':'2@qq.com','age':34}
user3={'name':'tx','passwd':'222','gender':0,'email':'112@qq.com','age':24}
users = {'root':user1,'ccg':user2,'tx':user3}
for key in users.keys():
    print(key,":",users[key])
print('用户名：',key,'用户姓名：',users[key]['name'],'年龄：',users[key]['age'])
