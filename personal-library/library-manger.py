import json
import os

data_file= 'library.text'

def load_library():
    if os.path.exists(data_file):
        with open(data_file, 'r') as file:
            return json.load(file)
    else:
        return []
def save_library(library):
    with open(data_file, 'w') as file:
        json.dump(library, file)

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    year = input("Enter book publication year: ")
    library.append({"title": title, "author": author, "year": year})
    genre= input("Enter book genre: ")
    read= input("Have you read this book? (yes/no): ").lower() == 'yes'
    new_book= {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    save_library(library)
    print(f"Book '{title}' added to the library.")
def remove_book(library):
        title = input("Enter the title of the book to remove: ")
        for book in library:
            if book['title'].lower() == title.lower():
                library.remove(book)
                save_library(library)
                print(f"Book '{title}' removed from the library.")
                return
        print(f"Book '{title}' not found in the library.")

def search_book(library):
    title = input("Enter the title of the book to search: ")
    for book in library:
        if book['title'].lower() == title.lower():
            print(f"Book found: {book}")
            return
    print(f"Book '{title}' not found in the library.") 

def display_books(library):
    if not library:
        print("No books in the library.")
    else:
        for book in library:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Genre: {book['genre']}, Read: {'Yes' if book['read'] else 'No'}")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    unread_books = total_books - read_books
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Books unread: {unread_books}")
    print(f"Percentage of books read: {percentage_read:.2f}%")
def main():
    library = load_library()
    while True:
        print("\nLibrary Manager")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_books(library)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()