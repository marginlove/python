class Student:
    school="***学校"
    def __init__(self,name,score): #构造方法第一个参数必须为 self
          self.name = name #实例属性
          self.score = score
    def print_score(self): #实例方法
         print(self.school,self.name,'的分数是：',self.score)

stu_a=Student("李四",98)  #对象实例创建
stu_a.print_score()    #实例方法的访问
stu_a.school="浙江*****学院 "   #实例属性的修改
stu_a.print_score()
