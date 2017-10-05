#VISUALIZATION

# -*-coding:utf-8 -*-
from numpy import array
from numpy.random import normal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from   pandas import DataFrame,Series

from matplotlib import pyplot

import pylab as pl

plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


ts = pd.Series( np.random.randn(1000), 
                index=pd.date_range('1/1/2000',
                periods=1000))
				
ts1 = pd.Series( np.random.randn(1000), 
                index=pd.date_range('1/1/2000',
                periods=1000))
				
ts = ts.cumsum()
ts1 = ts1.cumsum()

#*****************方式一
plt.figure(num=1, figsize=(10,7))     #建立图像,图像命名为1，图像大小
#plt.subplots_adjust(wspace=1,hspace=1)
plt.subplot(221,title='TS1')  #将画布切分为2*2块，使用第一块
ts1.plot(label='Ts1',legend=True)  # 添加图例 


#ax1.set_xlable('Time')
#plt.figure()
plt.subplot(222,title='TS')  #将画布切分为2*2块，使用第二块
ts.plot(label='Ts',legend=True) 
plt.subplot(212,title='TS1&TS')  #重新将画布切分为2*1块，使用第二块
ts.plot(label='Ts',legend=True)
ts1.plot(label='Ts1',legend=True)
#plt.subplot(224) #重叠的图像会被覆盖
#ts.plot()
plt.savefig('figure.jpg')


#*******************方式二
fig=plt.figure(figsize=(10,7))              #建立图像画布
plt.subplots_adjust(wspace=0.3,hspace=0.3)  #设置子图像之间的间距
ax1=fig.add_subplot(2,2,1,title='TS1')      #分割画布，建立子图像，命名图像
ax1.set_xlabel('Time')                      #建立子图像相关属性

ts1.plot(ax=ax1,label='TS1',legend=True)    #引入建立的子图像属性



ax2=fig.add_subplot(2,2,2,title='TS')
ax2.plot(ts,label='TS')     # 设置图例
ax2.legend()
ax2.set_xlabel('Time')
ts.plot(ax=ax2,label='TS',legend=True)


ax3=fig.add_subplot(2,1,2,title='TS&TS1')
ax3.plot(ts,label='TS')
ax3.plot(ts1,label='TS1')
ax3.legend()
ax3.set_xlabel('Time')
#plt.grid(True)  显示网格
plt.text(-400,250, r'$\mu=100,\ \sigma=15$')
plt.savefig('figure_22.jpg')
#plt.set_xticklabels('aa')
plt.show()

#Hexagonal Bin Plot

df = pd.DataFrame(np.random.randn(1000, 2), columns=['a', 'b'])
df['b'] = df['b'] + np.arange(1000)
fig1=plt.figure(figsize=(10,7))
ax11=fig1.add_subplot(1,1,1,title='Hexagonal')
df.plot.hexbin(ax=ax11,x='a', y='b', gridsize=25)
plt.show()

# Scatter Plot

df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b');
plt.show()


# Bar plots

plt.figure();
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2.plot.bar();
plt.show()
df2.plot.bar(stacked=True);
plt.show()

df2.plot.barh(stacked=True);
plt.show()

df2.plot.barh();
plt.show()


df4 = pd.DataFrame(
                     {'a': np.random.randn(1000) + 1,'b': np.random.randn(1000),'c': np.random.randn(1000) - 1},
					  columns=['a', 'b', 'c']
				   )
df4.plot.hist(alpha=0.5)
plt.show()

# Box Plots
plt.figure();
df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','C','A','B','B','B','C','C'])
bp = df.boxplot(by='X') #特定列分组计算
plt.show()






