a=34
b=56
print(a,"+",b,end="")
c= input("输入结果: ")#如改成c=eval(input("输入结果: "))程序运行结果不同
if(a+b==c):
    print('正确')
else:
    print('错误')
