# 整数类型
print(pow(2,100))
#十进制  100
#二进制  0b 0B
#八进制  0o144   0O
#十六进制 0x64 0X   0x1A

#浮点数类型
print (1.23e-2)
print(1.23E2)
print(1.23E2)
import  sys
print(sys.float_info)
#不确定尾数问题
#浮点数直接运算可能产生不确定尾数问题
print(0.1 + 0.2)
#使用round()辅助浮点数运算，消除不确定尾数
#round(x,d)  对x四舍五入  d 是小数截取位数
print(round(0.1 + 0.2,2))
print(round(0.1 + 0.2,1))
#复数类型
a = 1 + 2j
print(a.real)
print(a.imag)
