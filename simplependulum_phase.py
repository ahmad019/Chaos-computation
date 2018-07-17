# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:09:12 2018

@author: ahmad
"""
import numpy as np
import matplotlib.pyplot as plt

steps=8
density=1000

SAMPLES=density*steps #we need 10000 samples persecond so 
    

time = np.ndarray(SAMPLES, float) #array for time steps
theti = np.ndarray(SAMPLES, float)   #for 0 values
pi = np.ndarray(SAMPLES, float)     #for 0' (derivative)



p0 = 0;
theta0 = np.pi / 4;
h0 = 0.001;
t0 = 0
w = 1

U = -w*np.sin(theta0)

def U(theta):
    return -w**2 * theta

def Usin(theta):
    return -w**2 * np.sin(theta)


def euler(p,theta,h,t,c,u):
    i = 0;
    
    while i<=SAMPLES - 1:
        
        eul = p + h* u(theta)
        eul2 = theta + h*p
        
        p = eul;
        t = t + h;
        theta = eul2;
        
        time[i]=t;
        theti[i]=eul2;
        pi[i]=eul;
        
        i+=1
        
    plt.plot(theti,pi,color=c) #phase plot
    
    #plt.plot(time,theti, color=c)
   # plt.show()
    #plt.plot(time,pi, color=c)
    

#euler(p0,theta0,h0,t0,'b', Usin)
euler(p0,theta0,h0,t0,'m', U)

