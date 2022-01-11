# -*- coding: utf-8 -*-
"""
Mutable datatype casting
"""

lst=[20,60,50,23,69]
print(lst)
print(type(lst))
print(id(lst))

lst.append(90)
print(lst)

lst1=[20, 60, 50, 23, 69, 90]
print(lst1)
print(id(lst1))

print(lst is lst1)