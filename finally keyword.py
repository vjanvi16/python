
# Finally Keyword in python :-

# Finally keyword is always execute in the program.

def func1():
    try :
        l = [1,3,5,7,8,9]
        i = int(input("Enter the index : "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I'm always executed")

a = func1()
print(a)