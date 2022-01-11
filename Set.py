# -*- coding: utf-8 -*-
"""
Example for Set
"""

"""
Set didnot follow the order we have created so it is "Unordered" in nature. 
In this there is no index value for the data.

Set is a unique collection of data. if we try to save a copy of duplicate value it wont allow you to do that.
instead of that only first or original copy of that element is stored inside that set

"Set is a unique collection of unordered dat""
"""
s1={10,29.3,"Yhtu","Salina",False}
print(s1)
#print(type(s1))
#print(s1[3])
s1.add(200)
s1.remove("Yhtu")
s1.add(200)
print(s1)
