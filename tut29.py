class person:
    name="harry"
    occupation="Manager"
    salary=1000
    def info(self):
        print(f"{self.name} is a {self.occupation}")
a=person()
a.name="Reet"
a.occupation="Designer"
b=person()
b.name="Sujay"
b.occupation="Accountant"
a.info()
b.info() 