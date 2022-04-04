import tkinter as tk
import time
root = tk.Tk()
root.title('多行文本框示例')
lable1=tk.Label(root,text='多行文本框示例',font=('隶书', 20))
lable1.pack()
txt1 = tk.Text(root, height=5, width=100,relief='groove')
txt1.insert(tk.END, '欢迎使用\n')
txt1.insert(tk.INSERT, 'Python')
txt1.insert(tk.INSERT, '\n好好学习，天天向上！')
#增加滚动条
yscrollbar = tk.Scrollbar(root)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# 滚动条与text联动
yscrollbar.config(command=txt1.yview)
# text与滚动条联动
txt1.config(yscrollcommand=yscrollbar.set)
txt1.pack()
v = tk.StringVar()
v.set('登录时间：'+time.strftime("%Y-%m-%d %H:%M:%S"))  # 获取当前时间
lable4=tk.Label(root,textvariable=v,font=('隶书', 20))
lable4.pack()
root.mainloop()
