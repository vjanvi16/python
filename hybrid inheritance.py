
#   4. HIERARCHICAL INHERITANCE :-

# Syntax :-

class BaseClass:                    # |
    pass                            # |--- Single Inheritance
class Derived1(BaseClass):          # |
    pass                           
class Derived2(BaseClass):          # |
    pass                            # |____ Mutliple Inheritance
class Derived3(Derived1,Derived2):  # |
    pass                            # |


