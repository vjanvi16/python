
# Recursion :-

# In python, we know that a function can call other functions. It is even possible for the function to call itself.
# These type of construct are terned as recursive function.

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n * factorial(n-1))

n = int(input("Enter the number : "))
factorial(n)
print(f"The Factorial of {n} is : {factorial(n)}",)
    