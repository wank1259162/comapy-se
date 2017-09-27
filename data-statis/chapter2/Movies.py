from numpy import array
from numpy.random import normal
import pandas as pd
from   pandas import DataFrame,Series
from matplotlib import pyplot
#参数初始化
inputfile = 'Movies.xlsx'
#data = pd.read_excel(inputfile, index_col = u'序号') #导入数据
data_movies = pd.read_excel(inputfile) #导入数据

pyplot.scatter(data_movies[u'Opening Gross'],data_movies[u'Total Gross'])
pyplot.xlabel('Opening Gross')
pyplot.ylabel('Total Gross')
pyplot.title('Opening Gross &Total Gross')
pyplot.show()