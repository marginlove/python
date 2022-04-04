import os
cur_path=os . path. dirname (__file__)   #获取当前路径
os.system ("mkdir newdir")  #创建newdir目录
os . system ("copy my.py  newdir\your.py")  #复制文件
file=cur_path + "\newdir\your .py"
os . system ("notepad " + file)  #用记事本打开your.py
