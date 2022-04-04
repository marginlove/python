# 需要安装graphics图形模块
from graphics import *
# 设置画布窗口名和尺寸
win = GraphWin('画个图', 900, 900)
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
    for j in range(2,10,1):
        pt = Point(10*j, 10*i)  # 画点
        pt.draw(win)
    cir.draw(win)
# 关闭画布窗口
win.getMouse()
win.close()
