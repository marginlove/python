s='宁波' 	#字符串s
#下面一句字符串编码成字节 b'\xe5\xae\x81\xe6\xb3\xa2' ，encode（）编码函数
print(s.encode())
print(type(s.encode())) #字符串编码后字节码类型<class 'bytes'>
# 下面一句解码结果为’宁波‘ decode（）解码函数
print(b'\xe5\xae\x81\xe6\xb3\xa2'.decode(encoding='UTF-8') )
s='hello'
print(s)
s='\'hello\\\'\n'	#字符串s涉及多个转义字符
print(s)
