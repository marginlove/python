import random
# 定义用来记录总的答题数目和回答正确的数目
count = 0
right = 0
# 因为题目要求：提供10道题目(因为题目要求：提供10道题目)
while count <= 10:
    # 创建列表，用来记录加减乘除四大运算符
    op = ['+', '-', '*', '/']
    # 随机生成op列表中的字符
    s = random.choice(op)
    # 随机生成0-100以内的数字
    a = random.randint(0,100)
    # 除数不能为0
    b = random.randint(1,100)
    print('%d %s %d = ' %(a,s,b))
    # 默认输入的为字符串类型
    question = input('请输入您的答案:')
    # 判断随机生成的运算符，并计算正确结果
    if s == '+':
        result = a + b
    elif s == '-':
        result = a - b
    elif s == '*':
        result = a * b
    else:
        result = a / b

    #  判断用户输入的结果是否正确,str表示强制转换为字符串类型
    if question == str(result):
        print('回答正确')
        right += 1
        count += 1
    else:
        print('回答错误')
        count+=1
    goon = input('还要继续吗:(Y/N)')
    if goon=='Y':
        continue
    else:
        break
# 计算正确率
if count == 0:
    percent = 0
else:
    percent = right / count
print('测试结束,共回答%d道题,回答正确个数为%d,正确率为%.2f%%' %(count,right,percent*100))