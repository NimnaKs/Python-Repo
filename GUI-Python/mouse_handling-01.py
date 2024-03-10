import tkinter as tk

window = tk.Tk()


def click_handler(event):
    if event.num == 1:
        print("Left Click")
    if event.num == 2:
        print("Mid Click")
    if event.num == 3:
        print("Right Click")


window.bind("<Button>", click_handler)

window.mainloop()
