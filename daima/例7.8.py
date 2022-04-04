def add(a, b, *c):
 sum = a+b 
    #遍历元组中所有的项目
 for n in c:
   sum+=n
 return sum

print(add(1,2,3,4,5))
