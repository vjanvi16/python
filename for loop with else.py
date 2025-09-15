
# For loop with else :-

for i in range(1,5):
    print(i)
    
else :
    print("There is no i.")


# While loop with else :-

i=1
while(i<6):
    print(i)
    i = i+1

else:
    print("There is no i")


# with break statement :-
 
for i in range(1,5):
    print(i)
    if(i==4):
        break   # Here break statement break the loop so else part will not excetute.
    
else :
    print("There is no i.")


i=1
while(i<6):
    print(i)
    i = i+1
    if(i==4):
        break   # Here break statement break the loop so else part will not excetute.

else:
    print("There is no i")

# Example :-

for a in range(5):
    print(f"ilteration no {a+1} in for loop.")
else:
    print("Else block in loop.")
print("Out of the loop.")