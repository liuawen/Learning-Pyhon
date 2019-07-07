C = (100-32)/1.8
print(C)

#同步赋值语句  同时给多个变量赋值的过程
#可用于j交互变量值
x = 1
y = 2
print("交换前:",x,y)
x, y = y, x
print("交换后:",x,y)
#分支语句  单   二分   多分支
#判断呢？
guess = eval(input("请输入一个整数来猜拳："))
if guess > 99:
    print("猜大了 ")
elif guess < 99:
    print("猜小了 ")
else:
    print("Goodbye 猜对了")