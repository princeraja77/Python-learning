# so the __new__ creates the object with empty dictionary and passes that object as first parameter of __init__
#so using that internal dict we are assigning variable because variables are stored as dict in object
class Employee:
    def __init__(self) -> None:
        self.__dict__["name"]="Prince"
        self.__dict__["salary"]=2000

# assigning the variable using simpler syntax provided by python
class Person:
    def __init__(self) -> None:
        self.name="Prince"
        self.age=20


print(Employee.__dict__)
e=Employee()
p=Person()
print(e.__dict__)
print(p.__dict__)