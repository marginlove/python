import matplotlib.pyplot as plt
font = {'family':'SimHei',
        'weight':'bold',
        'size':'15'}#字体(黑体字体) 中文字体
plt.rc('font',**font)
plt.figure(figsize=(15,8), dpi=80)
x=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
y=[21,54,19,16,25,23,12,45,56,34,23,34]
plt.title("2019年度销售统计")
plt.ylabel("十亿人民币")
plt.xlabel("2019年各月份")
plt.grid(color='r',axis='y', linestyle=(0,(5,1)),linewidth=1.1)
plt.plot(x,y,label="销量", linewidth = 2,linestyle='-',
marker='>',markersize=10,color='coral',markerfacecolor = 'blue')
#设置图框线粗细
bwith = 1.5 #边框宽度设置为2
TK = plt.gca()#获取边框
TK.spines['bottom'].set_linewidth(bwith)#图框下边
TK.spines['left'].set_linewidth(bwith)#图框左边
TK.spines['top'].set_linewidth(bwith)#图框上边
TK.spines['right'].set_linewidth(bwith)#图框右边
plt.legend(bbox_to_anchor=(0., 1.02, 0.1, .102), loc=3,ncol=3, mode="expand", borderaxespad=0.)
plt.annotate("年度低点", xy=('7月',12), xycoords='data',xytext=('6月', 35),arrowprops=dict(arrowstyle='->',color='blue', linewidth = 2))
plt.annotate("年度高点", xy=('9月',56), xycoords='data',xytext=('8月', 35),arrowprops=dict(arrowstyle='->',color='red', linewidth = 3))
for a in range(len(x)):     #循环遍历并添加标注文本
        plt.text(x[a],y[a],x[a],fontsize=20)
plt.show()
