# -*-coding:utf-8-*-
#
mytuple3 = (1,  2,  3,  4,  5,  6,  7)
#顺序       0   1   2   3   4   5   6
#倒序      -7  -6  -5  -4  -3  -2  -1
# print(mytuple3[::-1])               # 倒序
print("0:" + str(mytuple3))
print("1:" + str(mytuple3[0:]))
print("2:" + str(mytuple3[0:3]))
print("3:" + str(mytuple3[:3]))
print("4:" + str(mytuple3[0::2]))       #起始元素（包含），结束元素（不包含），步进
print("5:" + str(mytuple3[0:5:2]))
print("6:" + str(mytuple3[5:0:-1]))
print("7:" + str(mytuple3[-3:-1]))
print("8:" + str(mytuple3[-3::-1]))
print("9:" + str(mytuple3[-3:0:-1]))
print("10:" + str(mytuple3[-3:2:-1]))