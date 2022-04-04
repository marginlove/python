import re

string = "<span class=p_t>/114页</span>"
num = re.findall(r"\d+", string)
print(num[0])