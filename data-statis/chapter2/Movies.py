#-*- coding: utf-8 -*-
from numpy import array
from numpy.random import normal
import pandas as pd
from   pandas import DataFrame,Series
from matplotlib import pyplot
import matplotlib.pyplot as plt
#参数初始化
inputfile = 'Movies.xlsx'
#data = pd.read_excel(inputfile, index_col = u'序号') #导入数据
data_movies=pd.read_excel(inputfile) #导入数据

pyplot.scatter(data_movies[u'Opening Gross'],data_movies[u'Total Gross'])
pyplot.xlabel('Opening Gross')
pyplot.ylabel('Total Gross')
pyplot.title('Opening Gross &Total Gross')
pyplot.show()


bins=[0,3,6,10,35,100]

cats=pd.cut(data_movies[u'Opening Gross'],bins)

data_group=data_movies.groupby(by=cats)
data_n=data_movies.iloc[:,1:5]
data_zs = 1.0*(data_n - data_n.mean())/data_n.std() #数据标准化
k = 4 #聚类的类别
iteration = 500 #聚类最大循环次数

from sklearn.cluster import KMeans
model = KMeans(n_clusters = k, n_jobs = 1, max_iter = iteration,n_init=20) #分为k类，并发数4
model.fit(data_zs) #开始聚类

#简单打印结果
r1 = pd.Series(model.labels_).value_counts() #统计各个类别的数目
r2 = pd.DataFrame(model.cluster_centers_) #找出聚类中心
r = pd.concat([r2, r1], axis = 1) #横向连接（0是纵向），得到聚类中心对应的类别下的数目
r.columns = list(data_n.columns) + [u'类别数目'] #重命名表头
print(r)

#详细输出原始数据及其类别
r = pd.concat([data_n, pd.Series(model.labels_, index = data_n.index)], axis = 1)  #详细输出每个样本对应的类别
r.columns = list(data_n.columns) + [u'聚类类别'] #重命名表头
r.to_excel('discretization_data.xls') #保存结果

r1 = pd.concat([data_movies, pd.Series(model.labels_, index = data_n.index)], axis = 1)  #详细输出每个样本对应的类别
r1.columns = list(data_movies.columns) + [u'聚类类别'] #重命名表头
r1.to_excel('discretization1_data.xls') #保存结果


def density_plot(data): #自定义作图函数
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex = False)
  [p[i].set_ylabel(u'密度') for i in range(k)]
  plt.legend()
  plt.subplots_adjust(wspace=0.3,hspace=0.3)
  return plt

pic_output = 'pd_' #概率密度图文件名前缀
for i in range(k):
  density_plot(data_n[r[u'聚类类别']==i]).savefig(u'%s%s.png' %(pic_output, i))

plt.figure(11)  
from sklearn.manifold import TSNE
tsne = TSNE()
tsne.fit_transform(data_zs) #进行数据降维
tsne = pd.DataFrame(tsne.embedding_, index = data_zs.index) #转换数据格式

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

#不同类别用不同颜色和样式绘图
d = tsne[r[u'聚类类别'] == 0]
plt.plot(d[0], d[1], 'r.')
d = tsne[r[u'聚类类别'] == 1]
plt.plot(d[0], d[1], 'go')
d = tsne[r[u'聚类类别'] == 2]
plt.plot(d[0], d[1], 'b*')
plt.show()







