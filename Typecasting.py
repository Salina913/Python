# -*- coding: utf-8 -*-
"""
Typecasting Examples
"""

#INteger to floating point typecatsing using float()

a=99
print(type(a))
print(a)
B=float(a)
print(B)
print(type(B))


# Floating point to Integer conversion using int()

n=10.23
print(n)
C=int(n)
print(C)
print(type(C))

# Coverting floating point to complex using complex()

a=99.9
print(a)
print(type(a))
b=complex(a)
print(type(b))
print(b)
#wewant to tell the imaginary part by doing this

c=complex(a,4)
print(c)

# integer to string conversion using str()

y=69
print(y)
print(type(y))
x=str(y)
print(x)
print(type(x))