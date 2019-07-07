#全部大写  upper   全部小写 lower
print("ABCDabcd".lower())
print("ABCDabcd".upper())

#str.split(sep = None)
#返回一个列表,tr根据sep被分隔的部分组成
print("A,B,C,D,a,b,c,d,e,' a'".split(","))
#统计出现的次数
print("aaaaacccc".count('a'))

#替换  old  new
print("aaaabbbbccccABC".replace("a","A"))
#字符串str根据宽度 width 居中，fillchar可选
print("width".center(20,"="))
#去掉str左右  列出的字符
#4567890
print("====1234567890=====+".strip("==123+"))
print(",".join("abcd"))