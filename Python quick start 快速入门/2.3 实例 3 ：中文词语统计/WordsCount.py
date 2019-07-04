#WordsCount.py
#引用外部功能库
import jieba
#打开文件
f = open("2018年一号文件.txt", "r", encoding="utf-8")
#读入文件
txt = f.read()
#关闭文件
f.close()
print(txt)
ls = jieba.lcut(txt)#中文分词
#形成键值对关系   词  与  次数 
d = {}#建立字典
#利用字典词语统计
for w in ls:
    d[w] = d.get(w, 0) + 1
#遍历结果 设置条件 打印输出
#标点符号也算 我把文件.txt改成utf-8 的 满足50的太少了  换下10
for k in d:
    if d[k] >= 10 and k != "\n":#不输出换行的
        print('"{}"出现{}次'.format(k,	d[k]))
