
# OOPs :-

# Classes and Object :-

# CLASS :-

# A class is a blueprint for create object.

class person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 2000

a = person()
a.name = "Charry"
print(a.name)
print(a.occupation,a.networth)




class employee:
    name = "janvi"
    language = "python"
    salary = 80000

emp = employee()
print(emp.name,emp.language,emp.salary)


# OBJECT :-

# An object is an instanitiation of class. When class is defined, a template is defined.
# Memory is allocated only after object instantiation.

# Object of a given class can invoke the methods available to it.Without revealing the implementation details to
# user.

# In above program the emp is object and employee is it's class.


# MODELLING A PROBLEM IN OOPs :-

# We identify the following in our problems.
#  NOUN       -> Class      -> employee
#  Adjectives -> Attributes -> name, language, salary
#  Werbs      -> Methods    -> getsalary(), increament()

# Here above program name, salary and language are class attributes as they directly belongs to the class.


# OBJECT/INSTANCE ATTRIBUTES :-

# The attribute of object calls object attribute or instance attributes.

# In the below program the name is instance attribute

class employee:
    language = "python"   
    salary = 400000

emp = employee()
emp.name = "Harry"   # This is an instance attribute.
print(emp.name, emp.language,emp.salary)

emp = employee()
emp.name = "Rajjo"   # This is an instance attribute.
print(emp.name, emp.language,emp.salary)

