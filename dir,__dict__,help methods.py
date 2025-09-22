
# dir, __dict__ and help methods :-

# ḍir() method :-

# The dir() function returns a list of all the attributes and method(including dunder method) available for an object. 

a = [1,2,3,4]
print(a)
print(dir(a))


# __dict__ attribute :-

# The __dict__ attribute returns a dictionary representation of an object's attribute.

class person:
    def __init__(self,nm,a):
        self.name = nm
        self.age = a
        print(f"{self.name}")
        print(f"{self.age}")

p = person("Jennie",22)
print(p.__dict__)


# help() :-

# The help() function is used to get help documentation for an object.
# including a description of its attributes and method.

print(help(person))
