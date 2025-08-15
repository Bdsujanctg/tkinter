from tkinter import *

root=Tk()
root.title("Age calculator")
root.geometry("400x400")
lbl=Label(text="Enter birthyear",height='1',width='300',fg='white',bg='blue')
birth_entry=Entry()
def sub():
    birth=int(birth_entry.get())
    subs=2025-birth
    message="So you are "+str(subs)+"\n"
    textbox.insert(END,message)
btn=Button(text="Show results",command=sub,bg="green")
textbox=Text(height=3,fg="black",bg="white")
lbl.pack()
birth_entry.pack()
btn.pack()
textbox.pack()
root.mainloop()