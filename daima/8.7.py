class my_name1():
    name1="ccg"
class my_name2(my_name1): 	# my_name2继承了my_name1
    name2="独闯天下"
class my_name3(my_name2):   # my_name3继承了my_name2
    name3="陈成钢"
a=my_name3()   #a具有三个属性，自己和继承来的两个属性
print(a.name3,a.name2,a.name1)
