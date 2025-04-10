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


# Base class - Vehicle
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass - Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Subclass - Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Subclass - Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Function to prompt the user for input and create the appropriate vehicle
def create_vehicle():
    print("Choose a vehicle to create:")
    print("1. Car")
    print("2. Plane")
    print("3. Boat")

    choice = int(input("Enter the number of your choice: "))

    if choice == 1:
        return Car()
    elif choice == 2:
        return Plane()
    elif choice == 3:
        return Boat()
    else:
        print("Invalid choice. Defaulting to Car.")
        return Car()  # Default to Car if invalid choice

# Main program
vehicle = create_vehicle()  # Create the vehicle based on user input
vehicle.move()  # Call the move method, which behaves differently based on the vehicle

