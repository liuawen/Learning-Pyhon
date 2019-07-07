# to clean data from xuetangx
fi = open("xuetangx.txt", "r", encoding="utf-8")
U = set()
for line in fi:
    if "慕课" in line:
        continue
    if "大学" in line or "学院" in line:
        U.add(line.strip("\n "))

print(" ".join(U))
print(len(U))
fi.close()
