a = int(input('请输入数字1：'))
b = int(input('请输入数字2：'))
c = int(input('请输入数字3：'))
if a > b:
    if a>c:
        max = a
    else:
        max =c
else:
    if b>c:
        max = b
    else:
        max =c
print('输出最大值是：',max)
