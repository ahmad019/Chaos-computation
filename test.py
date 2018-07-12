# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:09:12 2018

@author: ahmad
"""
import numpy as np
import matplotlib.pyplot as plt

SAMPLES=50000

time = np.ndarray(SAMPLES, float) #array for time steps
theti = np.ndarray(SAMPLES, float)   #for 0 values
pi = np.ndarray(SAMPLES, float)     #for 0' (derivative)



p = 0;
theta= 10;
h = 0.001;
t = 0;
w = 1;

U = -w*np.sin(theta)


def euler(x,y,z,a,u):
    i = 0;
    
    while i<=SAMPLES - 1:
        
        eul = x + z*u
        eul2 = y + z*x
        
        x = eul;
        a = a + z;
        y = eul2;
        
        time[i]=a;
        theti[i]=eul2;
        pi[i]=eul;
        
        i+=1
        
    plt.plot(time,pi,'y')
    

euler(p,theta,h,t,U)

