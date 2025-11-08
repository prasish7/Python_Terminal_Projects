import json

class RecipeBook:
    def __init__(self):
        self.recipes = []
    
    def add_recipes(self):
        recipe = input("Enter recipe")
        self.recipes.append({
            "Recipes":recipe
        })
        print(f"{recipe} added")

    def view_recipes(self):
        if not  self.recipes:
            print("Recepies Not found")
        else:
            for idx , item in enumerate(self.recipes , start = 1):
             print(f"{idx}. {item['Recipes']} ")

    def search_recipes(self):
        search = input("Enter  Recipes to Search ")
        for sear in self.recipes:
            if search == sear["Recipes"]:
                print(f"Your Searched Recipes is {sear['Recipes']}")
                break
        else:
            print("Invalid Recipes ")
    
    def remove_recipes(self):
        remove = input("Enter the Recipe you want to remove ")
        for rem in self.recipes:
            if remove == rem["Recipes"]:
                self.recipes.remove(rem)
                print(f"{remove} Recipe is removed")
                break
        else :
            print(" Recipe not found")

    def save_recipes(self,filename):
         with open("Recipe.json" , "w") as f:
             json.dump(self.recipes, f, indent = 4)
             
    def load_recipes(self, filename):
        try:
            with open(filename,"r") as f:
                self.recipes = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
         self.recipes = []
        print(" No saved Recipes found. Starting a new Recipe Book.")


def main():
    book = RecipeBook()
    book.load_recipes("Recipe.json")

    while True:
        print("Wellcome to Coking Recipes Book")
        print("1. Add Recipes ")
        print("2. View Recepies  ")
        print("3. Search Recepies  ")
        print("4. Remove Recipes  ")
        print("5. Save and Exit")
        choice = int(input("Enter Your Choice between 1-5: "))
        if choice == 1 :
            book.add_recipes()
        elif choice == 2 :
            book.view_recipes()
        elif choice == 3 :
            book.search_recipes()
        elif choice == 4 :
            book.remove_recipes()
        elif choice == 5 :
            book.save_recipes("Recipe.json")
            break
        else:
            print("Invalid Number, Please Check")

if __name__ == "__main__":
    main()

            