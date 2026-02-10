# class Library:
#     def __init__(self):
#      self.noBooks = 0
#      self.Books =[]

#     def addbook (self,book):
#        self.Books.append(book)
#        self.noBooks = len(self.Books)

#     def showInfo (self):
#        print(f"The Libaray has {self.noBooks} books.The books are")
#        for book in self.Books:
#           print(book)

# L1 = Library()
# L1.addbook("biology")
# L1.addbook("Mathematics")
# L1.addbook("Science")
# L1.addbook("Chemistry")
# L1.showInfo()


class Library:
    def __init__(self):
        self.books = []          # list of books (no ebooks)
        self.no_of_books = 0     # number of books

    def add_book(self, book_name):
        # ebook check
        if "ebook" in book_name.lower():
            print("E-books are not allowed!")
        else:
            self.books.append(book_name)
            self.no_of_books = len(self.books)
            print(f'"{book_name}" added successfully.')

    def show_books(self):
        if self.no_of_books == 0:
            print("No books in library.")
        else:
            print("Books available in library:")
            for book in self.books:
                print("-", book)

    def get_number_of_books(self):
        # length check
        if self.no_of_books == len(self.books):
            print("Book count is correct.")
        else:
            print("Book count mismatch!")

        print("Total number of books:", self.no_of_books)


#program execution

lib = Library()

lib.add_book("Python Programming")
lib.add_book("Data Structures")
lib.add_book("Java ebook")      # This will be rejected
lib.add_book("DBMS")

lib.show_books()
lib.get_number_of_books()

     
                