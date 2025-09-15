
# Set methods :-

# Union() method :-

s1 = {2, 22, 4, "apple", 36, True}
s2 = {16,4,False,"rose"}
print(s1.union(s2))     # print union of set 1 and 2.
s1.update(s2)  
print(s1,s2)            # print both set sapretlly.          


# Intersaction() method :-

cities = {"Tokyo","Mumbai","London","Paris"}
country = {"Japan","Paris","Thailand","Russia"}
print(cities.intersection(country))
# print(cities,country)


# diffrence() method :-

cities = {"Tokyo","Mumbai","London","Paris"}
country = {"Japan","Paris","Thailand","Tokyo"}
print(cities.difference(country))
print(country.difference(cities))


# isdisjoin() method :-

cities = {"Tokyo","Mumbai","London","Paris"}
country = {"Japan","Paris","Thailand","Tokyo"}
print(cities.isdisjoint(country))


# issuperset() method :-

cities = {"Tokyo","Thailand","London","Paris"}
country = {"Thailand","Tokyo"}
print(cities.issuperset(country))
print(country.issubset(cities))


# add() method :-

cities = {"Tokyo","Thailand","London","Paris"}
cities.add("Seoul")
print(cities)


# update() method :-

cities = {"Tokyo","Thailand","London","Paris"}
country = {"Seoul","Hongkong"}
cities.update(country)
print(cities)


# remove()/discard() method :-

# If u use remove method in set when the value is unpresent it will show an error.
# If u use discard method in set when the value is unpresent it will not show an error.
cities = {"Tokyo","Thailand","London","Paris"}
cities.remove("Tokyo")
cities.discard("china")
print(cities)


# pop() method :-

# This method remove the last item from the set.
cities = {"Tokyo","Thailand","London","Paris"}
cities.pop()
print(cities)


# del() method :-

country = {"Seoul","Hongkong"}
del country
# print(country)


# clear() :-

# If we don't want to delete the entire set, we just want to delete all items in the set we need to use clear.

country = {"Seoul","Hongkong"}
country.clear()
# print(country)


# check if item exits :-
cities = {"Tokyo","Thailand","London","Paris"}
if "Seoul" in cities:
    print("Yes seoul in cities")
else:
    print("No seoul is not in cities")