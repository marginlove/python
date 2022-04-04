import pandas as pd
sExcelFile = "fcxs.xls"
df = pd.read_excel(sExcelFile, sheet_name='Sheet1')
pd.set_option('display.max_colwidth', 1000)#单列数据宽度，以字符个数计算，超过时用省略号表示
pd.set_option('display.width', 1000)#数据显示区域的总宽度，以总字符数计算
pd.set_option('display.max_columns', 1000)#最大显示列数，超过该值用省略号代替，为None时显示所有列
# 中文标题时对齐数据,这两个参数的默认设置都是False
pd.set_option('display.unicode.ambiguous_as_wide', True)#中文标题时对齐数据
pd.set_option('display.unicode.east_asian_width', True)#中文标题时对齐数据
values={'契税':0.15}
df.fillna(value=values,inplace=True,axis=0)
values={'契税':0.15,'契税总额':df.面积*df.单价*df.契税,'房价总额':df.面积*df.单价}
df.fillna(value=values,inplace=True,axis=0)
print(df)
