#String
str = "Python"
print(str[0])
print(str[-1])
#多行字符三个单引号 或三个双引号 表示
s = '''Hello
World
!'''
print(s)
#字符串的索引 和 切片
print("零一二三四五六七八九十"[0])
#返回字符串中的一段 string[M:N] 字符串不包含 N
print("零一二三四五六七八九十[0:5]"[0:5])
#<字符串>[M:N]  M缺失表示至开头  N缺失表示至结尾
print("零一二三四五六七八九"[:9])
print("零一二三四五"[1:])
#<string>[M:N:K],根据步长K对字符串切片
print("零一二三四五"[::2])
print("零一二三四五六七八九"[::-1])#倒的