# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 05:58:17 2018

@author: srikant nayak
"""

import numpy as np


Q=np.array([[4,2],[2,2]])

b = np.array([-1,1])
Q = (Q+Q.T)/2
x=np.random.rand(Q.shape[0])
g=np.subtract(Q.dot(x),b)
eps=.00001
iteration=0
while(1):
    iteration=iteration+1
    if(all(v == 0 for v in g)):
        print(x)
        break
    else:
        d=-g
    alpha = -g.T.dot(d)/(d.T.dot(Q).dot(d)) 
    print(alpha)
    x_new = x + alpha*d
    diff=x_new-x
    error = np.linalg.norm(diff)  #calculating error for convergence
    x= x_new
    
    
    g = Q.dot(x) - b  #calculatin of gradient for next step
    beta = g.T.dot(Q).dot(d)/d.T.dot(Q).dot(d) 
    d = -g + beta*d 
    if(error<eps):
        print('Value of X vector is {}'.format(x))
        break
    if(iteration==2):
        break
    
        

        
        
    
    