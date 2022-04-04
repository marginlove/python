from tkinter import *
root = Tk()
root.title("滚动字幕")
root.geometry('1024x768')
show_str = StringVar(root)
show_str.set("好好学习，天天向上!")
source_str = "好好学习，天天向上!"
stopflag = True
pos = 0
mytkg = Canvas(root, bg='red',width =800, height = 600)
sel =mytkg.create_rectangle(10, 5, 768, 10, outline='blue', fill='yellow')
mytkg.pack()
#画一条黄色的横线
mytkg.create_line(0, 150, 800, 150, fill = "yellow")
#画一条黄色的x斜线（虚线）
mytkg.create_line(500, 0, 100, 100, fill = "yellow", dash = (4, 4))
#画一条黄色的斜线（虚线）
mytkg.create_line(0,0,500, 100,  fill = "yellow", dash = (4, 4))
#中间画一个蓝色的矩形
mytkg.create_rectangle(100,500,600,600, fill = "Wheat")
mytkg.create_text(350, 540, text = "程序设计：独闯天下！",font=('隶书',30))
mytkg.create_text(300, 300, text = "努力学习，报效祖国！",font=('隶书',30))
show_lb = Label(root, textvariable=show_str)
show_lb.place(x=180, y=50, width=500, height=80)
show_lb.config(font=('隶书',30),background='yellow')
root.mainloop()
