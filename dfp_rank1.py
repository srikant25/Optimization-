# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 02:46:33 2018

@author: srikant nayak
"""

import numpy as np
import random


Q = np.array([[2,0],[0,1]])
b = np.array([0,0])
Q = (Q+Q.T)/2
#x=np.array([1,2])
x=np.random.rand(Q.shape[0])
H = np.eye(Q.shape[0])

eps=.00001
eig_q = max(np.linalg.eig(Q)[0])
alpha = random.uniform(0,2/eig_q)
while(1):
    g=np.subtract(Q.dot(x),b)#derivative of the function
    if(all(v == 0 for v in g)):
        print(x)
        break
    else:
        di=-H.dot(g)
    alpha = -g.T.dot(di)/(di.T.dot(Q).dot(di))    
    x_nxt = x + alpha*di
    error = np.linalg.norm(x_nxt-x)
    del_x = alpha*di
    g_1= Q.dot(x_nxt) - b
    dg = g_1 - g
    Hdelg = del_x -H.dot(dg)
    gta = dg.T.dot(Hdelg)
    out = np.outer(Hdelg,Hdelg.T)
    H = H + out/gta
    x= x_nxt
    g = g_1
    if(error<eps):
        print('Value of X vector is {}'.format(x))
        break