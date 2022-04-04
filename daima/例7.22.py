def hannuo(k,a,b,c):
  if(k==1):
    print("move",k,"from",a,"to",c)
  else:
    hannuo(k-1,a,c,b)
    print("move",k,"from",a,"to",c)
    hannuo(k-1,b,c,a)

hannuo(4,'a','b','c')
