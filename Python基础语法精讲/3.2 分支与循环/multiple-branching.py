score = eval(input("输入:"))
if score <= 60:
    grade = "GG"
elif score <= 70:
    grade = "D"
elif score <= 80:
    grade = "C"
elif score <= 90:
    grade = "B"
elif score <= 100:
    grade = "A"
print("输入成绩属于级别{}".format(grade))