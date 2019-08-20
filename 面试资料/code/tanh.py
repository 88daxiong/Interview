'''
@Descripttion: 
@Author: daxiong
@Date: 2019-08-20 10:36:44
@LastEditors: daxiong
@LastEditTime: 2019-08-20 10:37:39
'''

import matplotlib.pyplot as plt 
import numpy as np
plt.rcParams['font.family']='SimHei'
plt.rcParams['font.sans-serif']=['SimHei']

import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['font.sans-serif']=['SimHei']

x=np.linspace(-10,10,100)
y=(1-np.exp(-2*x))/(1+np.exp(-2*x))
plt.xlabel('x')
plt.ylabel('y')
plt.title("Tanh function and its derivative image")
plt.plot(x,y,color='r',label='Tanh')
y=1-pow((1-np.exp(-2*x))/(1+np.exp(-2*x)),2)
plt.plot(x,y,color='b',label='derivative')
plt.legend()
plt.show()