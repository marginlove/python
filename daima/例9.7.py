import os
f1=open("test.dat",'w+b')  #打开或创建test.dat
f1.seek(0)     #定位到test.dat文件头
f1.write(b"python")  #写入字符串’python’
f1.write(b"program")  #写入字符串’program’
f1.seek(-7,os_SEEK_END)  #定位到文件尾的倒数第七个字节
print(f1.read(7))  #读取七个字节
