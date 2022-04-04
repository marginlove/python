from math import *
print("程序求一元二次方程ax**2+bx+c=0的根\n")
a=float(input("输入a:"))
b=float(input("输入b:"))
c=float(input("输入c:"))
disc=b*b-4*a*c
p=-b/(2*a)
q=sqrt(disc)/2/a
x1=p+q; x2=p-q
print("\nx1=%.2f\nx2=%.2f\n" %(x1,x2))
