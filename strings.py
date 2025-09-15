
# STRING :-

# In python, anything that you enclose between single or double quotation mark is consider a string.
# Strings are immutable.

name = "animal"
thing = 'cars'
print(name)
print(thing)


msg = "He said, \"I want to eat apple."
print(msg)


# If u want to print multiple line in string then u need to use """   """ or '''  '''.
print("""He said,
he want to 
eat an apple. """)


# Accessing characters of a string :-

name = "animal"
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])

# Looping through the string :-

name = "animal"
for character in name:
    print(character)
