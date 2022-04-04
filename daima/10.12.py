import tkinter as tk
from tkinter.constants import *
root = tk.Tk()
def callback():
    v.set("我被执行了")
def callback2():
    v.set("执行菜单命令，我变了")
# 创建一个弹出菜单
menu = tk.Menu(root, tearoff=False)
menu.add_command(label="试试看", command=callback2)
menu.add_command(label="撤销", command=callback)
menu.add_command(label="重做", command=callback)
v = tk.StringVar()
v.set('单击右键选取快捷菜单')
L2 = tk.Label(root,textvariable=v,justify=RIGHT, font=("宋体", 12, "bold"))
frame = tk.Frame(root, width=400, height=82)
frame.pack()
L2.pack(padx=2,pady=100,side=RIGHT,anchor=N)

def popup(event):
    menu.post(event.x_root,event.y_root)
# 绑定鼠标右键
frame.bind("<Button-3>", popup)

root.mainloop()
