
# 'is' VS '==' :-

# is :
# compare exact location of object in memory.

#  == :
#  == Compare the value

a = "Harry"
b = "Harry"
print(a is b)
print(a==b)


x = [1,2,3,4]
y = [1,2,3,4]
print(x is y)
print(x==y)

c = None
d = None
print(c is d)
print(c==d)
