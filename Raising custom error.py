
# Raising  Custom Error :-

# In short u can create your own error. 

a = int(input("Enter any value between 1 to 10 : "))

if(a<1 or a>11 ):
    raise ValueError("Invalid Value!")

print(f"Valid Input {a}")