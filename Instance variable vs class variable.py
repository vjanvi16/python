
# Instance attribute VS Class attributes :-

# INSTANCE ATTRIBUTES take preference over CLASS ATTRIBUTES during assignment and retrival.
# In the below program u can show instance attribute take first preferece over the class attribute.
# The language of instance attribute print and the language of class doesn't print in emp object.

class employee:
    language = "python"   # This is class attribute
    salary = 400000

emp = employee()
emp.language = "JavaScript"   # This is an instance attribute.
print( emp.language,emp.salary)

emp2 = employee()
print( emp2.language,emp2.salary)



# Instance variable VS Class variable :-

class Employee:

    companyName = "Apple"         # Class variable
    NoOfEmployee = 0

    def __init__(self,nm):
        self.name = nm            # Instance variable
        self.raise_amount = 0.2
        Employee.NoOfEmployee += 1
    
    def showDetails(self):
        print(f"The employee number {self.NoOfEmployee} is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}.")

emp1 = Employee("Harry")
emp1.showDetails()
emp2 = Employee("Perry")
emp2.raise_amount = 0.4
emp2.companyName = "Samsung"
emp2.showDetails()
