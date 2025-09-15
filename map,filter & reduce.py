
# map() :-

# The map() function applies a function to each element in sequence and returns a new sequence containing the
# transformed element.

l = [3,5,4,6,8,3,2,8]
l2 = list(map(lambda x : x*x*x,l))
print(l2)


# Filter() :-

l = [3,5,4,6,8,3,2,8]
l2 = list(filter(lambda a : a>4,l))
print(l2)


# reduce() :-

from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y : x + y ,numbers)
print(sum)