
# Exception Handling in python :-

# For example if the for loop has an error in this program.
# so we need to use exception handling in our program.

a = int(input("Enter the number : "))
print(f"Multiplication table of {a} is ")

try:
    for i in range(1,11):
        print(f"{a} * {i} = {a*i}")
except Exception as e:
    print(e)


print("Some imp line of code")
print("End of program")

# We can also use Exception Handling like this in above program:
# try:
#     for i in range(1,11):
#         print(f"{int(a)} * {i} = {int(a*i)}")
# except:
#     print("Invalid Input!")

# Example 2 :

# ValueError :-
try :
    num = int(input("Enter the number : "))
except ValueError:
    print("The number you entered is not integer.")

# IndexError :-

i = int(input("Enter the number : "))
a =[2,4,6,16,11,64,24,55,675,]
try:
    if i in a:
        print("Yes, this number in the list.")
except IndexError:
    print("Index Error!")


