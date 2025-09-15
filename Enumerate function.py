
# Enumerate Function in python :-

# If you want to print string inside the list in specific index number this function is use in python.

marks = [23,44,67,72,49,91,16,82,56]
for index,mark in enumerate(marks):
    print(mark)
    if(index==6):
        print("Harry, very bad!")

