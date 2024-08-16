from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
# i=0
# def add():
#     global i
#     lbx.insert(ACTIVE,f"{i}")
#     i+=1
# lbx=Listbox(root)
# lbx.pack()
# lbx.insert(END,"First item of our listbox")
# Button(text="Add Item",command=add).pack()
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
listbox=Listbox(root,yscrollcommand=scrollbar.set)
for i in range(344):
    listbox.insert(END,f"Item {i}")
listbox.pack()
scrollbar.config(command=listbox.yview)
root.mainloop()