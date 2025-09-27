
# Walrus Operator :-

# Walrus Operator allows you to assign value to a variable within an expression.
# This can be useful when you need to use value multiple times in a loop, but don't want to reapet 

a = True
print(a:=False)

numbers = [1,2,3,4,5]
while (n := len(numbers)) > 0:
    print(numbers.pop())


happy = True
print(happy)

print(happy := False)

foods = list()
while True:
    food = input("Which food do you like most ? ")
    if food == "quit":
        break
    foods.append(food)