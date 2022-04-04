#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter as tk
import time
def gMove(event):
    if event.keysym == 'Left':
        canvas.move(1,-5,0)
    if event.keysym == 'Right':
        canvas.move(1,5,0)
    if event.keysym == 'Up':
        canvas.move(1,0,-5)
    if event.keysym == 'Down':
        canvas.move(1,0,5)
window = tk.Tk()

window.title('图片示例')

window.geometry('800x600')  # 这里的乘是小x
l = tk.Label(window, width=20, text='图片示例', font=('隶书', 20))
l.pack()
# 在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, width=800, height=600,bd=1)

# 说明图片位置，并导入图片到画布上
image_file = tk.PhotoImage(file='a.png')  # 图片位置（本例使用相对路径，文件与.py文件同一文件夹下，也可使用绝对路径）
image = canvas.create_image(380, 90, anchor='n', image=image_file)
# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 10, 10, 750, 750
canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180,outline = 'red',stipple = 'gray12')
canvas.create_rectangle(0, 0, 750, 50,fill='yellow')
l2 = canvas.create_text((200,30), text="湖光山色", font="MSGothic 30 bold", fill="#652828")
canvas.place(relx= 0.01, rely=0.1)
canvas.bind_all('<KeyPress-Left>',gMove) #画布绑定键盘操作，按键图片移动
canvas.bind_all('<KeyPress-Right>',gMove) #画布绑定键盘操作，按键图片移动
canvas.bind_all('<KeyPress-Up>',gMove) #画布绑定键盘操作，按键图片移动
canvas.bind_all('<KeyPress-Down>',gMove) #画布绑定键盘操作，按键图片移动
for i in range(0,60): #对象移动示例
    canvas.move(4,5,0)#canvas对象中的编号“4”图形调用移动函数，x轴5个像素点，y轴不变
    window.update()
    time.sleep(0.05)
window.mainloop()
