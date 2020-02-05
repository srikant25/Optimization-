# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 02:23:35 2018

@author: srikant nayak
"""

import numpy as np
import random


Q=np.array([[4,2],[2,2]])
b = np.array([-1,1])
Q = (Q+Q.T)/2
x=np.random.rand(Q.shape[0])

eps=.00001
eig_q = max(np.linalg.eig(Q)[0])
alpha = random.uniform(0,2/eig_q)
while(1):
    g=np.subtract(Q.dot(x),b)#
    if(all(v == 0 for v in g)):
        print(x)
        break
    alpha = g.T.dot(g)/(g.T.dot(Q).dot(g))
    x_new = x - alpha*g
    diff=x_new-x
    error = np.linalg.norm(diff)
    x= x_new
    if(error<eps):
        print('Value of X vector is {}'.format(x))
        break