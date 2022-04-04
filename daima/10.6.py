#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
window = tk.Tk()
window.title('按钮示例')
window.geometry('500x300')
var = tk.StringVar()
l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('点我试试看')
    else:
        on_hit = False
        var.set('试试就试试')
b = tk.Button(window, text='点击我试试', font=('Arial', 12), width=20, height=1, command=hit_me)
b.pack()
window.mainloop()
