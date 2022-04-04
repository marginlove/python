#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
window = tk.Tk()
window.title('其它控件')
window.geometry('600x500')
var1 = tk.StringVar()  # 创建变量，用var1用来接收鼠标点击具体选项的内容
l1 = tk.Label(window, text="单选框、复选框和列表框示例", font=('隶书', 20), width=50)
l1.pack()
l = tk.Label(window, bg='yellow', fg='blue', font=('Arial', 12), width=50, textvariable=var1)
l.pack()
def print_selection():
    value = lb.get(lb.curselection())  # 获取当前选中的文本
    var1.set(value)  #为label设置值
def print_selection2():
    value = '单选选项：'+str(var.get())  # 获取当前选中的单选框文本
    var1.set(value)  # 为label设置值
def print_selection3():
  if check1.get()==1:
    value = '清蒸鱼'  # 获取当前选中的复选框值
  else:
      value =' '    # 取消
  var1.set(value)  # 为label设置值
def print_selection4():
  if check2.get()==1: # 获取当前选中的复选框值
    value = '清蒸螃蟹'   # 设置值
  else:
      value =' '
  var1.set(value)  # 为label设置值
b1 = tk.Button(window, text='测试选中状态', width=15, height=2, command=print_selection)
b1.place(relx= 0.4, rely=0.6)
# list增加内容三种方法
var2 = tk.StringVar()
var2.set(('米饭','面条', 32, '爆炒白菜'))  #第一种方法，为变量var2设置值
# 创建Listbox
lb = tk.Listbox(window, listvariable=var2)  # 将var2的值赋给Listbox
# 第二种方法，创建一个list并将值循环添加到Listbox控件中
list_items = ['糖醋排骨','红烧肉', '番茄蛋汤', '清炒白菜']
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置开始加入值
lb.insert(1, '狮子头')  # 第三种方法，在第一个位置加入'first'字符
lb.insert(2, '榨菜')  # 在第二个位置加入'second'字符
lb.delete(2)  # 删除第二个位置的字符
lb.pack()
# 单选框
var = tk.IntVar()
r1 = tk.Radiobutton(window, text='红烧肉', variable=var, value=1, command=print_selection2)
r1.place(relx= 0.1, rely=0.15)
r2 = tk.Radiobutton(window, text='清蒸鱼', variable=var, value=2, command=print_selection2)
r2.place(relx= 0.1, rely=0.25)
r3 = tk.Radiobutton(window, text='清蒸螃蟹', variable=var, value=3, command=print_selection2)
r3.place(relx= 0.1, rely=0.35)
#复选框
check1 = tk.IntVar()
check2 = tk.IntVar()
c1 = tk.Checkbutton(window, text = "清蒸鱼", variable = check1,onvalue = 1, offvalue = 0, height=3,width = 20, command=print_selection3)
c2 = tk.Checkbutton(window, text = "清蒸螃蟹", variable = check2, onvalue = 1, offvalue = 0, height=3, width = 20, command=print_selection4)
c1.place(relx= 0.7, rely=0.15)
c2.place(relx= 0.7, rely=0.25)
window.mainloop()
