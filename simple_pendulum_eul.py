# -*- coding: utf-8 -*-
"""
iCreated on Wed Jul 11 14:22:50 2018

solving simple pendulum 2nd ODE by using Euler method

equation: 0''=(-g/l)*sin0
          p' = -w^2*sin0

@author: ahmad
"""
import matplotlib.pyplot as plt
import numpy as np


SAMPLES=50000



time = np.ndarray(SAMPLES, float) #array for time steps
theti = np.ndarray(SAMPLES, float)   #for 0 values
di = np.ndarray(SAMPLES, float)     #for 0' (derivative)



d = 0;
h = 0.01;
theta= 2.96;
t = 0;
l=0.5;
w = 9.81/l;


i = 0;

while i<=SAMPLES - 1:
    
    w = 9.81/l;

    U = -(w**2)*np.sin(theta)
   # U = -(w**2)*theta
    eul = d + h*U
    eul2 = theta + h*d
    
    d = eul;
    t = t + h;
    theta = eul2;
    
    time[i]=t;
    theti[i]=eul2;
    di[i]=eul;
    
    i+=1
    
plt.title("displacement vs time")
plt.plot(time,theti, 'r')
plt.show()
plt.title("derivative vs time")
plt.plot(time,di, 'b')
plt.show()
plt.title("phase plot")
plt.plot(theti,di, 'orange')
plt.show()

