# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 02:27:00 2018

@author: srikant nayak
"""

import numpy as np
import random


Q = np.array([
        [3,0,1],
        [0,4,2],
        [1,2,3]])
b = np.array([1,2,3])
Q = (Q+Q.T)/2
x=np.random.rand(Q.shape[0])
H = np.eye(Q.shape[0])

eps=.00001
eig_q = max(np.linalg.eig(Q)[0])
alpha = random.uniform(0,2/eig_q)
while(1):
    g=np.subtract(Q.dot(x),b)#derivative of the function
    if(all(a == 0 for a in g)):
        print(x)
        break
    else:
        d=-H.dot(g)
    alpha = -g.T.dot(d)/(d.T.dot(Q).dot(d))    
    x_new = x + alpha*d
    error = np.linalg.norm(x_new-x)
    dx = alpha*d
    g_1= Q.dot(x_new) - b
    dg = g_1 - g
    H += np.outer(dx,dx.T)/dx.T.dot(dg) - np.outer(H.dot(dg),H.dot(dg).T)/dg.T.dot(H).dot(dg) 
    x= x_new
    g = g_1
   
    if(error<eps):
        print('Value of X vector is {}'.format(x))
        break
