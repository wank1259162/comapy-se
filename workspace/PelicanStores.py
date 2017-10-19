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
data_peli.plot.scatter(x=data_peli.iloc[:,4], y=data_peli.iloc[:,8])
plt.show()