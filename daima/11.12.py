import numpy as np
import matplotlib.pyplot as plt
np.random.seed(1) #随机种子
x = np.random.rand(100) #随机数生成
y = np.random.rand(100) #随机数生成
colors = np.random.rand(100) #随机数生成
plt.scatter(x, y, s=10, c=colors, alpha=0.8) #散点图绘制
plt.show()#显示图
