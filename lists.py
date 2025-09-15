
# Introduction to List :-

# LIST :-

# python list are contains to store a set of values of any data type.
# Lists are mutable.

friends = ["Apple","orange",6,16.11,False,"bts","kdrama"]
print(friends)
print(friends[0])
friends[0] = "Elephant"
print(friends[0])


# LIST INDEXING :-

# list can be indexing just like strings.

print(friends[6])
print(friends[1:4])


# Check element in list:

if "bts" in friends:
    print("Yes")
else:
    print("No")

if "jnv" in friends:
    print("Yes")
else:
    print("No")


# Same thing applies for string as well in list.
if "ts" in "bts":
    print("Yes")
else:
    print("No")


# List Comprehension :-

# list comprehension are used for creating new list from other iterables like lists,tuples,dictionaries,sets,
# ane even arrays and string.

list = [i for i in range(5)]
print(list)

# We can also add condition after the list :-

list = [i for i in range(10) if i%2==0]
print(list)