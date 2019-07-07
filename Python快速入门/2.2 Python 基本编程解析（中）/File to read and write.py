#一次性全部读入文件
f = open("file.txt","r")
txt = f.read()
print(txt)
f.close()
#文件的按行读入
fileReadLine = open("file.txt","r")
i = 1
for line in fileReadLine:
    print("en:",line)
fileReadLine.close()
