import numpy as np
import matplotlib.pyplot as plt
font = {'family':'SimHei','weight':'bold', 'size':'12'}
plt.rc('font',**font)
data = [ ("2岁", 85), ("3岁", 93), ("4岁", 100.2), ( "5岁", 107),
        ("6岁", 113.1), ( "9岁", 129.6), ("10岁", 134.0), ( "15岁", 174)]
N = len(data)
x = np.arange(1,N+1) #Numpy 中 arange() 主要是用于生成数组
y = [ num for (s, num) in data ]
labels = [ s for (s, num) in data ]
width = 0.5
bar1 = plt.bar(x, y, width, color="b" )
plt.ylabel( '身高' )
plt.xticks(x , labels )
plt.ylim(40,200)
plt.show()
