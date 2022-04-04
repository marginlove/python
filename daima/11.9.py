import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.sans-serif']=['SimHei']   # 用黑体显示中文
matplotlib.rcParams['axes.unicode_minus']=False     # 正常显示负号
data = np.random.randn(98000) # 随机生成正态分布的数据
print(data)
plt.hist(data, bins=40, facecolor="steelblue", edgecolor="black", alpha=0.7)
plt.xlabel("范围")
plt.ylabel("频数/频率")
plt.title("频数/频率分布直方图")
plt.show()
