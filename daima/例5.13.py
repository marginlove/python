#!-*- coding:utf-8 -*-
print('欢迎光临PYthon手机店'.center(30,'*'))
goods = [["华为",6488],["苹果",5799],["小米",2599],["手机壳",68],["保护模",35],["充电器",169]]
car = [] # 用户购物车
cost = 0 # 用户花费的金额
log = False # 标志位，默认设为False,退出
while not log:
    print("------ 商品列表 ------")
    print("编号    名称    价格")
    for index,i in enumerate(goods):
        print("%s     %s     %s"%(index,i[0],i[1]))
    user_choice = input("\n输入您想购买的产品编号(按“Q”退出):")
    if user_choice.isdigit():
        # 判断用户输入的是否是数字
        user_choice = int(user_choice)  #强制转换为数字
        if user_choice>=0 and user_choice < len(goods):
            # 判断用户购买的商品是否在商品列表中
            car.append(goods[user_choice]) # 加入购物车
            cost += goods[user_choice][1]  # 计算费用
            print("\n %s 已经加入您的购物车\n"%goods[user_choice])
        else:
            print("很抱歉，此商品不存在\n")
    elif user_choice == "Q":
      # 用户选择退出
        if len(car)>0:
            # 判断用户是否购买了商品
            print("\n------ 您的购物清单 ------")
            for index,i in enumerate(car):
                # index和i为临时变量，与前一个for循环里index和i作用的列表不同，故可重用
                print("%s  %s"%(i[0],i[1]))
            print("\n您此次购物的花费合计是:%s元\n"%cost)
            log = True # 退出购物
        else:
            log = True # 未购买商品，不打印购物车商品，直接退出
    else:
        # 输入不合法
        log = True