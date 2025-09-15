
#  Local vs Global variable :- 

#  Local variable :
#  A local variable is a variable that is defined within a function and is only accesible within that function.

#  Global variable :-
#  A global variable is a variable that is defined outside of function and is accesible from within any function 
#  in yolur code.

x = 6
print(x)

def hello():
    x = 4
    print(f"The local x is {x}")
    print("Hello Harry!")

hello()
print(f"The global x is {x}")


# The global Keyword :-

x = 10      # global variable
def func():
    global x      # It will change value of global variable x 
    x = 8
    y = 5    # local variable
    print(y)

func()
print(x)
# print(y)  It will print an error bcz y is local variable and not accesible outside of function.