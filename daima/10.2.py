#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用tkinter前需要先导入
import time  # 使用time模块改变时间
def gettime():
    v.set(time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
    window.after(1000, gettime)  # 每隔1s调用函数 gettime 自身获取时间
window = tk.Tk()
window.title('我的第一个窗体')
window.geometry('1024x600')  # 这里的乘是小x
photo = tk.PhotoImage(file='a.png') #图片a.png需要拷贝到代码文件的文件夹
lable2= tk.Label(window,text='湖边',justify='center',font=('隶书', 30))
lable3= tk.Label(window,text='-----作者：独闯天下',justify='center',font=('隶书', 18),foreground='blue')
lable1 = tk.Label(window,text='清晨\n我在湖边漫步，湖面薄雾轻掩，枯枝倒映，\n如梦似幻！',underline=3,justify='left',wraplength=220,borderwidth=2
,image=photo,compound='right', font=('Arial', 20))
v = tk.StringVar()
v.set(time.strftime("%Y-%m-%d %H:%M:%S"))
lable4=tk.Label(window,textvariable=v,font=('隶书', 10))#可变标签，显示时间变化
lable2.pack()
lable3.pack()
lable1.pack()  # pack 是按添加顺序排列组件
lable4.pack()
gettime()
window.mainloop()
