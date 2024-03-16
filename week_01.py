# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 17:15:15 2024

@author: gianluca
"""

# In[]

x = 20 # assignment, x is a variable

g = x/3

print('the type of x is', type(x), 'the type of g is ', type(g))


while abs(g*g - x) > 0.00001 :
    g = 0.5*(g + x/g)
    print(g)


# In[]

n = 16

finish = False

while not finish:
    if n == 0 or n == 1:
        print(n)
        finish = True
    else:
        b = n%2
        print(b)
        n = n//2
        
