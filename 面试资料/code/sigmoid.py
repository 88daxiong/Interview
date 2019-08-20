'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-20 10:33:48
@LastEditors: daxiong
@LastEditTime: 2019-08-20 10:36:34
'''
import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams['font.family']='SimHei'
plt.rcParams['font.sans-serif']=['SimHei']

import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

x=np.linspace(-10,10,100)
y=1/(1+np.exp(-x))
plt.xlabel("x")
plt.ylabel("y")
plt.title("sigmoid function and its derivative image")
plt.plot(x,y,color='r',label="sigmoid")
y=np.exp(-x)/pow((1+np.exp(-x)),2)
plt.plot(x,y,color='b',label="derivative")
plt.legend()#将plot标签里面的图注印上去
plt.show()
