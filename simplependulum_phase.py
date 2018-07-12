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



p0 = 0;
theta0 = 10;
h0 = 0.001;
t0 = 0;
w = 1;

U = -w*np.sin(theta0)

def U(theta):
    return -w * theta

def Usin(theta):
    return -w * np.sin(theta)


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
        
    plt.plot(theti,pi,color=c)
    

euler(p0,theta0,h0,t0,'b', Usin)
euler(p0,theta0,h0,t0,'y', U)

