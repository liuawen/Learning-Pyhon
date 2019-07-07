#Python整数没有取值范围限制
#浮点数存在取值范围，但很大，计算机存储问题
'''
与数学中的复数概念相同，定义 j =	−𝟏，复数表示为 a+bj
z = a+bj，a是实部，b是虚部，a和b都是浮点数
z.real获得z的实部，z.imag获得z的虚部
由0个或多个字符组成的有序字符序列
字符串由一对单引号或一对双引号表示，如："字符串" 或	'字符串'
字符串是字符的有序序列，可以用序号访问，如："字符串"[1]="符"
索引：s[N] 通过序号获取单个字符
如："字符串"[-1]="串"
切片：s[N:M]获取M到N(不含)子串 如："字符串"[0:-1]="字符"
'''

'''
由0个或多个字节组成的有序序列，每字节对应值为0-255
字节串由前导符b或B与一对单引号或双引号表示，如：b"a\xf6"
'''
#0-255间非可打印字符用 \xNN 方式表示，N是一个十六进制字符


#集合类型
A = {"Python",123,("Python",123)}
print(A)

#元组类型   序列类型的一种，元素间的有序组合，一旦创建不能被修改
#元组使用小括号()表示，元素间用逗号分隔，小括号可以省略

rgbcolor = 21, 11, 125
print(rgbcolor)

#列表类型 序列类型的一种，元素间的有序组合，类型不限，创建后可以随时被修改
#列表使用中括号[]表示，元素间用逗号分隔，括号不可省略

ls = ["cat", "tiger", 1024]
print(ls)

#字典类型  字典类型是键值对的集合，反映了数据之间的映射关系
#字典使用大括号{}表示，键值间用冒号分隔，键值对间用逗号分隔

d = {"中国":"北京", "美国":"华盛顿", "法国":"巴黎"}
print(d["中国"])
