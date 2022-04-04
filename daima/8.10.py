class my_name1():
    name="ccg"
    def my_print(self):
        self.defense=6.3
        print(self.defense)
class my_name2(my_name1):
    name = "独闯天下"
    def my_print(self):
        self.defense = 10.3
        print(self.defense)
class my_name3(my_name2):
    name="小李飞刀"
    def my_print(self):
        self.defense = 2.3
        print(self.defense)
a=my_name3()
print(a.name)
a.my_print()
