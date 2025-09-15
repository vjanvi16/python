
# Dictionary methods :-

# Update() :-

emp1 = {1:45,2:72,3:86,4:55,5:68}
emp2 = {12:36,16:11}
emp1.update(emp2)
print(emp1)

# Clear() :-

emp1.clear()
print(emp1)


# pop() :-

# It remove the item from dictionary.

emp1 = {1:45,2:72,3:86,4:55,5:68}
emp1.pop(3)
print(emp1)


# popitem() :-

# It will remove the last item from the dictionary.

emp1.popitem()
print(emp1)


# del :-

# del emp1        It will delete the entire dictionary
del emp1[1]
print(emp1)