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



xi = np.ndarray(101, float)
yi = np.ndarray(101, float)
pi = np.ndarray(101, float)



p = 0;
h = 0.01;
theta= 10;
w = 1;

i = 0;

while i<=100:

    U = -w*theta
    eul = p + h*U
    eul2 = theta + h*p
    
    p = eul;
    theta = theta + h;
    y = eul2;
    
    xi[i]=theta;
    yi[i]=eul2;
    pi[i]=eul;
    
    i+=1
    

plt.plot(xi,yi, 'r')
plt.plot(xi,pi, 'b')
plt.show()

