import pandas as pd
data = {'品名': ['鱼', '青菜', '豆腐', '芦笋', '猪肉', '羊肉'],
        '价格': [20, 4, 5, 12, 40, 80],
        '单位': [1000, 500, 500, 500, 1000, 1000]}
frame = pd.DataFrame(data)# 或df = pd.DataFrame.from_dict(data)
print(frame)
