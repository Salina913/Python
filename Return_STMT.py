# -*- coding: utf-8 -*-
"""
IN python as it can allow to take multiple values as input it also returns multiple values
in the form of tuple and we can also unpack the tuple as shown in below program
"""

def fun():
    a=10
    b=20
    c=30
    return a,b,c

print(fun())
res=fun()
print(res)
#unpacking tuple

res1, res2, res3 = fun()
print(res1)
print(res2)
print(res3)