
# DECORATOR :-

# A Decorator is a function that takes another function as an argument and return new function that modifies the
# behaviar of the original function.

# Syntax :-

#  @decorator_function
#  def my_function():
#       pass

def greet(fx):
    def mfx():
        print("Good morning")
        fx()
        print("Thanks for using this function")
        return mfx

@greet
def hello():
    print("Hello world!")

@greet
def add(a,b):
    print(a+b)

hello()
add(2,4)

