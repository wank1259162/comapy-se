#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl
import pandas as pd #导入数据分析库Pandas
import matplotlib.pyplot as plt

inputfile = './data/catering_sale.xls' #销量数据路径
outputfile = './tmp/sales.xls' #输出数据路径
data = pd.read_excel(inputfile) #读入数据

data.fillna(0,inplace=True)
#data.fillna(data.dropna().mean,inplace=True)
# data_n=data_movies.iloc[:,1:5]
data_zs = 1.0*(data[u'销量'] - data[u'销量'].mean())/data[u'销量'].std()  #数据标准化
k = 3#聚类的类别
iteration = 500 #聚类最大循环次数
threshold = 2 #离散点阈值

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 1, max_iter = iteration,n_init=20) #分为k类，并发数4
model.fit(data_zs.reshape((len(data_zs), 1))) #开始聚类

c = pd.DataFrame(model.cluster_centers_).sort_values(0) #输出聚类中心，并且排序（默认是随机序的）
w = pd.rolling_mean(c, 2).iloc[1:] #相邻两项求中点，作为边界点
#w = [0] + list(w[0]) + [data_zs.max()] #把首末边界点加上
w1=list(w[0])
w1.insert(1,0)
w = w1+ [data_zs.max()] #把首末边界点加上
d3 = pd.cut(data_zs,bins=w,labels = range(k))


def cluster_plot(d, k): #自定义作图函数来显示聚类结果
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  
  plt.figure(figsize = (8, 3))
  for j in range(0, k):
    plt.plot(data_zs[d==j], [j for i in d[d==j]], 'o')
  
  plt.ylim(-0.5, k-0.5)
  return plt

cluster_plot(d3, k).show()



#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
# r.columns = list(data.columns) + [u'类别数目'] #重命名表头
r.columns = [u'销量'] + [u'类别数目'] #重命名表头
print(r)


#标准化数据及其类别
r = pd.concat([data_zs, pd.Series(model.labels_, index = data.index)], axis = 1)  #每个样本对应的类别
r.columns =[u'销量']  + [u'聚类类别'] #重命名表头

norm = []
for i in range(k): #逐一处理
  norm_tmp = r[u'销量'][r[u'聚类类别'] == i]-model.cluster_centers_[i]
#norm_tmp = norm_tmp.apply(np.linalg.norm, axis = 1) #求出绝对距离

  norm_tmp = norm_tmp.apply(np.linalg.norm) #求出绝对距离
  norm.append(norm_tmp/norm_tmp.median()) #求相对距离并添加

norm = pd.concat(norm) #合并

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
norm[norm <= threshold].plot(style = 'go') #正常点

discrete_points = norm[norm > threshold] #离群点
discrete_points.plot(style = 'ro')

for i in range(len(discrete_points)): #离群点做标记
  id = discrete_points.index[i]
  n = discrete_points.iloc[i]
  plt.annotate('(%s, %0.2f)'%(id, n), xy = (id, n), xytext = (id, n))

plt.xlabel(u'编号')
plt.ylabel(u'相对距离')
plt.show()









plt.figure(11)  
from sklearn.manifold import TSNE

tsne = TSNE()
tsne.fit_transform(pd.DataFrame(data_zs)) #进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index = pd.DataFrame(data_zs).index) #转换数据格式
# tsne = pd.DataFrame(data_zs, index = pd.DataFrame(data_zs).index) #转换数据格式

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
#plt.grid(True)  显示网格
#plt.text(-400,250, r'$\mu=100,\ \sigma=15$')
plt.annotate('local max', xy=(-200, 100), xytext=(-300, 1.5),arrowprops=dict(facecolor='black', shrink=0.05))
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()