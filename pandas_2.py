#coding=utf8
import pandas as pd
import numpy  as np
from pandas import Series,DataFrame
file_frd=open('frd.txt','r')
data=file_frd.read()
file_frd.close() 
data_1=list(data) 
#data_2='wo  ai bei jing tian an men'
data_2=DataFrame(data_1)
print data_2
#file_frd.write(frid)


