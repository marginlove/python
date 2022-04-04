import pandas as pd
import numpy as np
sExcelFile = "fcxs.xls"
df = pd.read_excel(sExcelFile, sheet_name='Sheet1')
#省略数据宽度设置和中文对齐，自行参照例8
values={'契税':0.15}
df.fillna(value=values,inplace=True,axis=0)
values={'契税':0.15,'契税总额':df.面积*df.单价*df.契税,'房价总额':df.面积*df.单价}
df.fillna(value=values,inplace=True,axis=0)
print(df)
df.to_excel(r'DataTest1.xls',sheet_name='Sheet1')#输出df到excel文件中
df2=df.loc[:,['面积','单价','契税',"销售人员"]]
df2=df2.sort_values('单价')
df2=df2.groupby(by="销售人员")
df2=df2.aggregate([min,np.mean,np.median,max]).T  #转置结果，方便观察结果
print(df2)
