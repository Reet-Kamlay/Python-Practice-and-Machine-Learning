from tkinter import *
from PIL import Image,ImageTk
app_root=Tk()


app_root.geometry("600x400")
app_root.minsize(200,100)
app_root.maxsize(1200,900)
reet=Label(text="Reet is a good boy and this is my GUI")
reet.pack()
image=Image.open("picture2.jpg")
photo=ImageTk.PhotoImage(image)
reet_label=Label(image=photo)
reet_label.pack()
app_root.mainloop()
