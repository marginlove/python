import pandas as pd
sExcelFile = "fcxs.xls"
df = pd.read_excel(sExcelFile, sheet_name='Sheet1', header=None)
nrows = df.shape[0]# 获取最大行数
ncols = df.columns.size#获取最大列数
print("====================数据开始=======================")
print('行数: ' + str(nrows))
print('列数: ' + str(ncols))
print(df.iloc[0, 0])# 显示某特定单元格的值
print(df.iloc[0, 1])# 显示某特定单元格的值
print("====================显示某一行=======================")
print("请输入行号(1-" + str(nrows) + "):")
iRow = int(input()) - 1
for iCol in range(ncols):
    print(df.iloc[iRow, iCol],end=' ')
print("\n====================显示某一列=======================")
print("请输入列号(1-" + str(ncols) + "):")
iCol = int(input()) - 1
if iCol >= 0 and iCol <= ncols:
    for iRow in range(nrows):
        print(df.iloc[iRow, iCol],end=' ')
else:
    print('输入了错误的列号')
print("\n逐行逐列显示：")
for iRow in range(nrows):
    for iCol in range(ncols):
        print(df.iloc[iRow, iCol],end=' ')
print()
