for c in "Python123":
    if c == '1':
        continue
    print(c, end=',')
print()
for c in "Python123":
    if c == "1":
        break
    print(c, end=',')