import cmath
import math
x=513*2.7634 #浮点数
print(x)#输出1417.6242
print(round(x)) #输出1418
print(round(x,2)) #输出1417.62
print(round(x,-2)) #输出1400.0
print(math.sqrt(x)) #输出37.65135057338581
x=cmath.sqrt(-x) #复数
print(x) #输出37.65135057338581j
print(x+6+7j) #输出(6+44.65135057338581j)
