total = 0                # 这是一个全局变量
def add( par1, par2 ):   #par1和par2为局部变量
   total = par1 + par2   # total在这里是局部变量.
   print("函数内是局部变量 : ", total)
   return total
 
#调用sum函数
add( 10, 20 )
print("函数外是全局变量 : ", total)
