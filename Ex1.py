# -*- coding:gb18030 -*-
import jieba.analyse
import string
import matplotlib.pyplot as plt
import scipy as scipy
from wordcloud import WordCloud
from scipy.misc import imread
import wordcloud
import imageio
filename = r'data\message'  # 读取txt文件路径


# 此模块用于分析文件中的字频，输出结果形如 词语 --- 权重频次
def AnalyzeData():
    f = open(filename + '.txt', 'r', encoding='utf-8',errors='ignore')
    fcontent = f.read()
    alpha = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM,'  # 去除非中文部分
    tags = jieba.analyse.extract_tags(fcontent, topK=250, withWeight=True)
    new_tags = {}
    for k in range(len(tags)):
        uchar = tags[k][0][0]
        if uchar not in alpha:
            new_tags[tags[k][0]] = int(tags[k][1] * 10000)

    # 将词频-词语保存为文件，注意格式化对齐的方式
    with open(filename + '_Word.txt', 'w') as f:
        for i, j in tags:
            if i[0] not in alpha:
                f.write('{:15}\t{:15}'.format(i, int(j * 10000)) + '\n')
            # print('{:8}\t{:10}'.format(i,int(j*10000)))
        f.close()

    #生成需要去掉的无用词
    excludes = {"觉得", "什么", "这个", "那个",'不是','没事', '没有', '然后','怎么','那个','不是','没有','真的','可以','就是','还是','一下','不会','这么','皱眉','现在','干嘛','知道'}
    new_tags = {x:new_tags[x] for x in new_tags if x not in excludes}
    # 返回字典为wordcloud提供依据
    return new_tags

def cloudplot():
    # 设置词云整体形状
    target_coloring = imageio.imread(r'data\alice.png')
    
    # 以词频和背景模板为依据生成词云对象
    word_cloud = WordCloud(font_path=r'C:\windows\Fonts\simhei.ttf',
                           background_color="white", max_words=2000, mask=target_coloring).generate_from_frequencies(AnalyzeData())
    # 生成颜色分布
    image_color = wordcloud.ImageColorGenerator(target_coloring)
    # image_color =


    # 仅按照词频、边界、默认颜色生成词云图像
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.figure()

    # 重新上色，按照图像色彩分布生成
    plt.imshow(word_cloud.recolor(color_func=image_color))
    plt.axis("off")
    plt.figure()

    # 绘制原始图像
    plt.imshow(target_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

    word_cloud.to_file(filename + '.png')

cloudplot()
