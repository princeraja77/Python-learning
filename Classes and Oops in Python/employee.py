class Employee:
    def __init__(self) -> None:
        self.__class__=Employee
emp1=Employee()
print(emp1.__class__)