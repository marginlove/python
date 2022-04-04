number=0
sum=0
while True:
    s=input("请输入职工工资人(按Q退出)：")
    if s=='Q':
        print("职工工资录入已完成！")
        break
    if float(s)<0:
        continue
    number=number+1
    sum=sum+float(s)
print("职工人数：%d"%number)
print("平均工资：%.2f"%(sum/number))

