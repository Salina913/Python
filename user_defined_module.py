# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 16:54:36 2022

@author: OMC
"""

import mymodule as mm

dir(mm)
help(mm)
mm.add()
help(mm.power_of)
help(mm.get_quotient)

print(mm.power_of.__doc__)
print(mm.get_quotient.__doc__)

#__doc__ is called dunder doc

#we can access module description by help, dir , __doc__