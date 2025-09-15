
# CONDITIONAL OPERATORS :-

#  >, <, >=, <=, ==, !=

# IF ELSE STATEMENT :-

#  1. if
#  2. if-else
#  3. if-elif-else
#  4. nested if-else-elif


#  2. If-else statement :

# a = int(input("Enter your age : "))
# print(f"Your age is {a}")
# if(a>=18):
#     print("You can drive.")
# else:
#     print("You can't drive.")


#  3. if-elif-else statement :

# num = int(input("Enter the number : "))
# if(num>0):
#     print("The number is positive")
# elif(num<0):
#     print("The number is negative")
# else:
#     print("The number is zero")


#  4. nested if-else-elif statement :

nm = int(input("Enter the number : "))
if(nm<0):
    print("The number is negative")
elif(nm>0):
    if(nm<=100):
        print("Number is between 1 to 100")
    elif(nm>100 and nm<=999):
        print("Number is between 100 to 999")
    else:
        print("The number is more than 1000")
else:
    print("The number is zero")
    