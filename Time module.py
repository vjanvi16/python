
# Time module :-


import time

def usingwhile():
    i = 0
    while i < 10:
        i = i + 1
        print(i)

def usingfor():
    for i in range(10):
        print(i)


t = time.time()
usingwhile()
t1 = time.time()-t

t = time.time()
usingfor()
t2 = time.time()-t

print(t1)
print(t2)


# time.sleep() :-

print("Harry")
time.sleep(4)
print("This is print after 4 second.")



# time.strftime() :-

# The time.strftime() function formats a type value as string, based on a specified format.

t = time.localtime()
formatted_time = time.strftime("%Y-%M-%D \n%H:%M:S")
print(formatted_time)