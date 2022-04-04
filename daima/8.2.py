class student():
    name=input("输入姓名：")
    num=12
    height=160
    weight=57
    def laugh(self):
        print(self.name,"哈哈哈哈！！")
    def walk(self):
        print(self.name,"蹦蹦跳跳上学去！")
a=student()   #对象实例创建
a.laugh()   #对象方法访问
a.walk()   #对象方法访问
