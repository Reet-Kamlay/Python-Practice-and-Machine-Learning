from tkinter import *
root=Tk()
def myfunc():
    print("Hello Guys")
# mymenu=Menu(root)
# mymenu.add_command(label="File",command=myfunc)
# mymenu.add_command(label="Exit",command=quit)
# root.config(menu=mymenu)
yourmenu=Menu(root)
m1=Menu(yourmenu,tearoff=0)
m2=Menu(m1,tearoff=0)
m2.add_command(label="Single Page")
m2.add_command(label="Multiple Pages")
m1.add_command(label="New Project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_command(label="Save As",command=myfunc)
yourmenu.add_cascade(label="File",menu=m1)
m1.add_cascade(label="Print",menu=m2)
root.config(menu=yourmenu)
root.mainloop()