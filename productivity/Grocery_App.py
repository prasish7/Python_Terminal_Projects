import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "Grocery_List.json"

def add_item(grocery_list, item):
    grocery_list.append(item)

def remove_item(grocery_list, item):
    grocery_list.remove(item)

def mark_purchased(grocery_list, item):
    index = grocery_list.index(item)
    grocery_list[index] = f"{item} (purchased)"
def mark_unpurchased(grocery_list, item):
    index = grocery_list.index(item)
    grocery_list[index] = item.replace(" (purchased)", "")

def save_list(grocery_list, filename):
    with open(DATA_FILE, 'w') as f:
        json.dump(grocery_list, f)

def load_list(filename):
    with open(DATA_FILE, 'r') as f:
        return json.load(f)
    
def display_list(grocery_list):
    if not grocery_list:
        print("Your grocery list is empty.")
    else:
        print("Your Grocery List:")
        for idx, item in enumerate(grocery_list, start=1):
            print(f"{idx}. {item}")

def main():
    grocery_list = []
    is_running = True

    while is_running:
        print("\nGrocery List Menu:")
        print("1. View Grocery List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Mark Item as Purchased")
        print("5. Mark Item as Unpurchased")
        print("6. Save Grocery List")
        print("7. Load Grocery List")
        print("8. Exit")
        choice = int(input("Select an option (1-8): "))

        if choice == 1:
            display_list(grocery_list)
        elif choice == 2:
            item = input("Enter the item to add: ")
            add_item(grocery_list, item)
            print(f'Item "{item}" added to the grocery list.')
        elif choice == 3:
            item = input("Enter the item to remove: ")
            if item in grocery_list:
                remove_item(grocery_list, item)
                print(f'Item "{item}" removed from the grocery list.')
            else:
                print(f'Item "{item}" not found in the grocery list.')
        elif choice == 4:
            item = input("Enter the item to mark as purchased: ")
            if item in grocery_list:
                mark_purchased(grocery_list, item)
                print(f'Item "{item}" marked as purchased.')
            else:
                print(f'Item "{item}" not found in the grocery list.')
        elif choice == 5:
            item = input("Enter the item to mark as unpurchased: ")
            if f"{item} (purchased)" in grocery_list:
                mark_unpurchased(grocery_list, item)
                print(f'Item "{item}" marked as unpurchased.')
            else:
                print(f'Item "{item}" not found in the grocery list or is not marked as purchased.')
        elif choice == 6:
            save_list(grocery_list, DATA_FILE)
            print("Grocery list saved.")
        elif choice == 7:
            grocery_list = load_list(DATA_FILE)
            print("Grocery list loaded.")
        elif choice == 8:
            is_running = False
            print("Exiting Grocery App. Goodbye!")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

