try:
 fh = open("test", "w")
 fh.write("测试异常!!")
finally:
 print("Error: 没有找到文件或读取文件失败")
