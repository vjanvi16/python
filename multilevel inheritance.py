
#  3. MULTILEVEL INHERITANCE :-
#  Multilevel inheritance occurs when child class becomes a parent class for other child class.

#                           PARENT CLASS
#                                |
#                           CHILD CLASS 1
#                                |
#                           CHILD CLASS 2
# Syntax:-

class employee:
    pass
class programer(employee):
    pass
class manager(programer):
    pass

# Example :-

class employee:
    a = 1

class programer(employee):
    b = 2 

class manager(programer):
    c = 3

x = employee()
print(x.a)
y = programer()
print(y.b)
z = manager() 
print(z.c)



class Animal:
    def __init__(self,nm,spc):
        self.name = nm
        self.species = spc

    def show(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self,nm,br):
        Animal.__init__(self,nm,spc="Dog")
        self.breed = br

    def show(self):
        Animal.show(self)
        print(f"Breed : {self.breed}")

class Husky(Dog):
    def __init__(self, nm, clr):
        Dog.__init__(self,nm,br="Husky")
        self.color = clr

    def show(self):
        Dog.show(self)
        print(f"Fav Color : {self.color}")


a = Husky("Moris","Black")
a.show()
