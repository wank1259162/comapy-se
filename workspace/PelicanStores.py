from numpy import array
from numpy.random import normal
import pandas as pd
from   pandas import DataFrame,Series
from matplotlib import pyplot
import matplotlib.pyplot as plt
#参数初始化
#inputfile = 'PelicanStores.csv'
inputfile = 'fil.csv'

data_peli=pd.read_csv(inputfile) #导入数据
#data_peli.plot.scatter(x=data_peli.iloc[:,4], y=data_peli.iloc[:,8])
#data_peli.plot.scatter(x=data_peli.iloc[:,4], y=data_peli.iloc[:,8])
fig=plt.figure(figsize=(10,7))
#ax1=fig.add_subplot(2,2,1,title='TS1')
#ax1.set_xlabel('Time')
#ts1.plot(ax=ax1,label='TS1',legend=True)
#净销售额和顾客年龄间的散点图
plt.scatter(data_peli[u'Age'],data_peli[u'Net Sales'])

plt.show()

#plt.box(data_peli[u'Net Sales'])
plt.ylabel("ARI") 
plt.xlabel("Dissimilarity Measures") 
data_peli[u'Net Sales'].plot.box()
plt.show()
data_peli.plot.box()

