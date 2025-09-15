
# TYPE CASTING IN PYTHON :-

# The conversion of one data type into the other data type is known as type casting in python or type conversion 
# in python.

a = "2"
b = "2"
print(a+b)  # The output will be 22 bcz python take things in the "  " are string.

a = "4"
b = "4"
print(int(a) + int(b))
# Now the output will be 8 bcz we convert string into int with the type casting method.

string = "15"
number = 7
string_number = int(string)
sum = string_number + number
print(f"The sum is {sum}")



# IMPLICIT TYPE CASTING :-

# In the implicip type casting the python automatically convert one data type into another data type.
a = 1.8
b = 8
print(a+b)  
# Here b automatically convert into float datatype.