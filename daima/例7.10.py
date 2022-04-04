def fun():
    print('fun')
def fun1():
    print('fun1')
    return 10
def fun2():
    print("fun2")
    return 5, 'fun2', ['dog', 'cat'], {"name": "John"}

a=fun()
b=fun1()
c=fun2()
print(a)
print(b)
print(c)
