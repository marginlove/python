#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
def say_hi():
    print("演示下，以后设计")
root = tk.Tk()
root.geometry('800x600')
frame1 = tk.Frame(root,bg='blue',bd=2,height = 200, width=600)
frame2 = tk.Frame(root,bd=2,width=550,bg='#ff3399',height = 200)
root.title("tkinter frame")
label = tk.Label(frame2, text="发送信息", justify=tk.LEFT)
L2 = tk.Label(frame1,text='接\n收\n区',width=2, justify=tk.LEFT, font=("宋体", 12, "bold"))
L2 .pack(padx=2,pady=40,side=tk.LEFT,anchor=tk.N) # 添加接收区文字标签
v = '收到新信息：\n'# 添加接收区的文本框
txt1 = tk.Text(frame1, height = 10,yscrollcommand=1)
txt1.pack()
txt2 = tk.Text(frame2, height = 10,yscrollcommand=1)
txt2.pack()
label.pack(side=tk.LEFT)
hi_there = tk.Button(frame2, text="发送", command=say_hi)
hi_there.pack()
frame1.pack_propagate(0)
frame1.pack(padx=1, pady=1)
frame2.pack_propagate(0)
frame2.pack(padx=10, pady=10)
root.mainloop()
