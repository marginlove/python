score=int(input("请输入成绩："))
if score<60:
    print("成绩评定为：E")
elif score<70:
    print("成绩评定为：D")
elif score<80:
    print("成绩评定为：C")
elif score<90:
    print("成绩评定为：B")
else:
    print("成绩评定为：A")