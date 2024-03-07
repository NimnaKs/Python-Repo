import tkinter as tk

window = tk.Tk()

def configure_handler(event):
    print(f"X:{event.x} Y:{event.y} "
          f"Width:{event.width} Height:{event.height}")

window.bind("<Configure>",configure_handler)

window.mainloop()