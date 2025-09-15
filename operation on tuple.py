
# Manipulating Tuple :-

# Tuple are inmutable, If you want to add, remove or change tuple item, then first you must convert the tuple 
# into List. The perform operation on that list and convert it back to tuple.

country = ("Spain","Italy","India","England","Germany")
print(type(country))
temp = list(country)
temp.append("Russia")       # add item
print(country)
temp.pop(2)                 # remove item
print(country)              # In this output the original tuple will print bcz tuple are inmutable.
temp[2] = "South korea"     # Change item
country = tuple(country)
print(country)

country2 = ("China","Thailand","Japan")
countries = country + country2
print(countries)


# count() Method :-

# The count() method of tuple returns the number of times the given element appears in tuple.
t1 = (0,1,2,46,2,44,56,2,5,2,2)
print(len(t1))
print(t1.count(2))


# index() Method :-

# The index() method return the first occurrence of the given element from the tuple. 
# tuple.index(element,start,end)

print(t1.index(44))

print(t1.index(2,1,6))  #This tuple will start from index 1 and end at index 6 and output will show of element 2.
