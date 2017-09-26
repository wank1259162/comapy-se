#coding=utf8
import pandas as pd
import numpy  as np
from pandas import Series,DataFrame

df=DataFrame(np.random.randn(15,3),columns=['a1','b1','c1'])

df1=(df-df.mean())/df.std()
df.corr() # 协方差
df.cov() #相关系数


