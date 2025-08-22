from tkinter import *
root=Tk()
root.title("Length converter")
root.geometry("500x450")
lbl=Label(background="blue",fg="white",height=2,width=500,text="Convert")
lbl2=Label(background="light green",fg="white",height=2,width=500,text="Enter to convert")
entry1=Entry(text="Enter to convert")
def cm():
    ent=float(entry1.get())
    cm1=ent/100
    textbox.insert(END,cm1)
def m():
    ent2=float(entry1.get())
    m1=ent2*100
    textbox.insert(END,m1)
btn=Button(bg="red",fg="white",command=cm,text="Convert to centimeters")
btn2=Button(bg="red",fg="white",command=m,text="convert to meters")
textbox=Text(height=3,fg="black",bg="white")
lbl.pack()
lbl2.pack()
entry1.pack()
btn.pack()
btn2.pack()
textbox.pack()
root.mainloop()