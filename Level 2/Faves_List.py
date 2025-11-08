import json

def add_item(faves_list, item):
    faves_list.append(item)

def remove_item(faves_list, item):
    faves_list.remove(item)

def view_item(faves_list):
    if not faves_list:
         print("Your faves list is empty.")
    else:
        for idx, item in enumerate(faves_list, start=1):
            print("\nFaves List Items:")
            print(f"{idx}. {item}")
    
def rate_item(faves_list, rate):
    if not faves_list:
         print("Your faves list is empty.")
    else:
        for idx, item in enumerate(faves_list, start=1):
            print("\nFaves List Items:")
            print(f"{idx}. {item}")

def comment_item(faves_list, comment):
    if not faves_list:
        print("Your faves list is empty.")
    else:
        for idx, item in enumerate(faves_list, start=1):
            print(f"{idx}. {item}")

def save_item(faves_list , file):
    with open("he.json", 'w') as f:
        json.dump(faves_list, f)

def load_item(file):
    with open("he.json", 'r') as f:
        return json.load(f)

def main():
 faves_list = []
 is_running = True
 while is_running:
     print("-----------------------------")
     print("Wellcome To Your Faves List")
     print("-----------------------------")
     print("Enter 1 To Add Faves")
     print("Enter 2 To Remove Faves Items")
     print("Enter 3 To View Faves Item")
     print("Enter 4 To Rate Faves")
     print("Enter 5 To Comment Faves Items")
     print("Enter 6 To Save Faves Item")
     print("Enter 7 To Exit")
     print("Enter 8 To Load Faves List Automatically")
     choice = int(input("Enter Number Between 1-8  "))

     if choice == 1 :
         list = input("Enter Faves To Add")
         add_item( faves_list, list)
         print("-----------------------------")
         print(f"{list} Added to faves_list")
         print("-----------------------------")
     elif choice == 2 :
         list = int(input("Enter The Item Number To Remove  "))
         if list in faves_list : 
             remove_item(faves_list, list)
             print("-----------------------------")
             print(f"{list} Removed From Faves List")
             print("-----------------------------")
         else:
             print("Please Check Your Number or There is No Item to Remove")
     elif choice == 3 :
         view_item(faves_list)
     elif choice == 4:
         
         rate  = int(input("Enter a Number Between 1-5 to Rate "))
         if rate == 1:
             print("⭐")
         elif  rate == 1:
             print("⭐⭐")
         elif rate == 2 :
             print("⭐⭐⭐")
         elif rate == 3 :
             print("⭐⭐⭐")
         elif rate == 4 :
             print("⭐⭐⭐⭐")
         elif rate == 5 :
             print("⭐⭐⭐⭐⭐")
         else :
             print("Invalid Number ,  Please Choose Again")
         rate_item(faves_list, rate)
     elif choice == 5 : 
         comment = input("Enter Comment")
         comment_item(faves_list, comment)
         print("-----------------------------")
         print(f"Your Comment is {comment}")
         print("-----------------------------")
     elif choice == 6:
         save_item(faves_list , "he.json")
         print("Faves List Saved")
     elif choice == 7 :
         is_running = False
         print("Exiting Faves List App. Goodbye!")
     elif choice == 8:
         faves_list = load_item("he.json")
         print("-----------------------------")
         print(faves_list)
         print("Faves List Loaded")
         print("-----------------------------")
     else : 
         print("Invalid Input , Please Check Your Input")

if __name__ == "__main__":
    main()

    

         
         
         

            
    
        
         
    
