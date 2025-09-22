
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



class employee:
    language = "python"   
    salary = 400000

    def __init__(self,name,language,salary):
         self.name = name
         self.language = language
         self.salary = salary
         print("I am creating an object")
    
    @staticmethod
    def greet():
         print("Good Day..:)")

emp = employee("Janvi","C++",200000)
print( emp.name,emp.language,emp.salary)
emp.greet()

emp2 = employee("Rajoo","C",250000)
print(emp2.name,emp2.language,emp2.salary)