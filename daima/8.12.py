class People():
    def __init__(self):
        self.name = People
    def say(self):
        print("人类",self.name)
class Animal():
    def __init__(self):
        self.name = Animal
    def say(self):
        print("动物",self.name)
#People中的 name 属性和 say() 会遮蔽 Animal 类中的
class Person(People,Animal ):    # People覆盖Animal的同名方法
    pass
a = Person()
a.name = "张三"
a.say()
