import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
x_major_locator=MultipleLocator(5) #把x轴的刻度间隔设置为5
y_major_locator=MultipleLocator(10) #把y轴的刻度间隔设置为10
ax=plt.gca()   #ax为两条坐标轴的实例
ax.xaxis.set_major_locator(x_major_locator) #把x轴的主刻度间隔设置为5
ax.yaxis.set_major_locator(y_major_locator) #把y轴的主刻度设置为10的倍数
plt.xlim(0,50) #把x轴的刻度范围设置为0到50
plt.ylim(-10,100) #把x轴的刻度范围设置为-10到100
plt.show()
