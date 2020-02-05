# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 18:42:34 2018

@author: srikant nayak
"""

import sympy as sym
import sys
def get_values(x,keys):
    x =x.tolist()
    x = [val for sublist in x for val in sublist]
    values =dict(zip(keys,x))
    return values

sys.stdout = open('logfile.txt', 'w')
alph = sym.Symbol('a')
expr=  sym.sympify('(x-4)**4 + (y-3)**2 +4*(z+5)**4') 
#expr = sym.sympify(str(input('Input cost function\n')))
var_list =list(expr.free_symbols)
sgrad = sym.Matrix([sym.diff(expr, i) for i in var_list])
#shess =sym.hessian(expr,list(expr.free_symbols)) 
values= {'x':4,'y':2,'z':-1}
x = sym.Matrix(var_list)
alpha=.0001
eps=.00001
iteration=0
while(1):
    iteration=iteration+1
    x_new = (x- alpha*sgrad).subs(values).evalf()
    diff = x_new -x.subs(values)
    error = diff.norm()
    print(error)
    values = get_values(x_new,values.keys())
    x=x_new
    if(error<eps):
        break
    if(iteration==200):
        break
print(values)    
#print('Value of X vector is {}'.format(get_values(x,values.keys())))