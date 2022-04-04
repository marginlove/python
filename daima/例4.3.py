from math import *
x=float(input("input number x="))
if x<0:
    y=x*x
elif x==0:
    y=x
else:
    y=sqrt(2*x+6)
print("y=%.2f"%y)