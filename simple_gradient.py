# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 21:07:07 2018
Program : Steepest descent general form
@author: durgesh singh
"""
import sympy as sym
import time 
import numpy as np
import sys

sys.stdout = open('logfile.txt', 'w')






def init():  
    alph = sym.Symbol('a')
    expr = sym.sympify(str(input('Input cost function\n')))
    var_list =list(expr.free_symbols)
    sgrad = sym.Matrix([sym.diff(expr, i) for i in var_list])
    shess =sym.hessian(expr,list(expr.free_symbols)) 
    values={}
    for var in var_list:
        values[var]=float(input('Provide initial value of variable {} :'.format(var)))
    x = sym.Matrix(var_list)
    return [x,alph,expr,sgrad,shess,values]

def get_values(x,keys):
    x =x.tolist()
    x = [val for sublist in x for val in sublist]
    values =dict(zip(keys,x))
    return values

def newton_one_var(alpha_expr,alpha,values):
    print('Starting newton ')
    der = sym.diff(alpha_expr,alpha)
    der_der =sym.diff(der,alpha)
    error=1e2
    err_tol = 1e-5
    steps =0

    while error>err_tol and steps<500:        
        alpha_new = (alpha - der/der_der).subs(values).evalf()
        print('Value of alpha is {}'.format(alpha_new))
        error = alpha_new -alpha.subs(values).evalf()
        values= {alpha:alpha_new}
        alpha=alpha_new
        steps+=1
        
    return alpha  
    

def bisection_one_var(alpha_expr,alph): 
    a=0
    b=0
    der = sym.diff(alpha_expr,alph)
    
    print('starting bisecion one variable')
    while(1):    
        a = np.random.uniform(low=-10,high = 10)
        b = np.random.uniform(low=-10,high = 10)
        if der.subs({alph:a}).evalf()*der.subs({alph:b}).evalf() < 0:
            break
        else:
            print('finding a and b')
            print('a ={} and b = {}'.format(a,b))
        
    
    print('value of derivative for a = {} is {}'.format(a,der.subs({alph:a}).evalf()))
    print('value of derivative for b = {} is {}'.format(b,der.subs({alph:b}).evalf()))
     
    while(1): 
        mid = (a+b)/2
        print(type(der.subs({alph:mid}).evalf()))
        if der.subs({alph:mid}).evalf() <= 1e-2:
            print(' ending bisection one variable final value of derivative is {} at alpha = {}'.format(der.subs({alph:mid}).evalf(),mid))
            return mid
        elif der.subs({alph:a}).evalf()*der.subs({alph:mid}).evalf() <0:
            b=mid
        elif der.subs({alph:b}).evalf()*der.subs({alph:mid}).evalf() <0:
            a=mid 
    print('ending bisection one variable value of alpha is {}'.format(mid))
        
    return mid
        
    
            
         
    
    
    
    
def get_alpha(x,sgrad,values):  
    alpha_fun = expr.subs(get_values((x - alph*sgrad).subs(values),values.keys()))
    return(bisection_one_var(alpha_fun,alph))
    
x,alph,expr,sgrad,shess,values = init()
error=1e2
err_tol = 1e-5
steps =0
alpha = 1e-5 #Taking general alpha

while error > err_tol and steps <= 200:
    
    alpha= get_alpha(x,sgrad,values)
    x_new = (x- alpha*sgrad).subs(values).evalf()
    diff = x_new -x.subs(values)
    error = diff.norm()
    print(error)
    values = get_values(x_new,values.keys())
    x=x_new
    steps+=1

end = time.time()    
print('Value of X vector is {}'.format(get_values(x,values.keys())))
#print('time taken for algorithm is {}'.format(end-start))
print('Algorithm took {} steps'.format(steps-1))
#x**3+exp(y**2-z**2+3)

#x**3-exp(y**2-x*2)
#(x-4)**4 + (y-3)**2 +4*(z+5)**4
#{'x':4,'y':2,'z':-1}






