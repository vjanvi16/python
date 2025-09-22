
# Inheritance :-

# Inheritance is a way of creating a new class from an existing class.

# Example :

class employee:
    pass
class programmers(employee):
    pass

# We can use the methods and attributes of "employee" in "programmers".
# We can overwrite or add new attributes and methos in "programmers".

# TYPE OF INHERITANCE :-

#  1. SINGLE INHERITANCE 
#  2. MULTIPLE INHERITANCE
#  3. MULTILEVEL INHERITANCE
#  4. HIERARCHICAL INHERITANCE
#  5. HYBRID INHERITANCE

class employee:
    def __init__(self,nm,i):
        self.name = nm
        self.id = i
    
    def showDetails(self):
        print(f"The name of employee number {self.id} is {self.name}.")

class programmer(employee):
    def showLanguage(self):
        print("The default language is python.")

e1 = employee("Harry",46)
e1.showDetails()
e2 = employee("Perry",278)
e2.showDetails()
e3 = programmer("Jerry",127)
e3.showDetails()
e3.showLanguage()
