#coding:utf-8  
import pandas as pd
import numpy  as np
import itchat
from   pandas import DataFrame,Series
itchat.login()
friends=itchat.get_friends(update=True)
file_frd=open('c:/workspace/frd.txt','w')
#file_frd.write(friends)
#file_frd.write('eew')


names1880=pd.read_csv('C:\workspace\pydata-book-master/ch02/names/yob1880.txt',names=['name','sex','births'])
print names1880
print friends
city_a=[ct['City'] for ct in friends if'City' in ct ]
file_frd.write(city_a)
file_frd.close()
#print city_a

#for i in friends:
#    signature=i['Signature']
#   tlist.append(signature)
#text=''.join(tlist)
frame=DataFrame(city_a)
print frame
