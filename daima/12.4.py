import pandas as pd
data = [{'姓名': '张三', '年龄': 12},{'姓名': '李四', '年龄': 10, '家庭地址': '宁波'}]
df = pd.DataFrame(data) # 第 1 行 3 列没有元素，自动添加 NaN
print(df)
