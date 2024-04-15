# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:36:20 2024

@author: Sam
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy.special as JAm

def const(g,m1,r1,m2,r2):
    return (g*(m1*r1-m2*r2))/(m1*r1**2+m2*r2**2)

m1=1
m2=0.5
r1=0.15
r2=0.35
c1=0.2
c2=0.1
g=9.81
t=1
constant=-(const(g,m1,r1,m2,r2))
#phi1=0.5*(np.pi-4*JAm.ellipj(0.5*np.sqrt((2*constant)+c1)*(t+c2)**2),(4*constant)/(2*constant+c1))
#phi2=0.5*(np.pi+4*JAm.ellipj(0.5*np.sqrt((2*constant+c1)*(t+c2)**2),(4*constant)/(2*constant+c1)))
arg1=(0.5*np.sqrt((2*constant+c1)*(t+c2)**2))*0.1
arg2=((4*constant)/(2*constant+c1))*0.1

ans=JAm.ellipj(arg1,arg2)
cnlist=[]
dnlist=[]
snlist=[]
idk=[]
tlist=[]
for t in range(100):
    arg1=(0.5*np.sqrt((2*constant+c1)*(t+c2)**2))*0.1
    arg2=((4*constant)/(2*constant+c1))*0.1

    ans=JAm.ellipj(arg1,arg2)
    snlist.append(0.5*(np.pi+4*ans[0]))
    cnlist.append(ans[1])
    dnlist.append(ans[2])
    idk.append(ans[3])
    tlist.append(t)
    

plt.plot(tlist,snlist)
plt.xlabel("time(t)")
plt.ylabel("phi as a function of t")
plt.title("a graph of phi against time")
#plt.plot(tlist,cnlist)
#plt.plot(tlist,dnlist)    
#plt.plot(tlist,idk)    
    
    
    
    
    
    
    
    
    
    