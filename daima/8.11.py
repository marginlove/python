class my_add():
    def add(self,a,b):
        print(a,"+",b,"=",end='')
        return a+b
class my_mul():
    def mul(self,a,b):
        print(a,"*",b,"=",end='')
        t=a*b
        return a*b
class fun_y(my_add,my_mul):
    pass		# pass 是空语句，保持程序结构的完整性，一般用做占位语句
a=fun_y()
print(a.add(23,45))
print(a.mul(23,45))
