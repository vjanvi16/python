
# Generators in python :-

# Generators in python are special type of functions that allows you to create an iterable sequence of values.

# Creating generator :-

# In python, you can create a generator by using the yield statement.
# The yield statement returns a value from the generator and suspends the execution of the function until the 
# next value is requested.

def my_generator():
    for i in range(10):
        yield i

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


for j in gen:
    print(j)