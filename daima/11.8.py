import matplotlib.pyplot as plt
import numpy as np
font = {'family':'SimHei','weight':'bold', 'size':'12'}
plt.rc('font',**font)
plt.figure(3)
x = np.arange(5)   #柱的索引
x_d = ('可乐', '薯片', '牛奶', '矿泉水', '饼干')
y1_d = (20, 35, 30, 35, 27)
y2_d = (25, 32, 34, 20, 25)
y3_d = (9, 12, 5, 1, 6)
bar_w = 0.35   #定义每个独立柱的宽度
#参数：左偏移、高度、柱宽、颜色、图例
rects1 = plt.bar(x, y1_d, width=bar_w, color='b',label='浙江')
rects2 = plt.bar(x + bar_w, y2_d, width=bar_w,color='r',label='苏州')
plt.xticks(x + bar_w/2, x_d)   #x轴刻度线,刻度线设置在柱的中间
plt.legend()    #显示图例
plt.show()
