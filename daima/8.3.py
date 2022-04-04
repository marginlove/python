class student():
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def laugh(self):
        print(self.name,"哈哈哈哈！！")
    def walk(self):
        print(self.name,"蹦蹦跳跳上学去！")
    def get_name(self):
        return self.name
    def get_num(self):
        return self.num
a=student("李四",18)       #带参数的类对象实例创建
print(a.name,a.num)     #对象的属性访问
print("姓名：",a.get_name(),"学号",a.get_num())   #对象的方法访问
a.laugh()   #对象方法访问
a.walk()   #对象方法访问
