import tkinter as tk
from tkinter.constants import *
import time
root = tk.Tk()
root.geometry('500x300')
root.title('一级菜单示例')
def gettime():
    v.set(time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
    root.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间
def callback():
    print("被调用了")
menubar = tk.Menu(root) # 创建一个顶级菜单
#创建实例，各属性格式参见表格5
filemenu = tk.Menu(menubar, tearoff=False,background='yellow',activebackground='blue',activeborderwidth=10,font='隶书',fg='black',relief='raised')
filemenu2 = tk.Menu(menubar, tearoff=False,background='yellow',activebackground='blue',activeborderwidth=10,font='隶书',fg='black',relief='raised')
filemenu.add_command(label="时间", command=gettime) # 创建菜单项
filemenu.add_command(label="测试不可用", command=gettime,state=tk.DISABLED)
filemenu.add_separator()  # 创建一个分割线
filemenu.add_command(label="打开", command=callback) # 创建菜单项
filemenu.add_command(label="保存", command=callback) # 创建菜单项
filemenu.add_separator()  # 创建一个分割线
filemenu2.add_command(label="测试菜单项", command=callback)
filemenu.add_cascade(label="二级菜单", menu=filemenu2)
filemenu.add_command(label="退出", command=root.quit) # 创建菜单项

menubar.add_cascade(label="文件", menu=filemenu) # 添加到父菜单
v = tk.StringVar()
v.set('单击菜单获取时间')  # 获取当前时间
L2 = tk.Label(root,textvariable=v,justify=LEFT, font=("宋体", 12, "bold"),)
menubar.pack_propagate(0)
L2.pack(padx=2,pady=40,side=RIGHT,anchor=N)
root.config(menu=menubar)# 显示菜单
root.mainloop()
