from tkinter import *
root=Tk()
root.title('Multiplier App')
root.geometry('300x400')
label1=Label(height='1',width='300',text='Enter the first number',fg='white',bg='light green')
entry1=Entry()
label2=Label(height='1',width='300',text='Enter the second number',fg='white',bg='light blue')
entry2=Entry()
def multiply():
    num1=float(entry1.get())
    num2=float(entry2.get())
    mul=num1*num2
    text_box.insert(END,mul)

text_box=Text(height=3)
btn=Button(text="Click",command=multiply,fg='black',bg='light yellow')
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
btn.pack()
text_box.pack()
root.mainloop()

