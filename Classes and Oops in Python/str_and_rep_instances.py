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
lets see the representation and string form of the object 
lets check of date
'''
import datetime
dt=datetime.date(2022,10,19)
print(dt)
print(repr(dt))
dt2=eval(repr(dt))
print(dt2)



'''
to give the custom behaviour when we need the str form of instance
and make it more descriptive we define __str__ method inside the class
so whenever we are converting it into string str(obj) the __str__ method will be triggered
'''
class Person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def change_age(self,age):
        self.age=age
    
    def __str__(self):
        return f"Person name is {self.name} and is {self.age} years old"
    def __repr__(self):
        return f"Person({repr(self.name)},{repr(self.age)})" '''
                                                            we are converting all the variables also in
                                                            their repr for then only we can create object 
                                                            using the repr of the whole object
                                                            '''

p=Person("Prince",20)
print(p)
print(str(p))
print(repr(p))
p2=eval(repr(p))
print(p2)

