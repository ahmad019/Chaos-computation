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


steps=100
density=10000

SAMPLES=density*steps


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
    #U = -(w**2)*theta
    eul = d + h*U
    eul2 = theta + h*eul
    euli = d + h/2*(U+eul) 
    eul2i = theta + h/2*(euli+eul2)
    
    d = euli;
    t = t + h;
    theta = eul2i;
    
    time[i]=t;
    theti[i]=eul2i;
    di[i]=euli;
    
    i+=1
    
plt.title("displacement vs time")
plt.plot(time,theti,color='r')
plt.show()
plt.title("derivative vs time")
plt.plot(time,di, color='b')
plt.show()
plt.title("phase plot")
plt.plot(theti,di, color='orange')
plt.show()

