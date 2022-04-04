import matplotlib.pyplot as plt
font = {'family':'SimHei','weight':'bold', 'size':'12'}
plt.rc('font',**font)
x_data = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
ln1 = plt.plot(x_data, y_data, color='red', linewidth=1.3, linestyle='-')
ln2 = plt.plot(x_data, y_data2, color='blue', linewidth=1.0, linestyle='-')
plt.legend(handles=[ln1,ln2],labels=['鼠标的年销量','键盘的年销量'],prop=font)
plt.title("电子产品销售量") #设置标题及字体
plt.plot(x_data, y_data)
plt.grid(color='r', linestyle=(0,(5,1)))
for a in range(len(x_data)):
    plt.text(x_data[a],y_data[a],str(y_data[a]/1000)+'k',fontsize=11, color='brown')
    plt.text(x_data[a],y_data2[a],str(y_data2[a]/1000)+'k',fontsize=11, color='purple')
plt.show()
