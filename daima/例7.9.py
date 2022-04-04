def test(x, *numbers, **phone):
    print('x', x)
    #遍历元组中的所有项目
    for every in numbers:
        print('every', every)
    #遍历字典中的所有项目
    for first_part, second_part in phone.items():
        print(first_part,second_part)

print(test(100,10,20,30,张三=139,李四=135,王五=130))
