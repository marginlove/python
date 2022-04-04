class Custom:
    def __init__(self, name):
        self.name = name
        self.__num=12
        # 存款为私有变量，不让外界直接访问
        self.__deposit = 18000
    # 存款为私有变量，通过私有方法提供访问接口
    def __secret(self):
        print("存款是%d" % self.__deposit)
a = Custom('风清扬')
print(a.name)
print('ID:',a._Custom__num)
a._Custom__secret()# 私有属性，外部不能直接访问
