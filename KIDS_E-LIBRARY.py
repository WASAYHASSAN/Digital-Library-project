import datetime

class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks
    
    def availableBooks(self):
        print("Book available in this library are: ")
        for book in self.books:
            print("\t *" + book)

    def issueBook(self, bookName):
        if bookName in self.books:
            a = datetime.datetime.now()
            print(f"{bookName} issued to {b} on {datetime.datetime.now()}, to be returned on {a + datetime.timedelta(days = 7)}.")
            print()
            self.books.remove(bookName)
            return True
        else:
            print("Already issued")
            print()
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book!")
        print()

class Reader:
    def requestBook(self):
        self.book = input("Please type the name of the book you want to issue: ")
        return self.book

    def returnBook(self):
        self.book = input("Please type the name of the book you want to return: ")
        return self.book

if __name__ == "__main__":
    KidsLibrary = Library(["David Copperfield", "The Picwick Papers", "Great Expectations", "Oliver Twist", "Treasure Island", "Kidnapped", "The Swing", "A Tale of Two Cities", "Hard Times", "Harry Potter", "Romeo and Juliet","Julius Ceasar", "Thirty Thousand Leagues Under Sea", "The Suicide Club", "My Shadow", "Bleak House", "A Christmas Carol", "Little Dorrit"])
    student = Reader()

while (True):
        welcomeMsg = '''=====+++++ Welcome to Kids Library +++++=====
        Choose what you want to do:
        1, List all books available in library
        2, Issue a book
        3, Return a book
        4, Exit
        '''
        print(welcomeMsg)
        b = str(input("Enter reader's name: "))
        print()
        a = int(input("Enter step no. from above: "))
        
        if a == 1:
            KidsLibrary.availableBooks()
        elif a == 2:
            KidsLibrary.issueBook(student.requestBook())
        elif a == 3:
            KidsLibrary.returnBook(student.returnBook())
        elif a == 4:
            Thanks = str(input(f"Thanks for choosing kids Library would you recommend this library to your friend, if yes then type y if no then type n: "))
            if Thanks == 'y':
                print()
                mail = str(input("Enter the email address of your friend: "))
                print()
                print(f"We will send library's notification on {mail}")
                exit()
            else:
                exit()
        else:
            print("Invalid Choice")
            
        with open('readers_names.txt', "w") as f:
            f.write(f"Last Reader: {b}")


            
            


