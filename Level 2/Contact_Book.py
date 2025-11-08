import json

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter your name: ")
        phone = input("Enter your phone number: ")
        self.contacts.append({
            "Name": name,
            "Phone": phone
        })
        print(f"✅ Contact '{name}' added successfully!")
    
    def view_contact(self):
        if not self.contacts:
            print("There are no contacts in your book.")
        else:
            print("\nContact List Items:")
            for idx, item in enumerate(self.contacts, start=1):
                print(f"{idx}. Name: {item['Name']} , Phone: {item['Phone']}")

    def remove_contact(self):
       remove = input("Enter the Name or Phone to remove contact : ")
       for contact in self.contacts:
          if remove == contact["Name"] or remove == contact["Phone"]:
             self.contacts.remove(contact)
             print(f"{remove} contact is removed")
             break
       else:
            print(" Contact not found in your book.")   

    def search_contact(self):
       search = input("Enter the contact you want to Search: ")
       for contact in self.contacts:
           if search == contact["Name"] or search == contact["Phone"]:
               print(f"Contact Found: Name: {contact['Name']} , Phone: {contact['Phone']}")
               break
       else:
           print(" Contact not found in your book.")

    def save_contact(self,filename ):
       with open("contact.json","w" ) as f:
          json.dump(self.contacts, f , indent=4)
     
    def load_contact(self):
       try:
        with open("contact.json", "r") as f:
          self.contacts = json.load(f)
       except (FileNotFoundError, json.JSONDecodeError):
        self.contacts = []
        print("⚠️ No saved contacts found. Starting a new book.")

def main():
    contact = ContactBook()
    contact.load_contact()

    while True:
            print("Welcome To Contact Book")
            print("1. Add Contact")
            print("2. View Contact")
            print("3. Remove Contact")
            print("4. Search Contact")
            print("5. Save and Exit")
            choice = int(input("Enter between 1-5 :  "))
            if choice == 1 :
               contact.add_contact()
            elif choice == 2 :
               contact.view_contact()
            elif choice == 3 :
               contact.remove_contact()
            elif choice == 4 :
               contact.search_contact()
            elif choice == 5 :
               contact.save_contact("contact.json")
               print("Contact Saving")
               break
            else:
               print("Invalid Number")

if __name__ == "__main__":
    main()
               




          
          
    

