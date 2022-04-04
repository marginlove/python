from tkinter import *
root = Tk()  # 创建窗口对象
root.title("GUI测试")# 窗口标题
root.geometry('1024x768')# 窗口大小
label=Label(root,text='我的第一个GUI界面') #生成标签
label.config(font=('隶书',50),background='yellow')#标签设置
label.place(relx = 0.2, rely = 0.5, anchor = "nw")#标签位置relx, rely为绝对位置
label.pack()
root.mainloop()  # 进入消息循环
