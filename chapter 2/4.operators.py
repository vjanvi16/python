
#  TYPES of OPERATORS IN PYTHON

#  1. Arithmetic Operators         +,-,*,/ etc
#  2. Assignment Operators         =,+=,-=,*=,/= etc
#  3. Comparison Operators         ==,>,>=,<,<=,!= etc    ~ Written value always boolean
#  4. Logical Operators            AND,OR,NOT 

#==================================================================================================================

# 1. Arithmetic Operators :-

a = 4                                                 
b = 4       
c = a + b    # the (+) is arithmetic operator
print(c)                                             

x = 5                                         
y = 2                                               
z = x * y    # the (*) is arithmetic operator                                          
print(z)

#=================================================================================================================

# 2. Assignment Operators

a = 4-2  # Assign 4-2 in a
print(a)

b = 6 
b *= 3  # Increment the value of b by 3 ,then assign it to b.
print(b)

#==================================================================================================================

#  3. Comparison Operators 

x = 5 < 4
print(x)

y = 8 >= 8
print(y)

z = 4 != 6
print(z)

#==================================================================================================================

#  4. Logical Operators

# AND = True when both are True
# OR = True if one are true
# NOT = if true than false, if false than return true

# Truth table of "OR" Logical operater
print("TRUTH TABLE")
print("True or True is ", True or True)
print("True or False is ", True or False)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of "AND" Logical operater
print("TRUTH TABLE")
print("True and True is ", True and True)
print("True and False is ", True and False)
print("False and True is ", False and True)
print("False and False is ", False and False)

# "AND" Logical operater
# It work as oposite like true ko false banade or false to true krde
print(not(True))
print(not(False))





