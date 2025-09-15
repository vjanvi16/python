
#  While loop :-

#  As the name suggests, while loops execute statement while the condition is True. As soon as the condition
#  becomes False, the interpreter comes out of the while loop.

#  In while loop the condition is checked first. If it evaluates to true. the body of the loop is execued 
#  otherwise not!

#  If the loop is entered, the process of[condition check & execution] is continued untill the condition becomes 
#  false.

#  syntax -

#  while(condition):
#  Body of the loop

#  Note : 1. while loop keep executing untill the condition is true.
#         2. If the condition never become false, the loop keeps getting executed.

# Example 1 :-

# Increament in while loop
i = 1
while(i<=5):
    print(i)
    i=i+1


# Example 2 :-

# decreament in while loop
a = 5
while(a>0):
    print(a)
    a=a-1



# Nested loop with while :

i = int(input("Enter the number : "))
print(f"The number is {i}")
while(i<40):
    i = int(input("Enter the number : "))
    print(f"The number is {i}")
print("Done with the loop")