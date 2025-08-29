from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

def load_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt1.delete(1.0, END)
    f = open(filepath, "r")
    txt1.insert(END, f.read())
    f.close()
    window.title(f"Interest & Text Editor - {filepath}")

def store_file():
    filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    f = open(filepath, "w")
    f.write(txt1.get(1.0, END))
    f.close()
    window.title(f"Interest & Text Editor - {filepath}")

def calculate_interest():
        principal = float(entry1.get())
        time = float(entry2.get())
        rate = float(entry3.get())
        si = (principal * time * rate) / 100
        ci = principal * ((1 + (rate/100))**time) - principal
        lbl4.config(text=f"Simple Interest: {si:.2f}")
window = Tk()
window.title("Interest & Text Editor")
window.geometry("700x600")

lbl1 = Label(window, text="Principal Amount:", font=("Arial", 12))
lbl1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry1 = Entry(window, width=20)
entry1.grid(row=0, column=1, padx=10)

lbl2 = Label(window, text="Time Period (years):", font=("Arial", 12))
lbl2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry2 = Entry(window, width=20)
entry2.grid(row=1, column=1, padx=10)

lbl3 = Label(window, text="Rate of Interest (%):", font=("Arial", 12))
lbl3.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry3 = Entry(window, width=20)
entry3.grid(row=2, column=1, padx=10)

btn1 = Button(window, text="Calculate Interest", command=calculate_interest, bg="green", fg="white")
btn1.grid(row=3, column=0, columnspan=2, pady=10)

lbl4 = Label(window, text="Simple Interest: ", font=("Arial", 12))
lbl4.grid(row=4, column=0, columnspan=2, pady=5)

btn_load = Button(window, text="Load File", command=load_file, bg="blue", fg="white")
btn_load.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

btn_store = Button(window, text="Save As", command=store_file, bg="orange", fg="white")
btn_store.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

txt1 = Text(window, height=15)
txt1.grid(row=7, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

window.mainloop()
