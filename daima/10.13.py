#coding:utf-8
import tkinter as tk
from tkinter.constants import *  # 导入TK的符号常量，简化属性等方面的代码设计
import time
def sendStr():
    vv =tk.StringVar()
    vv.set(time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
    vv=str(vv.get())+'信息：'+txt2.get('1.0', tk.END)
    txt1.insert(tk.END,vv)

def gettime():
    v.set(time.strftime("%Y-%m-%d %H:%M:%S "))  # 获取当前时间

top = tk.Tk()
top.wm_geometry('800x480+1000+100') # 设置窗口的尺寸大小
top.wm_resizable(False,False) # 不允许 改变 窗口的宽和高
top.title('简单演示') # 设置窗口标题

v = tk.StringVar()
v.set('登录时间：'+time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
lable4=tk.Label(top,textvariable=v,font=('隶书', 10))
lable4.pack()

# 设置框架容器
frame1 = tk.Frame(top,height=80 ,relief=RIDGE, bg='#ff3399',bd=5,borderwidth=4)
# 设置框架容器填充和布局
frame1.pack(fill=NONE,ipady=2,expand=False)

# 添加接收区文字标签
L2 = tk.Label(frame1,text='接\n收\n区',width=2, justify=LEFT, font=("宋体", 12, "bold"),)
L2.pack(padx=2,pady=40,side=LEFT,anchor=N)
# 添加接收区的文本框
v = '收到新信息：\n'
txt1 = tk.Text(frame1, height = 10,yscrollcommand=1)
#增加滚动条
yscrollbar = tk.Scrollbar(frame1)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 滚动条与text联动
yscrollbar.config(command=txt1.yview)
# text与滚动条联动
txt1.config(yscrollcommand=yscrollbar.set)

txt1.pack(padx=2,pady=10,side=RIGHT,anchor=N)
txt1.insert(tk.END,v)
frame2 = tk.Frame(top, relief=RIDGE,bg='#3366ff')
frame2.pack(fill=X, padx=2,pady=10,side=TOP)
# 设置容器
frame3 = tk.Frame(top,height=120 ,relief=RIDGE, bg='#ff3399',bd=5,borderwidth=4)
# 设置填充和布局
frame3.pack(fill=X,ipady=2,expand=False)
# 设置字符串变量
ServerReceiveVar = tk.StringVar(top,'')
L3 = tk.Label(frame3, text='输入信息:',font=('黑体',12))
L3.pack(fill=NONE, expand=NO, side=TOP, anchor=W, padx=2,pady=10)
txt2 = tk.Text(frame3, height = 2, width = 30)
txt2.pack(padx=2, pady=2, ipady=4, side=LEFT, anchor=N)

button1 = tk.Button(frame3,text='发送', command=sendStr)
button1.pack(side=TOP, anchor=W, padx=2, pady=4)
button2 = tk.Button(frame3,text="退出",command=top.destroy)
button2.place(relx= 0.35, rely=0.5)

top.mainloop()
