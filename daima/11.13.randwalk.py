from random import choice# 导入random模块
class RandomWalk(): # 定义生成随机漫步数据的类
      def __init__(self, num_points=6000):
        self.num_points = num_points
        self.x_values = [0] # 初始化列表数值，代表出发点x
        self.y_values = [0] # 初始化列表数值，代表出发点y
      def fill_walk(self):
        """计算随机漫步包含的所有点"""
        while len(self.x_values) < self.num_points: #生成所有数值
            # 下面一段代码，计算随机的数值变化
            x_direction = choice([1, -1])  # 随机返回1或-1
            x_distance = choice([0, 1, 2, 3, 4])  # 随机返回0~4中的一个
            x_step = x_direction * x_distance  # 计算出一个x坐标值
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance  # 计算出一个y坐标值
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的x和y的值
            next_x = self.x_values[-1] + x_step  # 在上一个x坐标值基础上随机漫步
            next_y = self.y_values[-1] + y_step  # 在上一个坐标值基础上随机漫步
            self.x_values.append(next_x) # 添加x值到列表
            self.y_values.append(next_y) # 添加y值到列表
import matplotlib.pyplot as plt
rw = RandomWalk()# RandomWalk类实例化
rw.fill_walk()   # 生成随机的x,y漫步数据
point_num=list(range(rw.num_points)) #生成一个列表，以便下面动态设置颜色
plt.scatter(rw.x_values, rw.y_values, s=1,c=point_num,edgecolors=None) #绘制散点图
plt.show()
