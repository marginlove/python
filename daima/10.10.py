import tkinter as tk
from tkinter.constants import *
import time
root = tk.Tk()
root.geometry('500x300')
root.title('一级菜单示例')
def gettime():  #窗体事件代码
    v.set(time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
    root.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间
menubar = tk.Menu(root) # 创建一个顶级菜单
menubar.add_command(label="时间", command=gettime)#增加普通菜单项
menubar.add_command(label="退出", command=root.quit) #增加普通菜单项
#下面代码实现窗体显示一个标签
v = tk.StringVar()
v.set('单击菜单获取时间')  # 获取当前时间
L2 = tk.Label(root,textvariable=v,justify=LEFT, font=("宋体", 12, "bold"),)
L2.pack(padx=2,pady=40,side=LEFT,anchor=N)
root.config(menu=menubar) # 显示菜单
root.mainloop()
