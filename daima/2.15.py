a=15
print(bin(a)) #输出为0b1111
a=15>>2
print(bin(a)) #输出为0b11
a=9
b=5
a ^= b
b ^= a
a ^= b
print(a,b)#输出为5 9
