class employee:
    def __init__(self,empid,name,salary,address):
        self.empid=empid
        self.name=name
        self.salary=salary
        self.address=address
class teacher(employee):
    def __init__(self,empid,name,salary,address,department,subject):
        employee.__init__(self,empid,name,salary,address)
        self.department=department
        self.subject=subject
    def display(self):
        print("Employee ID:\t",self.empid,"\nName:\t\t",self.name,"\nSalary:\t\t",self.salary,"\nAddress:\t",self.address,"\nDepartment:\t",self.department,"\nSubject:\t",self.subject)
i=int(input("Enter the id:"))
n=input("Enter the name:")
s=int(input("Enter the salary:"))
a=input("Enter the address:")
d=input("Enter the department:")
sub=input("Enter the subject:")
ob=teacher(i,n,s,a,d,sub)
ob1=employee(i,n,s,a)
ob.display()
