a=list()
mnum={0:'零',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}
for i in range(10,20):
    mnum[i]=str(i)
for i in range(1,20):
    if i<10 :
        b={'user':'张'+mnum[i],'num':i}
    else:
        b={'user':'张'+mnum[i//10]+mnum[i%10],'num':i}
    a.append(b)
print(a)
print('第三个学生数据---姓名:',a[2]['user'],'学号：',a[2]['num'])
