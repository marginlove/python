try:
 fh = open("test.txt", "w")
 fh.write("测试异常!")
except IOError:
 print("Error: 没有找到文件或读取文件失败")
else:
 print("内容写入文件成功")
 fh.close()
