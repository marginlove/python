class fun_drop():
    def __init__(self,v,g):
        self.v=v
        self.g=g
    sum=0
    def my_fun(self,t):
        return self.v*t+0.5*self.g*t**2
a=fun_drop(3,9.8)    #对象实例创建
print(a.my_fun(5))    #实例方法的访问
