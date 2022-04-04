import tkinter as tk
from tkinter import ttk

app = tk.Tk()
app.title("demo")
app.geometry('500x300')
label = ttk.Label(app, text="Hello 中国!")
count = 0

def clickOK():
    global count
    count = count + 1
    label.config(text="点了OK " + str(count) + " 次")

button = ttk.Button(app, text="OK", command=clickOK)
label.pack()
button.pack()
app.mainloop()