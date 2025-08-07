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


