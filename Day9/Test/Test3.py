#library management system
class Library:
    def __init__(self):
        self.title = input("Enter the name of the book:")
        self.author = input("Enter the author of the book:")
        self.isbn = input("Enter the ISBN number of the book:")
    
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)

book1 = Library()
book1.display()