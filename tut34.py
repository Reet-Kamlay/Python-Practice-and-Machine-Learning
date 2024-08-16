class employee:
    def __init__(self,name,id):
        self._name=name
        self._id=id
    def showdetails(self):
        print(f"{self._name} is a employee of id {self._id}")
class programmer(employee):
    def showlanguage(self):
        print("The default language is python")
e1=employee("Rohan Das",400)
e1.showdetails()
e2=programmer("Harry",600)
e2.showdetails()
e2.showlanguage()