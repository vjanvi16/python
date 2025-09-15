 
# DICTIONARY :-

# Dictionary is a collection of key-value pairs.
# Dictionary is mutable.

d = {}  # this is an empty dictionary.


# In this example janvi,anjali and hiral are key of dictionary mark and 98,94,26 are value of it.
marks = {"janvi":98,"anjali":94,"hiral":26}

print(marks,type(marks))
print(marks["janvi"])


# In this example name are key of dictionary and countries are value of dictionary.
dic = {
    "janvi":"India",
    "Jimin":"South Korea",
    "Jong":"Thailand"
}
print(dic["Jong"])
print(dic.keys())       # print keys of the dictionary
print(dic.values())     # print value of the dictionary

# Using for loop :-

for k in dic.keys():
    print(f"The value of {k} is {dic[k]}")


# Accessing Keys :-

# We can print all the key value pairs in the dictionary using items() method.
dic = {
    "janvi":"India",
    "Jimin":"South Korea",
    "Jong":"Thailand"
}
print(dic.items())

# Using for loop :-

for key,value in dic.items():
    print(f"{key} is from {value}")
