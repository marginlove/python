import matplotlib.pyplot as plt
font = {'family':'SimHei', 'weight':'bold', 'size':'15'}#黑体
plt.rc('font',**font)
plt.figure(figsize=(15,8), dpi=80)
x=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
y=[21,54,19,16,25,23,12,45,56,34,23,34]
plt.title("2019年度销售统计")
plt.ylabel("十亿人民币")
plt.xlabel("2019年各月份")
plt.plot(x,y, linewidth = 2,linestyle=(0,(5,1)),marker='>',
markersize=10,color='coral',markerfacecolor = 'blue')
plt.show()
