class my_name1():
    name1="ccg"
    def my_print(self):
        print(self.name1)
        print("my_name1")
class my_name2(my_name1):  # my_name2继承了my_name1
    name2 = "独闯天下"
    def my_print2(self):  #派生出新方法my_print2
        super().my_print()  # 调用父类my_name1的方法
        print("my_name2")
class my_name3(my_name2): # my_name3继承了my_name2
    name3="陈成钢"
    def my_print3(self):
        super().my_print2() # 调用父类my_name2的方法
        print("my_name3")
a=my_name3()
print(a.name3,a.name2,a.name1)
a.my_print3()
