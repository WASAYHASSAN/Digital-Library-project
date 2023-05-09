from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime

list_of_books = ["The Valley of farmer", "Robinson Crusoe", "Gladiators", "Cleopatra", "Napoleon", "The Adventures Of Sinbad The Sailor", "Snow White and The Seven Dwarfs", "Stories From The Jungle Book", "Alice In Wonderland", "The Shining Hour", "Tom Sawyer", "The Secret Garden", "Benny and the Giants", "Heroes and Heroines", "Geography of Pakistan", "The flopperty Bird", "Money Bags", "Aladin and the Wonderful Lamp", "Reader Digest Brain Power", "Horrid Henry and the secret club", "Oliver Twist", "Bignate", "The very clever farmer", "Gran", "John Sandford", "The Wonderful Wizard Of OZ", "Tiger's eye", "Ali Baba and the forty thieves", "Reader Digest Killer Whales in new Waters", "Key Words with Lady Birds 4a", "English Speeches and Dialogues", "Ten Stories from Islam", "The Ducks and the tortois", "Spies in Disguise", "Plum Girl", "Auxilaries and Modals", "The Motorway", "Key Word with Lady Birds 8a", "The Wakey Wakey Machine", "Dragon Stew", "Pirate Adventure", "The Princess and The Pea ", "The Farmer and His Sons", "The Boy Who Cried Wolf ", "The Eagle and the Man ", "The Stubborn Mule", "A Practical English Grammar (Third Edition)", "Othello and other Stories", "Kidnapped", "1000 Basic Signs", "How to Handle your Mum", "Master your English Noun", "Great book of Knowledge", "Mathematics Grade 1", "Readers Digest Chasing the Northern Lights", "The Art of War ", "Clever Sayyah The Laughing Fish", "Oxford Very Forst Atlas", "Puss in boots", "Nepoleon Bona Pat ", "Teesri ka chand ", "Kaam Chor", "Gullivers Travels", "Physics for Higher Tier ", "CHildren Conversation ", "The Iron Wall", "Wizards vs Alliens", "Treasury of Teddy Bear Travels", "Mutthu and The Magical Bowls", "First Encyclopedia of Seas and Oceans", "Aladidinn's Lamp", "The Steadfeast Tin Soldier", "Narayan The Magical Gem", "Cinderella", "Kohsar ki Sair ", "Tambakto", "Bulhan", "Sleeping Beauty", "The Sheep", "Storm Castle", "The Monkey and The Fishermen", "The Four Complains", "The Rat Who Bargains all the Time", "366 Stories", "The Mermaid Princess and the Octopus King", "Charlie Babbage", "Art and Craft", "David Copperfield", "Odyssey of a Sailor", "The Incredibles ", "Deceit of a Writer", "The Beaten Gate ", "Kyun ri Titli", "Aaiye ghar ko jahannum banaiye ", "Is there life after sixth Grade", "Three Men in a Boot ", "Interesting and Unique Talks", "No Easy Answers", "The Ugly Duckling", "The Monkey", "Abdul Sattar Edhi", "The Three Billy Goat Gruff", "Readers Digest Aching Knees", "Rainbows, Roots, and Magic Shoots", "Mutthu and the magical Bowls", "Baffy the Arrogant Rat", "Designed to take care of your back", "The Motorway", "Iron Man Extremis", "New Stories", "Queen Elizabeth I", "Joseph Stalin", "Modern Basic Science", "20 stories of prophet Muhammad", "The Boy Who Cried Wolf and The Goose that laid the Golden Eggs", "The Eagle and the man and Town Mouse and the Country Mouse", "Blue Beard", "The Rat who Bargains all the Time", "Aladdin's Lamp", "Roald Dahl", "Merry Mister Meddle", "Money Bags", "Shakespeare Alive! Book 1", "Readers Digest 6 new treatments that can save your life", "Fairy Tales", "New Trainers", "Edge", "joon put nadi lal", "Nostradamus Magic eye", "Sea Pheonix", "Children's First Fun Dictionary", "Hazrat Musa A.S (urdu)", "Modern English Nursery ", "Simply Science 2", "Simply Science 4", "Urdu Lazmi", "Information Technology and Computer Science Book 4", "Hazrat Shuaib AS", "Amir temur lung", "Gaba coloring for Nursery", "Urdu grade 7", "AAGNEE RUBY", "Josh malekh Abadi", "Molana hali", "Molana shibli nomani", "Meer taqi Meer", "ismail merthi", "Farooque Azam", "kanjoos ki kahani", "parveen shakir", "Abroo", "Faiz ahmed Faiz", "Hasrat mohani", "Akber ala Abadi", "The Dream", "salam", "hakim mohammad saeed", "rana liaquat ali khan", "Pakistan k das sadar ", "Pakistan k tehwaar or taqreebaat", "Majmua-o-taif ", "Hazrat Suleman AS", "An illustrated History of Pakistan Book 2", "Karachi ", "mulakaat", "kipper and the giant", "Amazing Science", "Oxford History for Pakistan", "Mutalia Islam 7", "Stories of the prophets", "My book of hajj and eid ul azha", "Humayunama", "Jahangirnama", "Akber and the crows", "Biffo gets stuck", "The Wolf ", "Asaan namaz", "sahaba karam ki hikayaat", "The Two frogs", "mohtarma fatima jinnah", "The Day of germen unity", "chaar shikayaten", "Monster stories", "noorani qaida", "Oxford Progressive English 6", "Children's pictorial Book of Knowledge", "Catalouge 2018", "Catalouge 2015", "pre school and primary Catalouge", "Catalouge 2019", "Model curriculum guide for 2020", "Model curriculum 2016", "Model curriculum 2013", "Model curriculum 2015", "Guidance Manual", "Model curriculum 2014", "Step 1 Ahead", "Real writing and readings", "Who killed kennedy", "Brotherband chronicals", "Screwed by eoin colfer", "more bubbles of water ", "i will find my way ", "understand and communicate", "learn English in 21 lessons", "The oxford book of urdu short stories", "synonyms and antonyms", "International English language book", "The Students Companions", "proverbs", "John Grisham The chamber and the rainmaker", "Pak english composition for everybody", "The Hardy boys Hazed", "The Hardy boys foul play", "The Hardy Boys hurricane joe", "Word puzzle Dictionary", "students' english to urdu Dictionary", "Marks Twain The Adventures of tom Sawyer", "Oxford mini school Thesaurus", "Dictionary English to urdu", "prophet Muhammad as a millitary leader and commander", "The great game", "Practical english usage", "Readers Digest word Power", "Readers Digest Act of kindness everyone can do", "Readers Digest Daffodil Power", "Readers Digest A polar bears journey", "Readers Digest saving notre dame", "Readers Digest Frozen back to life", "Readers Digest Social Media rules", "Readers Digest Kevin kwan", "Readers Digest True stories from our archives", "Readers Digest Natures Best Prescription", "Readers Digest Live better with less", "Readers Digets i survived!", "Readers Digest Old time doctor remedies that worked", "Readers Digest William Shakespeare Centuries of shaping language", "Ethics ", "When life begins ", "The kite runner", "Readers Digest Adult adhd", "Readers Digest Successful tips to slim", "Readers Digest The real CSI", "Readers Digest saving our sea turtles", "Readers Digest The healing power of you", "Readers Digest We need to rethink ", "Reader Digest Up close to a cheetah", "Reader Digest World War II Soldier's great escape", "Readers Digest Super recognisers", "Readers Digest skydiving terror", "Readers Digest Vinyl revival", "Readers Digest new secrets of a heart healthy", "Readers Digest Kindness of strangers", "readers Digest The future of flight ", "Readers Digest healthy truth about salt", "Readers Digest Prescription addiction", "Readers Digest Daniel Ricciardo", "Readers Digest Fighting a skin cancer", "Readers Digest The big One", "Readers Digest online privacy", "Readers Digest dealing with road rage", "Readers Digest Great Oceans secrets", "Readers Digest Digital Amnesia", "Readers Digest My coma miracle", "Speling bee word list 2010", "Speling bee word list 2011", "Speling bee word list 2013", "Speling bee word list 2014", "The influence of sea power upon History", "Dead Reckoning", "memories of 1972 Bangladesh War", "US millitary vehicals", "Haider ali", "safarnama", "dilchasp or anokhi batein", "ser na tamaam", "pahaar jise chiriya achi lagti thi", "Encyclopedia insani jism", "sindhi to urdu lughat", "nida k nanhe dost", "na school na homework"]

def search(event):
    value = event.widget.get()
    if value == '':
        combo_box['value'] = list_of_books

    else:
        data = []

        for item in list_of_books:
            if value.lower() in item.lower():
                data.append(item)
        combo_box['values'] = data
         
def issue():
    a = datetime.datetime.now()
    if bookvalue.get() in list_of_books:
        messagebox.showinfo("Info", "Book issued to the reader thanks for using this library.")
        list_of_books.remove(bookvalue.get())
        with open("readers_names.txt", "a") as f:
            f.write(f"{bookvalue.get()} issued to {namevalue.get()} on {datetime.datetime.now()} Due Date: {datetime.datetime.now() + datetime.timedelta(days=7)}\n")
    elif bookvalue.get().lower() not in list_of_books:
        messagebox.showinfo("Info", "Book is already issued.")
    else:
        messagebox.showerror("Invalid bookname please try again.")
    
def return_book():
    if return_value.get() not in list_of_books:
        list_of_books.append(return_value.get())
        messagebox.showinfo("Info", "Thanks for returning the book")
    elif return_value.get() in list_of_books:
        messagebox.showinfo("Info", "Reader has already returned the book")
    else:
        messagebox.showerror("Invalid bookname please try again later")


        
root = Tk()
root.title("Search books")
root.geometry("900x540")
label = Label(root, text="Search the books you want to issue", font=("Calibri body", 19)).grid(row=4, column=41)

combo_box = ttk.Combobox(root, value=list_of_books, font=("Calibri body", 13))
combo_box.set("Search")
combo_box.grid(row=5, column=41)
combo_box.bind('<KeyRelease>', search)

Label(root, text="Enter your name:", font=("Calibri body", 15)).grid()

namevalue = StringVar()
Entry(root, textvariable=namevalue, font=("Calibri body", 15, "bold")).grid()


Label(root, text="Enter the name of book:", font=("Calibri body", 15)).grid(row=15)
bookvalue = StringVar()
Entry(root, textvariable=bookvalue, font=("Calibri body", 15)).grid()

Label(root, text="Enter the name of book you want to return:", font=("Calibri body", 15)).grid(row=54)
return_value = StringVar()
Entry(root, textvariable=return_value, font=("Calibri body", 15)).grid()

Button(root, text="Issue", font=("Calibribody", 15), relief=None, bg="lightblue", pady=4, command=issue).grid(row=51)
Button(root, text="Return", font=("Calibri body", 15), relief=None, bg="lightblue", pady=4, command=return_book).grid()

root.mainloop()
