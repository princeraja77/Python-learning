'''
we are going to declare functions inside the class which are called methods 
and use it to perform operation on instances
'''
class Employee:
    def __init__(self) -> None:
        self.__dict__["name"]="Prince"
        self.__dict__["salary"]=2000

    def increase_salary(employee,percentage):
        employee.salary+=employee.salary*percentage/100

e=Employee()
print(e.salary)
Employee.increase_salary(e,20)
print(e.salary)

'''
here we will do how it should be done with calling method using instance and not class
and first argument will automativ=cally the instance of class so no need to pass that 
only pass rest of the arguments
'''
class Person:
    def __init__(self) -> None:
        self.name="Prince"
        self.age=20
    
    def change_age(self,age):
        self.age=age

p=Person()
print(p.age)
p.change_age(30)
print(p.age)