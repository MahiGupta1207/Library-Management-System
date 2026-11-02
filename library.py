
import pickle
import os
def add_book():
    f = open("library.dat", "ab")
    book_id = int(input("Enter Book ID: "))
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")
    book = [book_id, book_name, author]
    pickle.dump(book, f)
    f.close()
    print("Book added successfully!")
def display_books():
    if not os.path.exists("library.dat"):
        print("No books available!")
        return
    f = open("library.dat", "rb")
    while True:
        try:
            book = pickle.load(f)
            print("ID:", book[0])
            print("Name:", book[1])
            print("Author:", book[2])
            print("------------------")
        except EOFError:
            break
    f.close()
def search_book():
    search_id = int(input("Enter Book ID: "))
    found = False
    f = open("library.dat", "rb")
    while True:
        try:
            book = pickle.load(f)
            if book[0] == search_id:
                print("Book Found!")
                print("Name:", book[1])
                print("Author:", book[2])
                found = True
                break
        except EOFError:
            break
    f.close()
    if found == False:
        print("Book not found!")
def update_book():
    search_id = int(input("Enter Book ID to update: "))
    books = []
    found = False
    f = open("library.dat", "rb")
    while True:
        try:
            book = pickle.load(f)
            if book[0] == search_id:
                book[1] = input("Enter new Book Name: ")
                book[2] = input("Enter new Author Name: ")
                found = True
            books.append(book)
        except EOFError:
            break
    f.close()
    f = open("library.dat", "wb")
    for book in books:
        pickle.dump(book, f)
    f.close()
    if found:
        print("Book updated successfully!")
    else:
        print("Book not found!")
def delete_book():
    search_id = int(input("Enter Book ID to delete: "))
    books = []
    found = False
    f = open("library.dat", "rb")
    while True:
        try:
            book = pickle.load(f)
            if book[0] == search_id:
                found = True
            else:
                books.append(book)
        except EOFError:
            break
    f.close()
    f = open("library.dat", "wb")
    for book in books:
        pickle.dump(book, f)
    f.close()
    if found:
        print("Book deleted successfully!")
    else:
        print("Book not found!")
while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        display_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        update_book()
    elif choice == 5:
        delete_book()
    elif choice == 6:
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
