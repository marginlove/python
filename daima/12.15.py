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

df.plot(x='时间',subplots=True, figsize=(6, 6),title='宁波2019降水、温度、湿度图')
plt.legend(loc='best')#对数据框相同索引分列分别作图
plt.show()
#删除异常数据
df= df.drop(df[df['夜间温度'] == 999].index)
df.plot(x='时间',subplots=True, figsize=(6, 6),title='宁波2019降水、温度、湿度图')
plt.legend(loc='best')#对数据框相同索引分列分别作图
plt.show()

