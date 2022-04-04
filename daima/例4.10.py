for i in range(100,1000):
    g=i%10
    s=i//10%10
    b=i//100
    if g*g*g+s*s*s+b*b*b==i:
        print(i)