# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 07:02:29 2018

@author: srikant nayak
"""

import sympy as sym

def get_values(x,keys):
    x =x.tolist()
    x = [val for sublist in x for val in sublist]
    values =dict(zip(keys,x))
    return values
alph = sym.Symbol('a') 
expr=  sym.sympify('-1*exp(-x**2 - y**2)')  #expression ..............
  
var_list =list(expr.free_symbols)    
grad =sym.Matrix([sym.diff(expr, i) for i in var_list]) 
hess = sym.hessian(expr,list(expr.free_symbols))
values= {'x':.1,'y':.1}  #initial value...................
x = sym.Matrix(var_list)
eps=1e-5
hess_inv = hess.inv()
while(1):
    if len(list(expr.free_symbols)) == 1:
            x_new = (x- sym.Matrix([hess_inv.dot(grad)])).subs(values).evalf() 
    else:
        x_new = (x- sym.Matrix(hess_inv.dot(grad))).subs(values).evalf()
    #print(x_new)
    diff = x_new -x.subs(values).evalf()
    error = diff.norm()
    values= get_values(x_new,values.keys())
    x=x_new
    if(error<eps):
        break
print(values)
    