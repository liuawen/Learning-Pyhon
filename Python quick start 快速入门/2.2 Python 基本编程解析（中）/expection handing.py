#异常处理：对程序执行异常的处理机制，提高用户体验
try:
    f = open("sensor-data-no-exist.txt", "r")
    for line in f:
        print(line)
    f.close()
except:
    print("文件不存在")