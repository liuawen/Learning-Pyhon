# input()
#回声程序 最短输入输出程序
print((input("请输入：")))

#print()
# 将单一字符串或变量直接输出
echo = "这是一个字符串"
print(echo)
print("这是一个字符串")
#将多个变量或字符串直接输出
echo1 = "这是第一个字符串"
echo2 = "这是第二个字符串"
print(echo1, echo2)
#字符串和变量混合输出
echo3 = "A"
print("这是变量{}的输出".format(echo3))# { } 输出的占位
echo4 = 1
print("这是字符{},这是数字{}".format(echo3,echo4))