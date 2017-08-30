#coding=utf8
import pandas as pd
import numpy  as np
from pandas import Series,DataFrame

df=pd.read_csv('itchat_maps.csv')

print df.columns
print df.reindex(index=[22],columns=['NickName','City','Signature'])

#print df.reindex([20])
