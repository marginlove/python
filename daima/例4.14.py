from math import *
for n in range(100,200):
    flag=0
    m=int(sqrt(n))
    for i in range(2,m+1):
        if n%i==0:
            flag=1
            break
    if flag==0:
        print('%5d'%n,end='')
