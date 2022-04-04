PI=3.1415
def area(r):
    global s    #s提升为全局变量
    s=r*r*PI
    print(s)
    
area(5)
print(s)
