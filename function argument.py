
# Function argument in python :-

# FUNCTION WITH ARGUMENT :-

# A function can accept some value it can work with. We can put these values in the parantheses.

# In the below program, name and ending are the argument we pass in the function goodDay.

def goodDay(name,ending):
    print("Good Day..:) ",name)
    print(ending)

goodDay("Janvi","Thank you")
goodDay("Jimin","Thank you")
goodDay("Jin","World Wide Handsome")


# Entered value by the user in User defined functions.

def average(a, b):
    print(f"The average of the numbers is {(a+b)/2}")


a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
print(f"The number is {a}")
print(f"The number is {b}")
average(a,b)

# Average with tuple :-

# def average(*numbers):
#     print(type(numbers))
#     sum = 0
#     for i in numbers:
#         sum = sum + i
#         print(f"The average is {sum/len(numbers)}")

# average(10,30,40,40)


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
        return sum/len(numbers)
c = average(11,12,13)
# print(c)


