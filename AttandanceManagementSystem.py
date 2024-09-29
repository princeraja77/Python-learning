import json
from datetime import date

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f'Name : {self.name} Age: {self.age}'

class Student(Person):
    def __init__(self,name,age,Student_id):
        super().__init__(name,age)
        self.__Student_id=Student_id
        self.attendance_list=[]

    def __str__(self):
        return f'Name : {self.name} Age: {self.age} Student id: {self.__Student_id}'

    def serialize(self):
        return {"Name" : self.name,"Age": self.age, "Student id": self.__Student_id,"Attandence list":self.attendance_list}

class Attendence_Management_system:
    def __init__(self):
        self.student_data={}
        try:
            with open("studentData.json",'r') as data:
                self.student_data=json.load(data)
        except:
            self.student_data={}
        
    def add_student(self,name,age,Student_id):
        s_id=Student_id
        
        if s_id in self.student_data:
            print("Student id already present")
            return
        self.student_data[s_id]=Student(name,age,Student_id).serialize()
        print("Addition done successfully")
        
    def remove_student(self,Student_id):
        if Student_id in self.student_data:
            self.student_data.pop(Student_id)
            print("removed successfully")
        else:
            print("No student to remove")
            
    def view_student_list(self):
        for i in self.student_data:
            print(self.student_data[i])
            
    def mark_attendence(self,Student_id):
        if Student_id in self.student_data:
            self.student_data[Student_id]["Attandence list"].append(str(date.today()))
        else:
            print("invalid student id")
    def get_attendence_list(self,Student_id):
        if Student_id in self.student_data:
            print(self.student_data[Student_id]["Attandence list"])
        else:
            print("invalid student id")
        
    def save_data(self):
        with open("studentData.json",'w') as data:
            json_object=json.dumps(self.student_data,indent=4)
            data.write(json_object)

def main():
    system=Attendence_Management_system()
    
    while 1:
        print("Attendance Maintainance System")
        print("1. Add new Sudent")
        print("2. Remove a Sudent")
        print("3. View all student details")
        print("4. Mark Attendance")
        print("5. Attandence list by student id")
        print("6. Exit")
        
        
        choice = int(input())
        
        if choice==1:
            name=input("enter student name: ")
            age=int(input("enter student age: "))
            Student_id=input("enter student id: ")
            system.add_student(name,age,Student_id)
            
        elif choice==2:
            r_id=input("enter student id : ")
            system.remove_student(r_id)
            
        elif choice==3:
            system.view_student_list()
            
        elif choice==4:
            Student_id=input("enter student id :")
            system.mark_attendence(Student_id)
            
        elif choice==5:
            Student_id=input("enter student id :")
            system.get_attendence_list(Student_id)
            
        elif choice==6:
            system.save_data()
            break
        
        else:
            print("Invalid choice")
            
        print()
    
if __name__== "__main__":
    main()
    