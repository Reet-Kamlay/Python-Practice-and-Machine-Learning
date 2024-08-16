class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @classmethod
    def fromstr(self,str):
        return self(str.split("-")[0],str.split("-")[1])
e1=employee("Harry",12000)
print(e1.name)
print(e1.salary)
string="John-13000"
e2=employee.fromstr(string)
print(e2.name)
print(e2.salary)