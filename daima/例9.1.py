import os
file = "my.txt" 
if os.path.exists (file): 
  os. remove (file)
else:
  print (file +"文件未找到！")
