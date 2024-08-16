class animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def make_sound(self):
        print("The animal makes a sound")
class dog(animal):
    def __init__(self,name,breed):
        animal.__init__(self,name,species="dog")
    def make_sound(self):
        print("Bark!")
d=dog("dog","Doggerman")
d.make_sound()
a=animal("Dog","Dog")
a.make_sound()