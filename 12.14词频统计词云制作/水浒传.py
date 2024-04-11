import jieba
import wordcloud
from imageio import imread
mk=imread("词云图要用到的图片/梅西图.png.jpg")
excludes={"两个","一个","只见","如何","那里","哥哥","说道","军马","头领","众人","这里","兄弟","出来","小人","这个","今日",
"妇人","先锋","好汉","便是","人马","问道","起来","甚么","我们","因此","却是","三个","如此","且说","不知","只是","次日","不曾","呼延","不得","一面","看时","不敢"
,"如今","来到","当下","原来","将军","山寨","喝道","兄长","只得","军士","里面","大喜","正是","不是","天子","一齐",
"知府","性命","商议","小弟","那个","公人","将来","前面","东京","喽罗","那厮","城中","弟兄","下山","不见","怎地"
,"上山","随即","不要","一条","背后","许多","答道","却说","太尉","收拾","一声","回来","只顾","你们","庄客","当时","起身","银子","下来","看见"
,"四个","慌忙","众将","前来","分付","当日","军师","听得","朴刀","兵马","心中","厮杀","向前","安排","朝廷","不肯"
,"那汉","明日","二人","到来","认得","正在","相见","这般","寻思","时迁","下马","几个","有些","两边","马上","娘子","酒店","方才","庄上","一般","乃是","包裹","不能"
,"学究","不在话下","后面","自去","客人","去处","酒保","路上","上马","水军","不可","取出"}
txt=open("D:/大一上课程内容/Python/大一上/课堂/11与12次课/电子书/水浒传.txt","r",encoding="utf-8").read()
words=jieba.lcut(txt)
counts={}
for word in words:
    if len(word)==1:
        continue
    elif word=="宋江道" or word=="宋公明"or word=="呼保义"or word=="孝义黑三郎"or word=="及时雨":
        rword="宋江"
    elif word=="和尚"or word=="洒家" or word=="智深":
        rword="鲁智深"
    else:
        rword=word
    counts[rword]=counts.get(rword,0)+1
for word in excludes:
    del counts[word]
w=wordcloud.WordCloud(width=1000,height=700,background_color="pink",
max_words=36,font_path="词云图要用到的字体/sxt.ttf",mask=mk)
w.generate_from_frequencies(counts)
w.to_file("shz99.png")
print("词云图制作完成！")
items=list(counts.items())
items.sort(key=lambda x:x[1],reverse=True)
for i in range(36):
    word,count=items[i]
    print("{0:<10}{1:>5}".format(word,count))