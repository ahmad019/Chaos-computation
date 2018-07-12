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
from math import sin 

SAMPLES=50000



time = np.ndarray(SAMPLES, float) #array for time steps
theti = np.ndarray(SAMPLES, float)   #for 0 values
pi = np.ndarray(SAMPLES, float)     #for 0' (derivative)



p = 0;
h = 0.001;
theta= 10;
t = 0;
w = 1;

i = 0;

while i<=SAMPLES - 1:

    U = -w*sin(theta)
    #U = -w*theta
    eul = p + h*U
    eul2 = theta + h*p
    
    p = eul;
    t = t + h;
    theta = eul2;
    
    time[i]=t;
    theti[i]=eul2;
    pi[i]=eul;
    
    i+=1
    
#plt.title("displacement vs time")
#plt.plot(time,theti, 'r')
#plt.show()
#plt.title("derivative vs time")
#plt.plot(time,pi, 'b')
plt.title("phase plot")
plt.plot(theti,pi, 'orange')
plt.show()

