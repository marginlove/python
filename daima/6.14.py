stu_score = {'fangming': { 'English': 94, 'Math': 95, 'Chinese': 93,'ave_score': 0 },
     'yanghong': { 'English': 75, 'Math': 82, 'Chinese': 59,'ave_score': 0 },
     'ahenlin': { 'English': 75, 'Math': 65, 'Chinese': 70,'ave_score': 0},
     'bangbai': { 'English': 95, 'Math': 76, 'Chinese': 80,'ave_score': 0 },
     }
for key in stu_score.keys():#求平均分
    for key2 in stu_score[key].keys():
        if key2 !='ave_score':
            stu_score[key]['ave_score']+=stu_score[key][key2]
    stu_score[key]['ave_score'] /=3
    stu_score[key]['ave_score']= float(format(stu_score[key]['ave_score'],'.1f')) #平均分保留一位小数
b = sorted(stu_score.items(), key=lambda x: x[0], reverse=False)#按姓名排序，可以更改排序的Key
#b = sorted(stu_score.items(), key=lambda x: x[1]['ave_score'], reverse=True)
print('排序后:')
for i in b:
    print(i)
print('排序前:')
for key,value in stu_score.items():
    print(key,value)
