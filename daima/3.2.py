x1="日照香炉生紫烟"
x2="遥看瀑布挂前川"
x3="飞流直下三千尺"
x4="疑是银河落九天"
f=open("古诗.txt","w")#打开古诗.txt，w表示打开的权限为写入
print(x1,x2,sep=",",end=" 。",file=f)#输出结果不在屏幕显示，而是输出到古诗.txt
print(x3,x4,sep=",",end=" 。",file=f) #输出结果不在屏幕显示，而是输出到古诗.txt
