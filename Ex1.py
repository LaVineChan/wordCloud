# -*- coding:gb18030 -*-
import jieba.analyse
import string
import matplotlib.pyplot as plt
import scipy as scipy
from wordcloud import WordCloud
from scipy.misc import imread
import wordcloud
import imageio
filename = r'data\message'  # ��ȡtxt�ļ�·��


# ��ģ�����ڷ����ļ��е���Ƶ������������ ���� --- Ȩ��Ƶ��
def AnalyzeData():
    f = open(filename + '.txt', 'r', encoding='utf-8',errors='ignore')
    fcontent = f.read()
    alpha = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM,'  # ȥ�������Ĳ���
    tags = jieba.analyse.extract_tags(fcontent, topK=250, withWeight=True)
    new_tags = {}
    for k in range(len(tags)):
        uchar = tags[k][0][0]
        if uchar not in alpha:
            new_tags[tags[k][0]] = int(tags[k][1] * 10000)

    # ����Ƶ-���ﱣ��Ϊ�ļ���ע���ʽ������ķ�ʽ
    with open(filename + '_Word.txt', 'w') as f:
        for i, j in tags:
            if i[0] not in alpha:
                f.write('{:15}\t{:15}'.format(i, int(j * 10000)) + '\n')
            # print('{:8}\t{:10}'.format(i,int(j*10000)))
        f.close()

    # �����ֵ�Ϊwordcloud�ṩ����
    excludes = {"����", "ʲô", "���", "�Ǹ�",'����','û��', 'û��', 'Ȼ��','��ô','�Ǹ�','����','û��','���','����','����','����','һ��','����','��ô','��ü','����','����','֪��'}
    new_tags = {x:new_tags[x] for x in new_tags if x not in excludes}
    return new_tags

def cloudplot():
    # ���ô���������״
    target_coloring = imageio.imread(r'data\alice.png')
    print(AnalyzeData())
    # �Դ�Ƶ�ͱ���ģ��Ϊ�������ɴ��ƶ���
    word_cloud = WordCloud(font_path=r'C:\windows\Fonts\simhei.ttf',
                           background_color="white", max_words=2000, mask=target_coloring).generate_from_frequencies(AnalyzeData())
    # ������ɫ�ֲ�
    image_color = wordcloud.ImageColorGenerator(target_coloring)
    # image_color =


    # �����մ�Ƶ���߽硢Ĭ����ɫ���ɴ���ͼ��
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.figure()

    # ������ɫ������ͼ��ɫ�ʷֲ�����
    plt.imshow(word_cloud.recolor(color_func=image_color))
    plt.axis("off")
    plt.figure()

    # ����ԭʼͼ��
    plt.imshow(target_coloring, cmap=plt.cm.gray)
    plt.axis("off")
    plt.show()

    word_cloud.to_file(filename + '.png')

cloudplot()