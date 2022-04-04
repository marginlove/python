import pandas as pd
sExcelFile = "fcxs.xls"
df = pd.read_excel(sExcelFile, sheet_name='Sheet1')
print(df.loc[4]['面积'])#输出索引4的面积数据
print(df.loc[[1,2,4]])#输出索引1、2、4行数据
print(df.loc[[1,2,4],['户型','面积']])#输出索引1、2、4行的'户型','面积'数据
print(df.loc[:2,['户型','面积','单价']])#输出0-2行的'户型','面积''单价'数据
print(df.loc[4])#输出索引4的单行数据
