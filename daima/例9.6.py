import chardet
f1 = open("test.txt",'r')
data =f1.read()   
print(data) 
f1.close() 

str = chardet.detect(data)   #检测文件内容
print(str)
