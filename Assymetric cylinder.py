# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:48:11 2023

@author: scook11
"""

import matplotlib.pyplot as plt
import numpy as np 
import sympy as sy

def f(O1):
    return O1
def g(O2):
    return O2
z = sy.Symbol("z")
w1s=[]
w2s=[]
ts=[]
R= 0.03
h= 0.5
k=1/2
c=1.5
a=1
O1=1.5/(np.pi*(k*h)*R**2)
O2=2.5/(np.pi*(k*h)*R**2)
M= sy.integrate(f(O1), (z, 0, k*h))+sy.integrate(f(O2),(z,k*h,h))#not correct bounds check idiot
dh=(h/2)*(((k**2)*O1+(1-k**2)*O2))/(k*O1+(1-k)*O2)
I1=(O1*np.pi*(R**2)*(((k*h)**3)/3-dh*((k*h)**2)+(dh**2)*k*h+((R**2)*k*h)/4)+O2*np.pi*(R**2)*((((k*h)**3)/3)-dh*((k*h**2))+(dh**2)*k*h+(R**2)*k*h/4))
I2=I1
I3=(np.pi*h*(R**4))/2*(O1*k+(1-k)*O2)
def I1calc(O1,R,k,h,dh,O2):
    return (O1*np.pi*(R**2)*(((k*h)**3)/3-dh*((k*h)**2)+(dh**2)*k*h+((R**2)*k*h)/4)+O2*np.pi*(R**2)*((((k*h)**3)/3)-dh*((k*h**2))+(dh**2)*k*h+(R**2)*k*h/4))
def I3calc(h,R,k,O1,O2):
    return (np.pi*h*(R**4))/2*(O1*k+(1-k)*O2)
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
G=0
#G=gamma(c,I3)
A=alpha(I1,I2,I3,G)

#A=0
C=1
D=1
E=1
F=1
#xold=-1.5
told=0
#tend=10
w1old=5
w2old=5
w2s.append(w2old)
w1s.append(w1old)
ts.append(told)
j=0.001
#Nsteps=int(np.floor((tend)/j))

space=np.arange(0,2,0.125)
for p in space:
    
    w1new=omega1(A,told,C,D)
    w1s.append(w1new)
    w2new=omega2(A,told,E,F)
    w2s.append(w2new)
    tnew=told+0.125
    ts.append(tnew)
    told=tnew
    
plt.plot(ts,w1s)
plt.title("rotation around omega1 where gamma=0 and alpha=0")
plt.xlabel("time (s)")
plt.ylabel("omega 1(s^-1)")
#plt.plot(ts,w2s)

wx=np.pi
wv=np.pi
V,X=np.mgrid[-wv:wv:10j,-wx:wx:10j]
W=V
P=C*np.sin(A*X)+D*np.sin(A*X)
fig=plt.figure(3)
plt.streamplot(X, V, W, P);
plt.xlabel("omega_1 (angular speed)")
plt.ylabel("omega_2 (angular speed)")
plt.title("A phase diagram of angular speed of an asymmetric cylinder")
AaV=[]
kvv=[]
kvspace=np.arange(0.1,1.1,0.0001)
for kv in kvspace:
    I1v=I1calc(O1,R,kv,h,dh,O2)
    I2v=I1calc(O1,R,kv,h,dh,O2)
    I3v=I3calc(h,R,kv,O1,O2)
    Gv=gamma(c, I3v)
    Av=alpha(I1v, I2v, I3v, Gv)
    AaV.append(Av)
    kvv.append(kv)
fig=plt.figure(4)    
plt.plot(kvv,AaV)
plt.xlabel("")
