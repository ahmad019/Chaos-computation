# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:09:12 2018

@author: ahmad
"""
import numpy as np
import matplotlib.pyplot as plt

cycles=100
density=10000
h0 = 1/density; #step size


SAMPLES=density*cycles #we need 10000 samples persecond so 
    

time = np.ndarray(SAMPLES, float) #array for time steps
theti = np.ndarray(SAMPLES, float)   #for 0 values
di = np.ndarray(SAMPLES, float)     #for 0' (derivative)



d0 = 0; #derivative
theta0 = np.pi / 4; #initial displacement
t0 = 0
w = 1

U = -w*np.sin(theta0)

def U(theta):
    return -w**2 * theta

def Usin(theta):
    return -w**2 * np.sin(theta)


def euler(d,theta,h,t,c,u):
    i = 0;
    #plt.axis([-1, 1, -1, 1])
    while i<=SAMPLES - 1:
        
        eul = d + h* u(theta)
        eul2 = theta + h*eul
        euli = d + h/2*( u(theta)+u(eul2)) 
        eul2i = theta + h/2*(euli+eul2)
        
        d = euli;
        t = t + h;
        theta = eul2i;
        
        time[i]=t;
        theti[i]=eul2i;
        di[i]=euli;
        
        i+=1
        #plt.scatter(time,theti, color=c)
        #plt.pause(0.001)
        
    plt.plot(theti,di,color=c) #phase plot
    plt.show()
    
   # plt.plot(time,theti, color=c)
    #plt.show()
    #plt.plot(time,di, color=c)
    

#euler(p0,theta0,h0,t0,'b', Usin)
euler(d0,theta0,h0,t0,'m', U)

