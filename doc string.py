
# Docstring in python :-

# python docstring are the string literals that appears right after the defination of a function,
# method, class or module.
# '''  ''' This is not comment  

def square(n):
    '''Takes in a number n, returns the square of n '''
    print(n*n)
    

n = int(input("Enter the number : "))
print(f"The number is {n}")
square(n)
print(square.__doc__)


#  PEP 8 :-

# Go to cmd and write python after this write a command import this.