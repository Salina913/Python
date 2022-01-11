# -*- coding: utf-8 -*-
"""
Example for Dictionary
Its a collection key value pair of elements
"""

dict={ "Dennis Ritchie": "C",
      "James Gosling": "Java",
      "Guido van rossum": "Python"}
print(dict)
print(type(dict))

# Adding and removing an elements in Dictionary
dict["Brendan Eich"]="Javascript"

dict.pop("Brendan Eich")
print(dict)