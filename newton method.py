# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:36:14 2018

@author: srikant nayak
"""

import sympy as sym

def get_values(x,keys):
    x =x.tolist()
    x = [val for sublist in x for val in sublist]
    values =dict(zip(keys,x))
    return values
alpha = sym.Symbol('a')
expression=  sym.sympify('(x1+10*x2)**2 + 5*(x3-x4)**2 + (x2- 2*x3)**4 +10*(x1-x4)**4')
values= {'x1':3,'x2':-1,'x3':0,'x4':1 }
var_list =list(expression.free_symbols)  
grad=sym.Matrix([sym.diff(expression, i) for i in var_list])
hess=sym.hessian(expression,list(expression.free_symbols))
x = sym.Matrix(var_list)
eps=1e-5
hess_inv = hess.inv()
iteration=0
while(1):
    iteration=iteration+1
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