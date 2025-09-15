
# Import in python :-

import math

print(math.floor(8.4369))
print(math.sqrt(64))


# From keyword :-

# If you want to import specific functions or variable from a module using the from keyword.

from math import sqrt,pi
a = math.sqrt(36)
b = math.pi*3
print(a)
print(b)


# The "as" keyword :-

import math as m
print(m.sqrt(81))


# dir function :-

import math
print(dir(math))  # It will print the List of the function in math


# Import from another file :-

from import2 import weclome,harry
weclome()
print(harry)