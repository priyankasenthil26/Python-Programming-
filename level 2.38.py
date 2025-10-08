# Library Management System

class Library:
    def __init__(self):
        self.books = [
            {"title": "Book A", "author": "Author 1", "available": True},
            {"title": "Book B", "author": "Author 2", "available": True},
            {"title": "Book C", "author": "Author 3", "available": True}
        ]
        self.borrowed_books = {}  # user -> list of borrowed books

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book["available"]:
                print(f"{book['title']} by {book['author']}")

    def borrow_book(self, user, title):
        for book in self.books:
            if book["title"] == title and book["available"]:
                book["available"] = False
                self.borrowed_books.setdefault(user, []).append(title)
                print(f"{user} borrowed {title}.")
                return
        print(f"Sorry, {title} is not available.")

    def return_book(self, user, title):
        if user in self.borrowed_books and title in self.borrowed_books[user]:
            self.borrowed_books[user].remove(title)
            for book in self.books:
                if book["title"] == title:
                    book["available"] = True
            print(f"{user} returned {title}.")
        else:
            print(f"{user} has not borrowed {title}.")

# Example usage
lib = Library()
lib.display_books()

lib.borrow_book("Priya", "Book A")
lib.display_books()

lib.return_book("Priya", "Book A")
lib.display_books()
