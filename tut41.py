class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @classmethod
    def fromstr(self,str):
        return self(str.split("-")[0],str.split("-")[1])
s1=student("Harry",12000)
print(s1.name)
print(s1.marks)
string="John-13000"
s2=student.fromstr(string)
print(s2.name)
print(s2.marks)
