class Student():
    def __init__(self,name,score): #构造方法第一个参数必须为 self
          self.school="***学校"
          self.name = name #实例属性
          self.score = score
    def print_score(self): #实例方法
         print(self.school,self.name,'的分数是：',self.score)
def learn(self,ss):            #定义一个函数
    print(ss,"好好学习，天天向上！")
Student.learn=learn        #动态的给Student类增加一个方法learn
stu_a=Student("李四",98)
stu_a.school="浙江*****学院 "
stu_a.print_score()
stu_a.learn(stu_a.name)
