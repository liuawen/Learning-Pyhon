# else 扩展
for c in "python":
    if c == "t":
        continue
    print(c, end=",")
else:
    print("正常退出")

for c in 'PYTHON':
    if c =='T':
        break
    print(c, end=',')
else:
    print("正常退出")