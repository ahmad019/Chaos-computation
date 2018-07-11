# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 14:22:50 2018

solving simple pendulum 2nd ODE by using Euler method

equation: 0''=(-g/l)*0
          p' = -w^2*0

@author: ahmad
"""
import matplotlib.pyplot as plt
import numpy as np



time = np.ndarray(1001, float)
theti = np.ndarray(1001, float)
pi = np.ndarray(1001, float)



p = 0;
h = 0.001;
theta= 10;
t = 0;
w = 1;

i = 0;

while i<=1000:

    U = -w*theta
    eul = p + h*U
    eul2 = theta + h*p
    
    p = eul;
    t = t + h;
    theta = eul2;
    
    time[i]=t;
    theti[i]=eul2;
    pi[i]=eul;
    
    i+=1
    

plt.plot(time,theti, 'r')
plt.plot(time,pi, 'b')
plt.show()

