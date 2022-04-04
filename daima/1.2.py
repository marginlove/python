import random    #导入模块
def myadd(a,b):   #定义函数
    return a+b   #返回数值
random.seed()    #调用函数生成种子数
a=random.randint(0,1000)   #调用函数生成随机数
b=random.randint(0,1000)   #调用函数生成随机数
sum=myadd(a,b)   #调用函数求和
print(a,"+",b,"=")   #调用输出函数，输出算式
c=input("输入答案：")  #调用输入函数，输入数据
if(sum==c):           #if语句判断结果
    print("正确")
else:
    print("错误")
