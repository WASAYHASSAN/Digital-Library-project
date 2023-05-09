import os  # <module 'os' from 'C:\\Users\\LENOVI\\AppData\\Local\\Programs\\Python\\Python310\\lib\\os.py'>

from tkinter import *       # <module 'tkinter' from 'C:\\Users\\LENOVI\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\playsound.py'>

root = Tk()         # declaring root
root.title("Educators Library")  # declaring title


    
    
def issue_book():           
    os.startfile("Issue_book.py")





def see_last_readers():     # see_last_readers method
    os.startfile("readers_names.txt")

    
def exit():         # exit method
    root.destroy()

root.geometry("2000x2000")      # declaring geometry
root.minsize(200, 200)          # minimum size is 200x200
root.title("Library")

# label (Educators Library)
label = Label(root, fg="green" ,bg="cyan", text="Educators Library", font=("Impact", 60), padx=200, pady=40)
label.pack(fill=X)

# main frame
frame = Frame(borderwidth=5, bg=None, pady=20, padx=20)
frame.pack(side=LEFT, anchor="w")


# second button
button_2 = Button(frame, fg="black" ,bg="skyblue", text="Issue a book", relief=GROOVE, pady=10, padx=20, font=("Impact", 20), command=issue_book)
button_2.pack(pady=10)



# fifth button 
button_5 = Button(frame, bg="skyblue", text="Library Record History", relief=GROOVE, pady=5, padx=20, font=("Impact", 20), command=see_last_readers)
button_5.pack(pady=10)

# fourth button
button_4 = Button(frame, bg="skyblue", text="Exit", relief=GROOVE, pady=5, padx=20, font=("Impact", 20), command=exit)
button_4.pack()




root.mainloop()         # mainloop for entering GUI



