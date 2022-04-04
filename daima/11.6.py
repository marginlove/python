import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,5,0.3) #Numpy 中 arange() 主要是用于生成数组
y = np.arange(-1,1,0.1) #Numpy 中 arange() 主要是用于生成数组
plt.xticks(x)
plt.yticks(y)
t2 = np.arange(0, 5, 0.02)
plt.plot(t2, np.sin(2 * np.pi * t2), 'r--')
plt.grid()
plt.show() 
