
# SELF PARAMETER :-

# If we create function in class. Then we have to write self in function.
# Then we have to write self in () of function otherwisw the output show error.

class employee:
    language = "python"   
    salary = 400000

    def getInfo(self):
         print(f"The language is {self.language} and the salary is {self.salary}")
    
    def greet(self):
         print("Good Day..:)")

emp = employee()
emp.language =  "JavaScript"
print(emp.language,emp.salary)
emp.getInfo()
emp.greet()



# STATIC METHOD :-

# When  in the function can't call any object then we don't need to add self 
# We just have to use @staticmethod there.

class employee:
    language = "python"   
    salary = 800000

    def getInfo(self):
         print(f"The language is {self.language} and the salary is {self.salary}")
    
    @staticmethod
    def greet():
         print("Good Day..:)")

emp = employee()
print( emp.language,emp.salary)
emp.getInfo()
emp.greet()



class person:
     name = "Harry"
     occupation = "Software Developer"

     def info(self):
          print(f"{self.name} is a {self.occupation}")

a = person()
a.info()

b = person()
b.name = "Jarry"
b.occupation = "Manager"
b.info()