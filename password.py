from tkinter import *
import os
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("Security")

def enter():
    if reader_value.get() == 'library':
        os.startfile("GUI_library_page_1.py")
    elif reader_value.get() == '':
        messagebox.showerror("Error", "Please enter password")
    elif reader_value.get() != 'library':
        messagebox.showerror("Error", "Invalid password")
    




Label(root, text="Enter password: ", font=("Calibri body", 20, "bold")).grid()

reader_value = StringVar()
Entry(root, textvariable=reader_value, font=("Calibri body", 16)).grid()

Button(root, text="Enter", font=("Calibribody", 18), fg="black", relief=None, bg="lightblue", command=enter).grid()


root.mainloop()