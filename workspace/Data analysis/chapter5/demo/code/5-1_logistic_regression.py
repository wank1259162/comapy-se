#-*- coding: utf-8 -*-
#逻辑回归 自动建模
import pandas as pd

#参数初始化
filename = '../data/bankloan.xls'
data = pd.read_excel(filename)
x = data.iloc[:,:8].as_matrix()
y = data.iloc[:,8].as_matrix()

from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 
rlr = RLR() #建立随机逻辑回归模型，筛选变量
rlr.fit(x, y) #训练模型
rlr.get_support() #获取特征筛选结果，也可以通过.scores_方法获取各个特征的分数
#print(u'通过随机逻辑回归模型筛选特征结束')
#print(u'有效特征为：%s' % ','.join(data.columns[rlr.get_support()]))
x = data[data.columns[rlr.get_support()]].as_matrix() #筛选好特征
lr = LR() #建立逻辑货柜模型
lr.fit(x, y) #用筛选后的特征数据来训练模型
#print(u'逻辑回归模型训练结束。')
#print(u'模型的平均正确率为：%s' % lr.score(x, y)) #给出模型的平均正确率，本例为81.4%


from sklearn.decomposition import PCA
data_1=data.iloc[:,:8]

pca = PCA()
pca.fit(data_1)
pca.components_ #返回模型的各个特征向量
pca.explained_variance_ratio_ #返回各个成分各自的方差百分比
low_d=pca.transform(data_1)
pd.DataFrame(low_d).to_excel('low_d_all.xls')

pca = PCA(4)
pca.fit(data_1)
pca.components_ #返回模型的各个特征向量
pca.explained_variance_ratio_ #返回各个成分各自的方差百分比

low_d1=pca.transform(data_1)
pd.DataFrame(low_d1).to_excel('low_d_4.xls')
#data_2=pca.inverse_transform(low_d)

