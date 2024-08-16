from tkinter import *
root=Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()
can_widget.create_line(0,0,800,400,fill="red")
widget=Button(root,text="")
root.mainloop()