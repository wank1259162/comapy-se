import json 
path='C:\workspace\pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records=[json.loads(line) for line in open(path)]
#open(path).readline()
#print records[0]['tz']
#print type(records)

time_zones=[rec['tz'] for rec in records  if 'tz' in rec]
#print time_zones
#print records
#a=[{'bk':'wk1','kk':'wk2'},{'bk':'wk3','lk':'rt'},{'tyu':'9h','bk':'i8'}]
#c=[dd['bk'] for  dd in a ]
#print c

#print time_zones[0:10]
from pandas import DataFrame,Series
import  pandas as pd
import  numpy as np
import  matplotlib.pyplot as plt
import pylab as pl
frame=DataFrame(records)
print frame
print frame['tz'][:10]

tz_counts=frame['tz'].value_counts()
print tz_counts[:10]
tz_counts.plot(kind='barh',rot=0)
#pylab.show()
results=Series([x.split()[0] for x in frame.a.dropna()])
#print results

