
import tkinter as tk

window = tk.Tk()

def openWindow():
    window2 = tk.Toplevel()
    window2.title("New Wind")


button = tk.Button(window, text='New Window', command= openWindow)
button.grid()



window.mainloop()