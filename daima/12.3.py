import pandas as pd
data = [['张三',34],['李四',45],['小明',54]]
df = pd.DataFrame(data,columns=['Name','Age']) # data转为为行，columns转化为列
print(df)
