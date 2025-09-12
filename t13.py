from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
root=Tk()
root.title("Denomination Counter")
root.configure(bg="light blue")
root.geometry("650x400")

upload=Image.open("app_img.jpg")
image=ImageTk.PhotoImage(upload)
label=Label(root, image=image, bg='light blue')
label1=Label(root,text="Hey there! welcome to denomination counter!",bg='light blue')
label1.place(relx=0.5,y=340,anchor=CENTER)

def msgbox():
    Msgbox=messagebox.showinfo('Alert!','Do you want me to show the calculation')
    if Msgbox=="ok":
        topwin()

button=Button(root, text="Lets get started!",command=msgbox,bg="red",fg="white")
button.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg="light grey")
    top.geometry('600x300+50+50')
    lbl=Label(top,text="Enter total amount",bg="light grey")
    label=Label(top,text="Here are number of notes for each denomination",bg='light grey')
    l1=Label(top,text="2000",bg="light grey")
    l2=Label(top,text="500",bg="light grey")
    l3=Label(top,text="100",bg="light grey")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
def calculator():
    try:
        global amount
        amount=int(Entry.get())
        note2000=amount//2000
        amount%=2000
        note500=amount//500
        amount%=500
        note100=amount//100 
        t1.delete(0,END)       
        t2.delete(0,END) 
        t3.delete(0,END)
        t1.insert(END,str(note2000))
        t1.insert(END,str(note500))
        t1.insert(END,str(note100))
    except ValueError:
        messagebox.showerror("Error","Please enter a valid number")
    btn=Button(top,text='calculate',command=calculator,bg="red",fg="white")
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)

    top.mainloop()
root.mainloop()
