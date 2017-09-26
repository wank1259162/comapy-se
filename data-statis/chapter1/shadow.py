#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#参数初始化
inputfile = 'Shadow02.xlsx'
#data = pd.read_excel(inputfile, index_col = u'序号') #导入数据
data = pd.read_excel(inputfile) #导入数据

grouped =data.groupby(data['Exchange']).count()
#grouped.plot(kind='bar')
#plt.show()

bins=np.array([0,15,30,45,60,75])
#labels=data.cut()
labels=pd.cut(data.GPM,bins)
pd.value_count(labels)

#grouped1 = data.groupby(['GPM',labels])
#sum=grouped1.GPM.sum()

data.GPM.hist(
               bins=[0,14.9,15,29.9,30,44.9,45,59.9,60,75],
               grid=False,
               figsize=(10,7)
              ).get_figure().savefig('shadow.jpg')
#plt.show()
#grouped1.size().unstack(0)
#grouped1.plot(kind='bar')
plt.show()
#plt.savefig('dog.jpg')
