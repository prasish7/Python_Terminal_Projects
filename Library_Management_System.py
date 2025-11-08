import json
import datetime

class LibraryManagementSystem:
    def __init__(self):
        self.book = []
        self.member = []
        


    def add_book(self):
        book = input("Enter The Title of the book you want to add : ")
        author = input("Enter The Author Name : ")
        self.book.append({
            "Title":book,
            "Name": author
                        })
        
        print(f"{book} written by {author} is added to libary")

    def view_book(self):
        if not self.book:
            print("No books available in the library.")
            return
        print("\n--- Available Books ---")
        for idx, item in enumerate(self.book, start=1):
            print(f"{idx}. {item['Title']} by {item['Name']}")

    def remove_book(self):
        search = input("Enter the Title or Author to remove the book: ").lower()
        found = False
        for item in self.book[:]:
            if item['Title'].lower() == search or item['Name'].lower() == search:
                self.book.remove(item)
                print(f"{item['Title']} by {item['Name']} is removed from the library.")
                found = True
        if not found:
            print("No matching book found.")
    
    def borrowed_book(self):
       borrow = input("Enter Title or Author of the book you want to borrow : ").lower()
       found = False
       for item in self.book[:]:
            if item['Title'].lower() == borrow or item['Name'].lower() == borrow:
                self.member.append(item)
                self.book.remove(item)
                print(f"{item['Title']} by {item['Name']} is has been borrowed from the library.")
                found = True
                break
       if not found:
             print("No matching book found.")

    def return_book(self):
       re_turn = input("Enter the Title or Author of the book you want to return : ").lower()
       found = False
       for item in self.member[:]:
            if item['Title'].lower() == re_turn or item['Name'].lower() == re_turn:
                self.member.remove(item)
                self.book.append(item)
                print(f"{item['Title']} by {item['Name']} has been returned to the library.")
                found = True
                break
       if not found:
             print("No matching book found.")


    def save_library(self, filename):
      data = {
        "books": self.book,
        "borrowed": self.member
    }
      with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

    def load_library(self, filename):
     try:
        with open(filename, 'r') as f:
            data = json.load(f)
            self.book = data.get("books", [])
            self.member = data.get("borrowed", [])
     except (FileNotFoundError, json.JSONDecodeError):
        self.book = []
        self.member = []


def main():
    library = LibraryManagementSystem()
    library.load_library("library_data.json")

    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Save & Exit")
        choice = int(input("Enter your choice (1-6): "))

        if choice == 1:
            library.add_book()
        elif choice == 2:
            library.view_book()
        elif choice == 3:
            library.remove_book()
        elif choice == 4:
            library.borrowed_book()
        elif choice == 5:
            library.return_book()
        elif choice == 6:
            library.save_library("library_data.json")
            print("Library data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

   
