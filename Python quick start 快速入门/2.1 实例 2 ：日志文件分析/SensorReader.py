#SensorReader.py  传感
#2018-02-28	01:03:16.33393	19.3024	38.4629	45.08	2.68742
try:
    f = open("sensor-data.txt","r")
    #f1 = open("sensor-data.txt", "r")  可
    avg, cnt = 0, 0
    for line in f:
        ls = line.split()
        cnt += 1
        avg += eval(ls[2])
    print("平均的温度是：{:.2f}".format(avg / cnt))
    f.close()
except:
    print("文件打开错误")
