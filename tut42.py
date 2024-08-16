class parent:
    def parentmethod(self):
        print("This is the parent method")
class child(parent):
    def parentmethod(self):
        print("Hello")
        super().parentmethod()
    def childmethod(self):
        print("This is the child method")
        super().parentmethod()
child_object=child()
child_object.childmethod()
child_object.parentmethod()