
# Super keyword :-

# The super keywoed() in python is used to refer to the parent class. It is especially useful when a class inherits 
# from multiple parent classes and you want to call a method from parent class.

class parentClass:
    def parent_method(self):
        print(f"This will print parent method.")

class childClass(parentClass):
    def child_method(self):
        print(f"This will print child class.")
        super().parent_method()
    
c = childClass()
c.child_method()
