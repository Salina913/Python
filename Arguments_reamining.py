# -*- coding: utf-8 -*-
"""
TYpes of Arguments
"""

# Keyword Arguments

def power_of(a, b):
    c=a**b
    print(c)

power_of(5,6)

#if we interchange the value it shoudnot change its posiion so for that do it like that
power_of(a=5, b=6)
power_of(b=6, a=5)


# Variable length Arguments(Arbitrary Arguments)

def pizza_toppings(*toppings):
    print(toppings)
    print(type(toppings))
    
pizza_toppings("cheese")
pizza_toppings("Cheese", "Onions", "Olives", "Corn")


# if we give just toppings as parameters we can only send 1 arguments but instaed of that if we give * before the parameters then we can pass n numbers of arguments

def pizza_toppings(name,*toppings, crust):
    print(name)
    print(toppings)
    print(crust)
    
pizza_toppings("Salina","cheese", "corn","onion","corn", crust="thin")

# after variable length arguments we have to must provide next arguments as keyword argument


# Vaiable length keyword arguments

def collect_student_data(**data):
    print(data)
collect_student_data(Name="Rohit", Age= 28, Avg=60.5, Gender='M')

# if we put "**" then python consider that parameter as variable length keyword arguments
# after the varibale length argument it must be an keyword arguments
