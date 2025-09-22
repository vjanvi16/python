
# CONSTRUCTOR :-

#  CONSTRUCTOR also known as __init__().
#  __init__() is a special method which is first run as soon as the object is created.
# It takes a self argument and can take further arguments.

class person:
     def __init__(self,nm,occ):
        self.name = nm
        self.occupation = occ
        print("Hey! I m The person.")

     def info(self):
        print(f"{self.name} is {self.occupation}")

obj = person("Harry","Developer")
obj2 = person("Parry","HR")
obj.info()
obj2.info()




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

# In the above program we doesn't called __init__().
# It called automatically when the program run.
# it run first before the any object.


