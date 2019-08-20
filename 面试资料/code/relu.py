'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-20 10:37:52
@LastEditors: daxiong
@LastEditTime: 2019-08-20 10:38:44
'''

import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams['font.family']='SimHei'
plt.rcParams['font.sans-serif']=['SimHei']

import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

x=np.linspace(-2,2,100)
y=x*(x>0)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Relu function and its derivative image")
plt.plot(x,y,color='r',label="Relu")

x=np.linspace(-2,0)
y=np.linspace(0,0)
plt.plot(x,y,color='b')

x=np.linspace(0,2)
y=np.linspace(1,1)
plt.plot(x,y,color='b',label="derivative")

plt.legend()

plt.show()
