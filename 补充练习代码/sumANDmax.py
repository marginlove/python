# 输入一个正整数，获得每个位的数的和，以及最大的数

# 用字符串的方式
def method_by_str(num):
    sumNum = 0
    maxNum = 0
    b = list(num)
    for i in range(0, len(b)):
        sumNum += int(b[i])
        # print(b[i])
    maxNum = b[-1]
    print("最大数", maxNum)
    print(sumNum)

# 用数值的方式
def method_by_num(num):
    sumNum = 0
    maxNum = 0
    while num != 0:
        y = num % 10
        sumNum += y
        if y > maxNum:
            maxNum = y
        num = int(num / 10)
    print("最大数", maxNum)
    print(sumNum)


a = input("请输入一个正整数:")

# method_by_str(a)

method_by_num(int(a))