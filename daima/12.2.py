import pandas as pd
mydata= [('鱼', 20, 1000),
         ( '青菜',4,500),
         ('豆腐' , 5 ,  500),
        ('芦笋' , 12 ,  500),
        ('猪肉' , 40 , 1000)
         ]
labels = ['品名', '价格', '单位']
mf2 = pd.DataFrame.from_records(mydata, columns=labels)
print(mf2)
