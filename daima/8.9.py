class my_name1():
    name="ccg"
    def my_print(self):
         print("my_name1",self.name)
class my_name2(my_name1):
    name = "独闯天下"
    def my_print2(self):
        super().my_print()
        print("my_name2",self.name)
class my_name3(my_name2):
    name="小李飞刀"
    def my_print3(self):
        super().my_print2()
        print("my_name3",self.name)
a=my_name3()
print("直接访问my_name3数据：",a.name)
print("测试my_name3数据：")
a.my_print3()
