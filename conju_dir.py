# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 06:46:19 2018

@author: srikant nayak
"""

import numpy as np
import sys
Q=np.array([[4,2],[2,2]])

b = np.array([-1,1])
w=np.eye(Q.shape[0])
d = np.zeros(Q.shape)
d[:,0] = w[:,0]
for k in range(1,w.shape[1]):
    a=0
    for l in range(k):
        a+=(w[:,k].T.dot(Q).dot(d[:,l])/d[:,l].T.dot(Q).dot(d[:,l]))*d[:,l]
    d[:,k]=w[:,k] -a
   

Q = (Q+Q.T)/2
x = np.random.rand(Q.shape[0])
eps = 1e-5
g=np.subtract(Q.dot(x),b)

g = Q.dot(x) - b
if (all(a == 0 for a in g)):
    print(x)
    sys.exit()
steps=0       
iteration=0
for k in range(d.shape[1]):
    iteration=iteration+1
    alpha = -g.T.dot(d[:,k])/(d[:,k].T.dot(Q).dot(d[:,k]))
    print(alpha)     
    x_new = x + alpha*d[:,k] 
    error = np.linalg.norm(x_new-x) 
    x= x_new
    steps+=1
    if(iteration==2):
        break
    
print(x)

