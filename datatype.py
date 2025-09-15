
#  DATA TYPES IN PYTHON

#  1. Integers   -   numbers like 1,2,3,4 are integer
#  2. Floating point numbers   -   numbers with (.) like 3.45,8.88,16.11 are floating point numbers
#  3. Strings   -   any world like "flower","fruit","elephant" are string
#  4. Booleans   -   True/False are boolean type of data type
#  5. None   -   If the variable has nothing value or empty type of variable are none variable   

#  EXAMPLE :-

a = 1 # a is an intiger

b = 5.22 # b is a floating point number

c = "Janvi" # c is a string

d = True # d is a boolean variable

e = None # e is a none type variable


#  Type() function :-

#  Tpye () function is used to find the data type of a given variable in python.
#  1. int is a function
#  1. float is a function
#  1. string is also a function

a = 16
t = type(a)
print(t)
# output : class <int>    bcz 16 is an integer type of datatype.

b = 16.11
t = type(b)
print(t)
# output : class <float>    bcz 16.11 is a floating point number.

c = "elephant"
t = type(c)
print(t)
# output : class <str>    bcz elephant is a string type of datatype.

b = "16.11"
t = type(b)
print(t)
# output : class <str>    bcz 16.11 is in "   ".


# We can convert into any datatype if the conversion is "VALID".
# NOW we create a string into float bcz float is a functinon


a = "16.11"
b = float(a)
t = type(b)
print(t)

a = "88.88"
b = int(a)
t = type(b)
print(t)


