
from numpy import array
from numpy.random import normal
import pandas as pd
from   pandas import DataFrame,Series
from matplotlib import pyplot

tips = pd.read_csv('tips.csv')
tips['tip_pct'] = tips['tip'] / tips['total_bill']

def top(df, n=5, column='tip_pct'):
    #return df.sort_index(by=column)[-n:]  #依据指定列排序
     return df.sort_values(by=column)[-n:]

top(tips, n=6)

tips.groupby('smoker').apply(top,n=10)