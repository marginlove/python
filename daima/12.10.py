#需安装模块xlwt
import pandas as pd
sExcelFile = "fcxs.xls"
df = pd.read_excel(sExcelFile, sheet_name='Sheet1')
#省略数据宽度设置和中文对齐，自行参照例8
values={'契税':0.15}
df.fillna(value=values,inplace=True,axis=0)
values={'契税':0.15,'契税总额':df.面积*df.单价*df.契税,'房价总额':df.面积*df.单价}
df.fillna(value=values,inplace=True,axis=0)
print(df)
df.to_excel(r'DataTest1.xls',sheet_name='Sheet1')#输出df到excel文件中
print(df.describe().round(2))
#print(df2.describe(include=['number']).loc[['min', 'max', 'mean', 'std']].round(2))
#print(df2.describe(percentiles=[.65,.75,.8],include='number').round(2))
'''
df2=df.loc[:,['面积','单价','契税']]#产生一个数据切片，以便显示特定列的统计信息
df3=df2.describe(percentiles=[.65,.75,.8],include='number')
print(df3.round(2))#显示数值的统计信息
df3.to_excel(r'DataTest11.xls',sheet_name='Sheet1')#输出df到excel文件中
print(df3)
'''

