#-*- coding: utf-8 -*-

import pandas as pd

df_wine = pd.read_csv('data/wine.data', header=None)


from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values # 把数据与标签拆分开来
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=0) # 把整个数据集的70%分为训练集，30%为测试集

# 下面3行代码把数据集标准化为单位方差和0均值
sc = StandardScaler()
X_train_std = sc.fit_transform(X_train)
X_test_std = sc.fit_transform(X_test)

import numpy as np
cov_mat = np.cov(X_train_std.T)
cov_mat.shape # 输出为(13, 13）

import numpy as np
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)

eigen_vecs.shape # 输出为(13, 13）


tot = sum(eigen_vals) # 求出特征值的和
var_exp = [(i / tot) for i in sorted(eigen_vals, reverse=True)] # 求出每个特征值占的比例（降序）
cum_var_exp = np.cumsum(var_exp) # 返回var_exp的累积和

import matplotlib.pyplot as plt

# 下面的代码都是绘图的，涉及的参数建议去查看官方文档
plt.bar(range(len(eigen_vals)), var_exp, width=1.0, bottom=0.0, alpha=0.5, label='individual explained variance')
plt.step(range(len(eigen_vals)), cum_var_exp, where='post', label='cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.show()

eigen_pairs =[(np.abs(eigen_vals[i]),eigen_vecs[:,i]) for i in range(len(eigen_vals))] # 把特征值和对应的特征向量组成对
eigen_pairs.sort(reverse=True) # 用特征值排序

first = eigen_pairs[0][1]
second = eigen_pairs[1][1]
first = first[:,np.newaxis]
second = second[:,np.newaxis]
w= np.hstack((first,second))

X_train_pca = X_train_std.dot(w) # 转换训练集
colors = ['r', 'b', 'g']
markers = ['s', 'x', 'o']
for l, c, m in zip(np.unique(y_train), colors, markers):
    plt.scatter(X_train_pca[y_train==l, 0], X_train_pca[y_train==l, 1], c=c, label=l, marker=m) # 散点图
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.legend(loc='lower left')
plt.show()

#from mlxtend.evaluate import decision_regions
#from mlxtend.evaluate import decision_regions.plot_decision_regions

from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
pca = PCA(n_components=2) # 保留2个主成分
lr = LogisticRegression() # 创建逻辑回归对象
X_train_pca = pca.fit_transform(X_train_std) # 把原始训练集映射到主成分组成的子空间中
X_test_pca = pca.transform(X_test_std) # 把原始测试集映射到主成分组成的子空间中
lr.fit(X_train_pca, y_train) # 用逻辑回归拟合数据

from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train_pca, y_train, clf=lr)
#decision_regions.plot_decision_regions(X_train_pca, y_train)
lr.score(X_test_pca, y_test) # 0.98 在测试集上的平均正确率为0.98
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend(loc='lower left')
plt.show()

pca = PCA(n_components=None) # 保留所有的主成分
X_train_pca = pca.fit_transform(X_train_std)
pca.explained_variance_ratio_