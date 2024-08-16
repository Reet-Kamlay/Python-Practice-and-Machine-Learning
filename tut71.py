from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
def ordernow():
    print(f"we have received your {var.get()} order")
    tmsg.showinfo("Order Placed",f"we have received your {var.get()} order")
def getdollar():
    print(f"We have credited {myslider2.get()} to your bank account")
    tmsg.showinfo("Amount Credited",f"We have credited {myslider2.get()} to your bank account")
Label(root,text="How many dollars do you want?").pack()
myslider2=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.pack()
Button(root,text="Get Dollars!",command=getdollar).pack()
Label(text="What food do you want?").pack()
var=StringVar()
var.set("Radio")
b1=Radiobutton(root,text="Dosa",variable=var,value="Dosa").pack(anchor="w")
b1=Radiobutton(root,text="Idli",variable=var,value="Idli").pack(anchor="w")
b1=Radiobutton(root,text="Paratha",variable=var,value="Paratha").pack(anchor="w")
b1=Radiobutton(root,text="Samosa",variable=var,value="Samosa").pack(anchor="w")
Button(text="Order Now",command=ordernow).pack(anchor="w")
root.mainloop()