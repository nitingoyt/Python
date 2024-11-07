# Write a Library class with no_of_books and books as two instance variables. 
# Write a program to create a library from this Library class and show how you can print all books,
# add a book and get the number of books using different methods.
# Show that your program doesnt persist the books after the program is stopped!


class Library:

    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addbooks(self, book):
        self.books.append(book)
        self.no_of_books +=1
    
    def printbooks(self):
        print(f"No. of books in library is: {self.no_of_books}")
        print("List of books->")
        for book in self.books:
            print(f"book")


a1 = Library()
a1.addbooks("Lord of rings")
# Library.addbooks("Silence")
a1.addbooks("1983")
a1.addbooks("Silence")
a1.addbooks("Min hao")
print(Library.printbooks)
a1.printbooks()
