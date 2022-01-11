# -*- coding: utf-8 -*-
"""
Types of arguments:
    1. Positional Arguments
    2. Default Arguments
    3. Keyword Arguments
    4.Variable length arguments(Arbitrary)
    5. Variable length keyword arguments(Arbitrary keyword arguments)

"""


# Positional Arguments

def power_of(a, b):
    c = a**b
    print(c)
    
power_of(8,6)
power_of(2,5)
power_of(5,2)

#power_of(2) if we pass single argument it raise an error 
# using single "*" provide multiplication. where as "**" gives power of or raise to


# Default Arguments

def power_of1(f=0, g=0):
    h=f**g
    print(h)
    
power_of1(5)
power_of1()

# if we forgot to assign a value to b it takes 0 by default for b's position by assigning 0 to that argument
# after a default arguments we caanot use a nondefault arguments

def fun(a,c,b=1,d=2 ):
    print(a,b,c,d)
    
fun(2,5)