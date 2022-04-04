person={
  '张帅':{
    '国籍':'中国',
    '民族':'傣族',
    '出生日期':'1977年10月16日',
    '身高':'182cm',
    },
  '陈风':{
    '国籍':'中国',
    '民族':'汉',
    '出生日期':'1976年4月12日',
    '身高':'176.5cm',
    }
  }
for pname,pinfo in person.items():
  print('*********************************')
  print("姓名：",pname)
  for key,value in pinfo.items():
    print(key+':'+value)
