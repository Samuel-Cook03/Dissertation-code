# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 14:06:00 2023

@author: Sam
"""

import matplotlib.pyplot as plt
import numpy as np 

w1s=[]
w2s=[]
ts=[]
Mu= 1061.03295394597
#Mu=1
R= 0.03
h= 0.5
c=100
a=1
def omega1(A,t,C,D):
    '''
    

    Parameters
    ----------
    A : float(alpha constant used in ODE)
    t : Float(time).
    C : float
    D : float

    Returns
    -------
    float(angular velocity in I1).

    '''
    return C*np.cos(A*t)+D*np.sin(A*t)
def omega2(A,t,E,F):
    '''
    

    Parameters
    ----------
    A : float(alpha constant used in ODE)
    t :  Float(time).
    E : float
    F : float

    Returns
    -------
    float(angular velocity in I2)

    '''
    return E*np.cos(A*t)+F*np.sin(A*t)
def gamma(c,I3):
   
    return c/I3
def alpha(I1,I2,I3,G):
    
    return (-(I3-I2)*G)/I1

I1=(3*(R**2)+(h**2))*(Mu/12)
I2=I1
I3=(Mu*(R**2))/2
#G=gamma(c,I3)
G=0
Au=alpha(I1,I2,I3,G)
C=1
D=1
E=5
F=5
#xold=-1.5
told=0
tend=100
w1old=0
w2old=0
w2s.append(w2old)
w1s.append(w1old)
ts.append(told)
j=0.001
#Nsteps=int(np.floor((tend)/h))

space=np.arange(0,10,0.1)
for a in space:
    
    w1new=omega1(Au,told,C,D)
    w1s.append(w1new)
    w2new=omega2(Au,told,E,F)
    w2s.append(w2new)
    tnew=told+0.1
    ts.append(tnew)
    told=tnew
    
#plt.plot(ts,w1s)
plt.plot(ts,w2s)


wx=np.pi
wv=np.pi
V,X=np.mgrid[-wv:wv:10j,-wx:wx:10j]
W=V
P=C*np.sin(Au*X)+D*np.sin(Au*X)
fig=plt.figure(3)
plt.streamplot(X, V, W, P);

plt.title("A phase diagram showing angular velocity about I1,I2 on a uniform cylinder")
plt.xlabel("angular velocity around x (s^-1)")
plt.ylabel("angular velocity around y (s^-1)")






























