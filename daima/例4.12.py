for x in range(21):

    for y in range(34):

        z = 100 - x - y       # 减少重复项

        if  5*x+3*y+z/3==100:

            print('公鸡：%d 母鸡：%d 小鸡：%d'%(x,y,z))