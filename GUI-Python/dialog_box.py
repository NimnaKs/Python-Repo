import tkinter as tk
from tkinter import messagebox as mbox

window = tk.Tk()
window.title("Dialog Box")


def center_window(window, width, heigth):
    screen_widht = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_widht - width) // 2
    y_position = (screen_height - heigth) // 2

    window.geometry(f"{width}x{heigth}+{x_position}+{y_position}")


width = 250
height = 120

center_window(window, width, height)

window.configure(bg="white")

promt_label = tk.Label(
    text="Enter your name : ",
    foreground="black",
    background="white",
)

promt_label.pack(fill='x')

promt_label.place(x=20, y=10)

txtField = tk.Entry(window)
txtField.pack()
txtField.place(x=20, y=40)


def process_entry_data():
    data = txtField.get()
    mbox.showinfo(title="Alert", message=f"Your name is {data}")


process_btn = tk.Button(text="Process", command=process_entry_data)
process_btn.pack()
process_btn.place(x=80,y=80)

window.mainloop()
