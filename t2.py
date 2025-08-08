from tkinter import *
from datetime import date
root=Tk()
root.title('Getting started with widgets')
root.geometry('300x400')

lbl=Label(text="Hey there!",fg='white',bg="blue",height=1,width=300)

name_lbl=Label(text="Full Name",bg='#3895d3')

name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to the application! \n Today's date: " 
    greet="Hello "+ name +"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END, date.today())

text_box=Text(height=3)
btn=Button(text="Click here",command=display,height=1,bg='#1261a0',fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()