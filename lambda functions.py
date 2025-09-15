
# Lambda functions :-

#  lambda() function are often used in situation where a small function is required for short period of time.

# Syntax :

# lambda arguments : expression 

# def double(x):
#     return x*2      We can create function like this normally


double = lambda x : x*2      # With lembda we can create like this
cube = lambda a : a*a*a
avg = lambda y,z : (y+z)/2

print(double(5))
print(cube(4))
print(avg(16,12))
