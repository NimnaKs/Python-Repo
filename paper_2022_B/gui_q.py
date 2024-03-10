from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter as tk

root = Tk()
root.title("CS1101")

lb1 = Label(root, text="Enter your name: ")
lb1.grid(column=1, row=1)

hieghttxt = Entry(root, width=25)
hieghttxt.grid(column=2, row=1)

lb2 = Label(root, text="Select your color:")
lb2.grid(column=1, row=3)

cbl = Combobox(root)
cbl["values"] = ("Red", "Green", "Yellow", "Blue")
cbl.current(2)
cbl.grid(column=2, row=3)

ch_State = BooleanVar()
ch_State.set(False)
chk = Checkbutton(root, text="Print Name", var=ch_State)
chk.grid(column=1, row=4)


def clicked():
    msg = " likes " + cbl.get()
    if ch_State.get():
        msg = hieghttxt.get() + msg
    messagebox.showinfo("Done!", msg)


btenter = Button(root, text=" Generate ", command=clicked)
btenter.grid(column=2, row=4)
root.mainloop()
