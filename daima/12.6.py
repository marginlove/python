#xlrd模块必须先安装,如果报错，原因是xlrd版本的问题，现在直接pip install xlrd下载的是2.0.1版本的，将其卸载下载1.2.0的即可
# 或者把文件名fcxs.xlsx改为fcxs.xls
import pandas as pd
sExcelFile = "fcxs.xls"
df = pd.read_excel(sExcelFile, sheet_name='Sheet1')
print(df)
