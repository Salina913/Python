# -*- coding: utf-8 -*-

"""
Examples for list
"""

"""
It is a ordered and  sequential collection of data and a combination of homegenious and 
heterogenious data
Inside list we can store heterogenious type of data.And in that each elements
have a positional value both positive and negetive
**List is  a mutable**

"""

lst=[23,56,89,56,75]
print(lst)
print(type(lst))


lst1=[26,52.5,68,69.3,3+6j, "Python", True]
print(lst1)
print(type(lst1))
print(lst1[2])
print(lst1[4])
print(lst1[-4])

"""
Adding element at the end of list
"""

lst.append(200)
print(lst)

"""
Remove element from the list
"""
lst.remove(200)
print(lst)

