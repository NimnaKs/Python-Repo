import tkinter as tk

window = tk.Tk(className="Exit Btn Program")

frame1 = tk.Frame(window,borderwidth=15)
frame1.pack(fill=tk.BOTH,expand=1)

"""
fill options:
 NONE (default), which will keep the widget’s original size.
 X, fill horizontally.
 Y, fill vertically.
 BOTH, fill horizontally and vertically.
"""
"""
expand : is an option for assigning additional space to the widget container
"""

label = tk.Label(
    frame1,
    text="I'm colored!",
    foreground="red",
    background="white"
)

label.pack(fill='x')

label = tk.Label(
    window,
    text="I'm colored too!",
    foreground="blue",
    background="black"
)

label.pack(fill='y',expand=True)

button = tk.Button(frame1,text="Exit",command=window.destroy)
button.pack(side=tk.BOTTOM)

"""
side : is a basic option, and includes padding options for positioning widgets in relation to the left,
right, top, bottom sides of the widget, and relative to each other.
"""

window.mainloop()