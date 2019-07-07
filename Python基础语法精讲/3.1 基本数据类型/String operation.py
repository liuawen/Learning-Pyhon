a = "Hello"
b = 'World'
print(a + b)
c = 'hi'
n = 10
print(c*n)
d = 'i'
print(d in c)
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字(1-7)："))
pos = (weekId - 1 ) * 3
print(weekStr[pos: pos+3])

weekStr = "一二三四五六日"
weekId = eval(input("请输入星期数字(1-7)："))
print("星期" + weekStr[weekId-1])
