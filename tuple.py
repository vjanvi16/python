
# Tuple :-

# Tuples are inmutable.
# Strings are inmutable.

t = (2,4,6,8,9,11,"green",True)

print(type(t))
print(t)
print(len(t))


# Indexing in tuple :-

print(t[0])
print(t[:8])
print(t[1:])


if 11 in t:
    print("Yes 11 in this tuple")


t2 = t[6:8]
print(t2)
