#jieba是优秀的中文分词第三方库
#对中文文本进行分词操作，产生包含产生词语的列表
#安装jieba  第三方库   cmd中 pip install jieba

import  jieba
#精确模式，返回字符串s对应的一个列表类型分词结果
print(jieba.lcut("中国是一个伟大的国家"))
#['中国', '是', '一个', '伟大', '的', '国家']

#全模式，返回字符串s对应的一个列表类型分词结果，存在冗余
print(jieba.lcut("中国是一个伟大的国家", cut_all=True))
#['中国', '国是', '一个', '伟大', '的', '国家']

#向分词词典增加新词w
print(jieba.add_word("蟒蛇语言"))


