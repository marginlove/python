# 需要安装graphics图形模块
from graphics import *
# 设置画布窗口名和尺寸
win = GraphWin('画个图', 900, 900)
pt = Point(100, 100) # 画点
pt.draw(win)
for i in range(50,2,-1): # 画圆
    cir = Circle(Point(400, 400),7*i)
    cir.setOutline('red')  # 外围轮廓颜色
    if(i == 50):
        cir.setFill('black')  # 填充颜色
    elif(i==3):
        cir.setFill('blue')
    elif(i%4==0):
        cir.setFill(color_rgb(125-i, 2*i, 5*i))
    else:
        cir.setFill(color_rgb(125,100,200))
    cir.draw(win)
# 关闭画布窗口
win.getMouse();win.close()
