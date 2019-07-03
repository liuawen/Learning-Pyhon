print('F' in ['F','f']) #True
#保留字in  成员判断

print("C" in ['F','f']) #False
print("C" in ['C','c']) #True
#评估函数eval() 去掉参数最外侧引号并执行余下语句的函数

print(eval('1+2')) #3
eval('print("hello")')  #hello
#字符串  数字
f = 1.234567898
print("？？为{:.2f}".format(f))