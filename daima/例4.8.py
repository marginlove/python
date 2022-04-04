s=0
i=1
while i<=10:
    score=float(input('请输入第%d个成绩：'%i))
    s=s+score
    i=i+1
print('平均成绩是：%.2f'%(s/10))