# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 15:09:12 2018

@author: ahmad
"""
import numpy as np
import matplotlib.pyplot as plt

cycles=10
density=100
h0 = 1.0/density; #step size


SAMPLES=density*cycles #we need 10000 samples persecond so 
    

time = np.ndarray(SAMPLES, float) #array for time steps
theti = np.ndarray(SAMPLES, float)   #for 0 values
di = np.ndarray(SAMPLES, float)     #for 0' (derivative)



d0 = 4; #derivative
theta0 = np.pi / 8; #initial displacement
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
        
        d_n = d + h* u(theta)
        theta_n = theta + h*d_n
        d_ni = d + h/2*( u(theta)+u(theta_n)) 
        theta_ni = theta + h/2*(d_ni+d_n)
        
        d = d_ni;
        t = t + h;
        theta = theta_ni;
        
        time[i]=t;
        theti[i]=theta_ni;
        di[i]=d_ni;
        
        i+=1
        #plt.scatter(time,theti, color=c)
        #plt.pause(0.001)
        
    plt.plot(theti,di,color=c)#phase plot
    plt.title('phase plot')
    plt.show()
    
    plt.plot(time,theti, color=c)
    plt.title('Time series of displacement')
    plt.show()

    
    plt.plot(time,di, color=c)
    plt.title('Time series of derivatives')
    plt.show()

euler(d0,theta0,h0,t0,'b', Usin)
#euler(d0,theta0,h0,t0,'m', U)

