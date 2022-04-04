#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk  # 使用tkinter前需要先导入
window = tk.Tk()#实例化object，建立窗口window
window.title('我的第一个窗体') #设置窗口标题
window.geometry('500x300')  #设定窗口的大小(长 * 宽)
window.maxsize(3090,768) #设定窗口最大化的最大值
window.minsize(500,300) #设定窗口最大化的最小值
#window.resizable(False,False) #高度和宽度不能变，去掉注释起作用
#window.attributes("-toolwindow",1) #窗口只有关闭按钮，去掉注释起作用
window.attributes("-alpha",0.95)#窗口的透明度,1为不透明，0为完全透明
window.mainloop()
