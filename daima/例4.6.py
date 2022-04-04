salary=float(input("请输入你的薪水："))
if salary<=850:
    tax=0
elif salary<=1350:
    tax=0.05*(salary-850)
elif salary<=2850:
    tax=0.10*(salary-850)
elif salary<=5850:
    tax=0.15*(salary-850)
else :
    tax=0.2*(salary-850)
print("你应交所得税为：%.2f"%tax)