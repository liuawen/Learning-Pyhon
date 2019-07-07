# to clean data from icourses
fi = open("icourses.txt", "r", encoding="utf-8")
ls = []
count = 0
for line in fi:
    if "alt" in line:
        tokens = line.split('"')
        uname = tokens[-2]
        print(tokens)
        count += 1
        if "大学生"	in uname:
            continue
        if "大学" in uname or "学院" in uname:
            ls.append(uname)
print(ls)
print(" ".join(ls))
print(len(ls))
fi.close()
print(count)