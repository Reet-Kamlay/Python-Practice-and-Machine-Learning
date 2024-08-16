class employee:
    company="Apple"
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")
    @classmethod
    def changecompany(self,newcompany):
        self.company=newcompany
e1=employee()
e1.name="Harry"
e1.show()
e1.changecompany("Tesla")
e1.show()
print(employee.company)