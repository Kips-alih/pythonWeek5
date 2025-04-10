# Book Class
class Book:
    def __init__(self, title, author, genre, pages):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.current_page = 0

    def read(self, pages_to_read):
        """Simulates reading the book, moves the current page forward."""
        if self.current_page + pages_to_read > self.pages:
            self.current_page = self.pages
            print(f"You've finished reading {self.title}!")
        else:
            self.current_page += pages_to_read
            print(f"You've read {self.current_page} out of {self.pages} pages.")

    def display_info(self):
        """Displays the details of the book."""
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Total Pages: {self.pages}")

    def is_finished(self):
        """Checks if the book is finished."""
        if self.current_page == self.pages:
            return True
        return False


# User input for book details
title = input("Enter the book title: ")
author = input("Enter the author of the book: ")
genre = input("Enter the genre of the book: ")
pages = int(input("Enter the total number of pages in the book: "))

# Create a Book instance with user input
my_book = Book(title, author, genre, pages)

# Display book info
my_book.display_info()

# Allow the user to read pages
while not my_book.is_finished():
    pages_to_read = int(input(f"How many pages would you like to read? (Currently on page {my_book.current_page}): "))
    my_book.read(pages_to_read)

# Final message when the book is finished
if my_book.is_finished():
    print("You have finished reading the book!")
