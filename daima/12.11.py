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

df2=df.loc[:,['面积','单价','契税',"销售人员"]]#产生一个数据切片，以便显示特定列的统计信息
gdf= df2.groupby('销售人员')#只分组没有进行任何运算
a = df2.groupby('销售人员').mean()#按销售人员分组计算平均值
b = df2.groupby(by=['销售人员','面积']).mean()#按'销售人员'和'面积'分组计算平均值
c = df2.groupby(['销售人员'])['单价'].mean()  # 以销售人员分组，算'单价'的平均值
d=df.groupby(['销售人员']).get_group('人员甲')
print(gdf)
print(a)
print(b)
print(c)
print(d)
