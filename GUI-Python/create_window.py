import tkinter as frame

topLevelWidget = frame.Tk()

print("Starting main loop")

topLevelWidget.mainloop()

print("End main loop")

"""
mainloop(): This method starts an event loop. 
            Unlike the programs we wrote before this is an event based program. 
            This can receive events such as button clicks, window events etc. 
            Without calling the mainloop the window will not appear in the screen.

Only when the window is closed we will see the rest of the code is being executed
"""