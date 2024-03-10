import tkinter as tk

window = tk.Tk()


def key_handler(event):
    print(f"char:{event.char} "
          f"sym:{event.keysym} "
          f"code:{event.keycode} ")


window.bind("<Key>", key_handler)

window.mainloop()
