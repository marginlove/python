import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
score = pd.read_csv('test2.csv')# 读取数据集
plt.style.use('ggplot')# 设置图形的显示风格
# 成绩的频数直方图
plt.hist(score .高等数学,# 绘图数据
        bins = 50, # 指定直方图的条形数为50个
        color = 'steelblue',bottom=0, alpha = 0.8,
        edgecolor = 'k', # 指定直方图的边界色
        label = '高等数学成绩直方图')# 为直方图呈现标签
plt.hist(score.计算机,# 绘图数据
        bins = 50, # 指定直方图的条形数为50个
        color = 'y', bottom=0, alpha = 0.5,
        edgecolor = 'red', # 指定直方图的边界色
        label = '计算机成绩直方图')# 为直方图呈现标签
plt.tick_params(top='off', right='off')# 去除图形顶部边界和右边界的刻度
plt.legend()# 显示图例
plt.show()# 显示图形
