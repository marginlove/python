import matplotlib.pyplot as plt
font = {'family':'SimHei',
        'weight':'bold',
        'size':'12'}
plt.rc('font',**font)
labels='冬瓜','土豆','青菜','肉'
sizes=15,20,56,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
