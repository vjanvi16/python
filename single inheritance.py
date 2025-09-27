
#  1. SINGLE INHERITANCE :-

# Single inheritance is type of inheritance where class inherits properties and behave from a single parent class.
# This is the simplest and most common from of inheritance.

#  1. SINGLE INHERITANCE :-

# Single inheritance occurs when child class inherits only single parent class.

#                           BASE CLASS
#                                |
#                          DERIVED CLASS
# Exmaple:-
class employee :
    company = "IFC"
    def show(self):
        print (f"The name of the employee is {self.name} and the salary is {self.salary}" )

class programmers(employee):
    company = "IFC info"
    def showlanguag(self):
        print(f"The name of employee is {self.name} and the language is {self.language}")

e = employee()
p = programmers()
print(e.company)
print(p.company)




class animal:
    def __init__(self,nm,sp):
        self.name = nm
        self.species = sp

    def make_sound(self):
        print("Sonud made by the animal")

class dog(animal):
    def __init__(self, name, b):
        animal.__init__(self,name,sp="dog") 
        self.breed = b

    def make_sound(self):
        print("Bark!")

d = dog("dog","Husky")
d.make_sound()

a = animal("dog","dog")
a.make_sound()        


    