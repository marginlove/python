d_weight = {'ccg':64,'zcw':68, 'zy':58}
for i in range(1,4): #利用循环运行3次查询
    name=input('查询的姓名：')
    print('姓名：',name,'体重:',d_weight.get(name))
