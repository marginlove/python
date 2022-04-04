user=['alibaba','tencent','baidu']
print(user)
user.insert(1,'jd')          #在user列表的第2个元素位置插入新元素'jd'
print(user)
newuser=['suning','pingduoduo']
user.insert(2,newuser)       #在user列表的第3个元素位置插入列表newuser
print(user)
user.insert(0,'taobao')          #在user列表的第1个元素位置插入新元素'taobao'
print(user)