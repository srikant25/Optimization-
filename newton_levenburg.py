# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 07:22:19 2018

@author: srikant nayak
"""

import sympy as sym

def get_values(x,keys):
    x =x.tolist()
    x = [val for sublist in x for val in sublist]
    values =dict(zip(keys,x))
    return values
alpha= sym.Symbol('a')
expr=  sym.sympify('(x1+10*x2)**2 + 5*(x3-x4)**2 + (x2- 2*x3)**4 +10*(x1-x4)**4')
values= {'x1':3,'x2':-1,'x3':0,'x4':1 } 
#expr=  sym.sympify('-1*exp(-x**2 - y**2)')  
var_list =list(expr.free_symbols)    
grad =sym.Matrix([sym.diff(expr, i) for i in var_list]) 
hess = sym.hessian(expr,list(expr.free_symbols))
#values= {'x':.1,'y':.1}
x = sym.Matrix(var_list)
alpha = 1e-4
mu = 1e-2
eps=1e-5
hess_inv = hess.inv()
iteration=0
while(1):
    iteration=iteration+1
    if len(list(expr.free_symbols)) == 1:
            muI= mu*sym.eye(hess_inv.shape[0])
            x_new = (x- alpha*(muI+sym.Matrix([hess_inv.dot(grad)]))).subs(values).evalf() 
    else:
        x_new = (x- sym.Matrix(hess_inv.dot(grad))).subs(values).evalf()
    diff = x_new -x.subs(values).evalf()
    error = diff.norm()
    
    values= get_values(x_new,values.keys())
    x=x_new
    if(error<eps):
        break
    if(iteration==3):
        break
print(values)
    