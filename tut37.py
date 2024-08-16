class employee:
    companyName="Apple"
    noofemployees=0
    def __init__(self,name):
        self.name=name
        self.raise_amount=0.02
        employee.noofemployees+=1
    def showdetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noofemployees} in {self.companyName} is {self.raise_amount}")
# employee.showdetails(emp1)
emp1=employee("Harry")
emp1.raise_amount=0.03
emp1.showdetails()
employee.companyName="Walmart"
emp2=employee("Rohan")
emp2.showdetails()