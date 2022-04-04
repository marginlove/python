class Student():
    @staticmethod
    def hello(name):
        print("欢迎访问",name,"考试系统")
    school="***学校"
    def __init__(self,name,score): #构造方法第一个参数必须为 self
          self.name = name #实例属性
          self.score = score
    def print_score(self): #实例方法
         print(self.school,self.name,'的分数是：',self.score)
Student.hello("浙江*****学院")  #无需实例化即可访问
Student.print_score()    #没有实例化无法访问，需改成例5先创建才能访问
