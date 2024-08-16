class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)
        self.lang=lang
rohan=employee("Rohan Das","420")
harry=programmer("Harry","2345","Python")
print(harry.name)
print(harry.id)
print(harry.lang)