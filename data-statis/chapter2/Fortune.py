from numpy import array
from numpy.random import normal
import pandas as pd
from   pandas import DataFrame,Series
from matplotlib import pyplot

#参数初始化
inputfile = 'Fortune.xlsx'
#data = pd.read_excel(inputfile, index_col = u'序号') #导入数据
data_fortune = pd.read_excel(
                              inputfile,names=['Company','Equity','Market-Value','Profit'],
                              skiprows=[0]
							 ) #导入数据
pd.crosstab(data_fortune.Equity,data_fortune.Profit,margins=True)

#绘制散点图

pyplot.scatter(data_fortune.Equity,data_fortune.Profit)
pyplot.xlabel('Equity')
pyplot.ylabel('Profit')
pyplot.title('Equity &Profit')
pyplot.show()

drawScatter(heights, weights)

