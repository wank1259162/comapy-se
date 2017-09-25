#-*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#参数初始化
inputfile = 'Shadow02.xlsx'
#data = pd.read_excel(inputfile, index_col = u'序号') #导入数据
data = pd.read_excel(inputfile) #导入数据

grouped =data.groupby(data['Exchange']).count()
grouped.plot(kind='bar')
plt.show()
