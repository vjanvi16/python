
#  2. MULTIPLE INHERITANCE :-

# Multiple inheritance occurs when child class inherits from more than one parent classes.

#                           PARENT CLASS 1           PARENT CLASS 2
#                                |                          |
#                                |__________________________|
#                                              |
#                                        CHILD CLASS                                    
# Syntax :-

class employee:
    pass
class coder:
    pass 
class programmer(employee,coder):
    pass

# Exmaple:-

class employee :
    company = "IFC"
    name = "Harry"
    salary = 440000
    def show(self):
        print (f"The name of the employee is {self.name} and the campany is {self.company}" )

class coder:
    language = "python"
    def printlanguage(self):
        print(f"This is your language Out of the other languages : {self.language}")

class programmers(employee,coder):
    company = "IFC info"
    def showlanguag(self):
        print(f"The name of employee is {self.company} and the language is {self.language}")

e = employee()
p = programmers()
p.show()
p.printlanguage()
p.showlanguag()




class Employee:
    def __init__(self,nm):
        self.name = nm

class Dancer :
    def __init__(self,dnc):
        self.dance = dnc

class DanceEmployee(Employee,Dancer):
    def __init__(self,nm,dnc):
        self.name = nm
        self.dance = dnc

    def show(self):
        print(f"The name of employee is {self.name} and his dance style is {self.dance}")


a = DanceEmployee("Harry","Hip-Hop")
a.show()



# class Animal:
#     def __init__(self,nm,fclr):
#         self.name = nm
#         self.fur_color = fclr

# class Dog(Animal,Mammal):
#     def __init__(self,name,breeb,fur_color):

    