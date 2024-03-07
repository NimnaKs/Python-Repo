import tkinter as tk

window = tk.Tk()
lbl = tk.Label(window, text="Click Me", bg="white", fg="navy")


def event_handler(event):
    if event.type == "7":
        lbl.config(bg="navy", fg="white")
        print("Enter")
    elif event.type == "8":
        lbl.config(bg="white", fg="navy")
        print("Leave")


lbl.bind("<Enter>", event_handler)
lbl.bind("<Leave>", event_handler)
lbl.pack()

window.mainloop()
