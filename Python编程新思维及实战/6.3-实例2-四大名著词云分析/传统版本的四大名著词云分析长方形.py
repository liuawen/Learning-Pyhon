# for WordCloud
import jieba
import wordcloud
names = {"红楼梦.txt", "三国演义.txt", "水浒传.txt", "西游记.txt"}

for name in names:
    f = open(name, "r", encoding="utf-8")  t = f.read()
    f.close()
    ls = jieba.lcut(t)
    txt = " ".join(ls)
    w = wordcloud.WordCloud(	font_path = "msyh.ttc",\
                                width = 1000, height = 700 \
    )
    w.generate(txt)
    w.to_file(name.split(".")[0] + ".png")
