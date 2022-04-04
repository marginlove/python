import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.sans-serif'] = [u'SimHei'] #字体设置
plt.rcParams['axes.unicode_minus'] = False
sExcelFile = "气象.csv"
df = pd.read_csv(sExcelFile)
pd.set_option('display.max_colwidth', 1000)#单列数据宽度，以字符个数计算，超过时用省略号表示
pd.set_option('display.width', 1000)#数据显示区域的总宽度，以总字符数计算
pd.set_option('display.max_columns', 1000)#最大显示列数，超过该值用省略号代替，为None时显示所有列
# #中文标题时对齐数据这两个参数的默认设置都是False
pd.set_option('display.unicode.ambiguous_as_wide', True)#中文标题时对齐数据
pd.set_option('display.unicode.east_asian_width', True)#中文标题时对齐数据
print(df.shape)
print(df.dtypes)
print(df.head(2))
print(df.tail(2))
print(df.describe())
print(df.corr(method='pearson'))
fig=plt.figure()
ax=fig.add_subplot(111)
cax=ax.matshow(df.corr(),vmin=-1,vmax=1,interpolation='none')
fig.colorbar(cax)
ticks=np.arange(0,6,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(['夜间温度','夜间湿度','晚上降水量','白天温度','白天湿度','白天降水量'])
ax.set_yticklabels(['夜间温度','夜间湿度','晚上降水量','白天温度','白天湿度','白天降水量'])
plt.show()

