import tkinter as tk

window = tk.Tk()
window.title("Centered Window")


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_position = (screen_width - width)//2
    y_position = (screen_height - height)//2

    window.geometry(f"{width}x{height}+{x_position}+{y_position}")


width = 400
height = 300

center_window(window, width, height)

window.mainloop()
