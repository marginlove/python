#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter
import tkinter.messagebox
top = tkinter.Tk()
top.title('按钮示例')
top.geometry('500x300')  # 这里的乘是小x
def button_click():
    tkinter.messagebox.showinfo("示例", "按钮示例")
b = tkinter.Button(top, text="点我", width=10 ,command= button_click)
b.place(relx= 0.35, rely=0.5)
top.mainloop()
