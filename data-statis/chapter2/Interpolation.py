#!/usr/bin/env python
# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
import pylab as pl
import pandas as pd #导入数据分析库Pandas
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


# x=np.linspace(0,10,11)
#x=[  0.   1.   2.   3.   4.   5.   6.   7.   8.   9.  10.]
# y=np.sin(x)
# xnew=np.linspace(0,10,101)
# pl.plot(x,y,"ro")

# for kind in ["nearest","zero","slinear","quadratic","cubic"]:#插值方式
#    "nearest","zero"为阶梯插值
#    slinear 线性插值
#    "quadratic","cubic" 为2阶、3阶B样条曲线插值
    # f=interpolate.interp1d(x,y,kind=kind)
#    ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
    # ynew=f(xnew)
    # pl.plot(xnew,ynew,label=str(kind))
# pl.legend(loc="lower right")
#pl.show()


inputfile = './data/catering_sale.xls' #销量数据路径
outputfile = './tmp/sales.xls' #输出数据路径
data = pd.read_excel(inputfile) #读入数据
data[u'销量'][(data[u'销量'] < 400) | (data[u'销量'] > 5000)] = None

# x1=data.index
# y1=data[u'销量'].dropna()
# x1=y1.index
# y1=data[u'销量']

# pl.plot(x1,y1,"ro")

# f=interpolate.interp1d(x1,y1,kind="cubic")

# xnew1=np.linspace(1,195,195)
# ynew1=f(xnew1)

# plt.figure(num=2, figsize=(10,7))     #建立图像,图像命名为1，图像大小
#data[u'销量'].plot()

# pl.plot(x1,y1,"ro")
# plt.plot(xnew1,ynew1)
 
# plt.show()

data_fill=data[u'销量'].interpolate(method='cubic')
fig=plt.figure(4)

plt.subplots_adjust(wspace=0.3,hspace=0.3)  #设置子图像之间的间距
ax1=fig.add_subplot(2,1,1,title='TS1')      #分割画布，建立子图像，命名图像
ax2=fig.add_subplot(2,1,2,title='TS2')      #分割画布，建立子图像，命名图像

data[u'销量'].plot(ax=ax1,label=u'销量',legend=True)
data_fill.plot(ax=ax2,label='fill',legend=True)
plt.show()