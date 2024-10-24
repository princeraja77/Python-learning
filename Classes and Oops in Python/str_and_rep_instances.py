'''
if we normally print instance of a class it will
only print about the class of instance and adresss
'''
class Employee:
    def __init__(self) -> None:
        self.__dict__["name"]="Prince"
        self.__dict__["salary"]=2000

    def increase_salary(employee,percentage):
        employee.salary+=employee.salary*percentage/100

e=Employee()
print(e)

'''
to give the custom behaviour when we need the str form of instance
and make it more descriptive we define __str__ method inside the class
so whenever we are converting it into string str(obj) the __str__ method will be triggered
'''
class Person:
    def __init__(self) -> None:
        self.name="Prince"
        self.age=20
    
    def change_age(self,age):
        self.age=age
    
    def __str__(self):
        return f"Person name is {self.name} and is {self.age} years old"

p=Person()
print(p)
print(str(p))