from employee import Employee

class Company:
    def __init__(self) -> None:
        self.employees=[]
    def add_employee(self,first,last,salary):
        newemp=Employee(first,last,salary)
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
    c.add_employee("prince","raja",10000)
    c.add_employee("emp1","khali",1000000)
    c.add_employee("emp2","khali",200000000)
    c.add_employee("emp3","khali",30000000)
    c.pay_salary()
    c.all_employees()

if __name__==main():
    main()