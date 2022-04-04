def listchange(mylist):  # mylist是函数输入参数对应的列表对象
    mylist.append([1, 2, 3, 4])  # 修改列表里的值
    print("函数体内: ", mylist)
    return

mylist = [10, 20, 30]
listchange(mylist)
print("函数体外: ", mylist)
