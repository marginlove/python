list = []
for i in range(10):
    x=int(input('请输入：'))
    list.append(x)
for i in range(9):
    for j in range(9):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]
print(list)