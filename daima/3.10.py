from math import *
a=float(input("请输入三角形的第一条边长"))
b=float(input("请输入三角形的第二条边长"))
c=float(input("请输入三角形的第三条边长"))
s=1/2*(a+b+c)
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("a=%.2f,b=%.2f,c=%.2f 面积：%.5f" %(a,b,c,area))
