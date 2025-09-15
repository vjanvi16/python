
# STRING METHODS :-

# 1. Upper() method :
# The upper method converts a string in uppercase.
a = "harry"
print(a.upper())


# 2. lower() method :
# The lower method converts a string in lowercase.
b = "Harry"
print(b.lower())


# 3. capitalize() method :
# The capitalize method converts only the first latter of the string in to uppercase and the rest other latter of
# the string are turned into a lowercase. The string has no effect if the first character already in uppercase.
c = "harry Parry"
print(c.capitalize())


# 4. replace() method :
# The replace method replace a string with new string.
d = "Harry"
print(d.replace("Harry","Jerry"))


# 5. count() method :
# The count() method returns the number of times the given value has occurred within the given string.
e = "harry"
print(e.count("r"))

nm = "hey! harry, Welcome to the city harry."
print(nm.count("harry"))


# 6. endswith() method :
# The endswith() method check if the string end with a given value. If yes than return true,else return false.
a = "harry"
print(a.endswith("y"))


# 6. startswith() method :
# The startswith() method check if the string start with a given value. If yes than return true,else return false.
a = "harry"
print(a.startswith("J"))


# 7. find() :
# The find() method searches for the first occurrence of the given value and returns the index where it is
# present. It given value is absent from the string then return -1.
str1 = "He's name is Dan. He is an Honest man."
print(str1.find("is"))
print(str1.find("fan"))


# 8. index() :
# The find() method searches for the first occurrence of the given value and returns the index where it is
# present.It given value is absent from the string then return an error.
# This is the diffrence between find() and index().
str2 = "He's name is Dan. He is an Honest man."
print(str2.index("Dan"))
print(str2.index("Dann"))





