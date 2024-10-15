class Employee:
    def __init__(self,first,last) -> None:
        self.firstname=first
        self.lastname=last

class SalaryEmployee(Employee):
    def __init__(self, first, last,salary) -> None:
        super().__init__(first, last)
        self.salary=salary
    def calculate_paycheck(self):
        return self.salary/12
    
class HourlyEmployee(Employee):
    def __init__(self, first, last,h_rate) -> None:
        super().__init__(first, last)
        self.h_rate=h_rate
    def calculate_paycheck(self,t_hour=45):
        return self.h_rate*t_hour
    
class CommisionEmployee(SalaryEmployee):
    def __init__(self, first, last, salary,c_rate) -> None:
        super().__init__(first, last, salary)
        self.c_rate=c_rate
    def calculate_paycheck(self,t_sales=30):
        return self.salary+(self.c_rate*t_sales)

class Company:
    def __init__(self) -> None:
        self.employees=[]
    def add_employee(self,newemp):
        self.employees.append(newemp)
    def pay_salary(self):
        for emp in self.employees:
            pay=emp.calculate_paycheck()
            print(f"Amount ${pay:,.2f} paid to {emp.firstname+" "+emp.lastname}")
        print("==============================================================")
    def all_employees(self):
        print("List of all Employees\n")
        for emp in self.employees:
            print(emp.firstname,emp.lastname)
        print("==============================================================")
        

def main():
    c=Company()
    emp1=SalaryEmployee("prince","raja",10000000)
    emp2=HourlyEmployee("kavita","rani",500)
    emp3=CommisionEmployee("Yogesh","Kumar",100000,700)
    c.add_employee(emp1)
    c.add_employee(emp2)
    c.add_employee(emp3)
    c.pay_salary()
    c.all_employees()

if __name__==main():
    main()

