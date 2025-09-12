from tkinter import *
root=Tk()
root.title("Main")
root.geometry("400x300")

def topwin():
    top=Toplevel()
    top.title("Top")
    top.geometry("180x100")
    l2=Label(top,text="This is toplevel window")
    l2.pack()

    top.mainloop()
l=Label(root,text="This is root window" )
btn=Button(root,text="Click her to open another window",command=topwin)
l.pack()
btn.pack()
root.mainloop()