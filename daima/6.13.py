km=['语文','高数','英语','计算机','大学物理','哲学','思政','金融学']
stu={'name':'ccg','num':21012,'subject':km,'score':[98,99,100,34,76,56,87,86]}
print('学号：',stu['num'],'姓名：',stu['name'])
print('本学期分数:')
for k in stu['subject']:
     print(k,end=' ')
print()
for i in stu['score']:
     print(i,end=' ')
