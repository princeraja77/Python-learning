class Employee:
    def __init__(self,first,last,salary) -> None:
        self.firstname=first
        self.lastname=last
        self.salary=salary
    def calculate_paycheck(self):
        return self.salary/12
    