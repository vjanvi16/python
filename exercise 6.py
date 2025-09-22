
class library:
    def __init__(self):
         self.NoOfBooks = 0
         self.Books = []

    def addBook(self,book):
         self.Books.append(book)
         self.NoOfBooks = len(self.Books)

    def showbook(self):
         print(f"The library has {self.NoOfBooks} books.")
         for b in self.Books:
              print(b)


l1 = library()
l1.addBook("Harry Potter")
l1.addBook("Pairets of the Carabians")
l1.showbook()