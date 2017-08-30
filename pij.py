 # -*- coding:utf-8 -*-
import jieba
import jieba.analyse as analyse
import matplotlib.pyplot as plt  
import codecs
from wordcloud import WordCloud
from scipy.misc import imread
from os import path
with codecs.open('pjl_comment.txt',encoding='utf-8') as f:
    comment_text = f.read()
    cut_text = " ".join(jieba.cut(comment_text))
    d = path.dirname(__file__) 
    color_mask = imread("e:/python/workspace/love.jpg") # 读取背景图片
    cloud = WordCloud(
	                   #font_path=path.join(d,'simsun.ttc'),
					   font_path='C:\Windows\Fonts\Arial.ttf',
	                   background_color='white',
	                   mask=color_mask,
	                   max_words=2000,
	                   max_font_size=40
					  )
					  
word_cloud = cloud.generate(cut_text) # 产生词云
plt.figure()  
# 以下代码显示图片  
plt.imshow(word_cloud)  
plt.axis("off")  
plt.show() 
word_cloud.to_file("pjl_cloud.jpg")



 
