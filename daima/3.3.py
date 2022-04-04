import time
import os
print("flush为真的：Loading效果---")
print("Loading",end="")
for i in range(20):
    print(".",end = '',flush = True)#强制刷新缓冲区，写出结果
    time.sleep(0.5)
