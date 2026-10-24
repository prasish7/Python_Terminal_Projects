import requests
import random
import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent / "pokedex.json"

class Pokemon():
    def __init__(self, name, id, type, abilities, stats, height , weight, sprite_url):
        self.name = name
        self.id = id
        self.type = type
        self.abilities = abilities
        self.stats = stats
        self.height = height
        self.weight = weight
        self.sprite_url = sprite_url

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.id}")
        print(f"Type: {', '.join(self.type)}")
        print(f"Abilities: {', '.join(self.abilities)}")
        print("Stats:")
        for stat, value in self.stats.items():
            print(f"  {stat}: {value}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"Sprite URL: {self.sprite_url}")

class Pokedex():
    def __init__(self):
        self.pokemon_list = []

    def add_pokemon(self, pokemon):
        self.pokemon_list.append(pokemon)

    def search_pokemon(self, identifier):
        url = f"https://pokeapi.co/api/v2/pokemon/{identifier.lower()}"
        print("Searching for Pokemon...")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data['name']
            id = data['id']
            type = [t['type']['name'] for t in data['types']]
            abilities = [a['ability']['name'] for a in data['abilities']]
            stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
            height = data['height']
            weight = data['weight']
            sprite_url = data['sprites']['front_default']
            pokemon = Pokemon(name, id, type, abilities, stats, height, weight, sprite_url)
            self.add_pokemon(pokemon)
            print("Pokemon found:")
            pokemon.display_info()
        else:
            print("Pokemon not found. Please check the name or ID and try again.")
    def random_pokemon(self):
        identifier = random.randint(1, 1010)
        url = f"https://pokeapi.co/api/v2/pokemon/{identifier}"
        print("Randomizing for Pokemon...")
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            name = data['name']
            id = data['id']
            type = [t['type']['name'] for t in data['types']]
            abilities = [a['ability']['name'] for a in data['abilities']]
            stats = {s['stat']['name']: s['base_stat'] for s in data['stats']}
            height = data['height']
            weight = data['weight']
            sprite_url = data['sprites']['front_default']
            pokemon = Pokemon(name, id, type, abilities, stats, height, weight, sprite_url)
            self.add_pokemon(pokemon)
            print("Pokemon found:")
            pokemon.display_info()
        else:
            print("Pokemon not found. Please try again.")
    
    def save_pokedex(self, filename):
        with open(filename, 'w') as f:
            json.dump([pokemon.__dict__ for pokemon in self.pokemon_list], f, indent=4)
        
    def load_pokedex(self, filename):
        try:
            with open(filename, 'r') as f:
                pokemon_data = json.load(f)
                for pdata in pokemon_data:
                    pokemon = Pokemon(
                        pdata['name'],
                        pdata['id'],
                        pdata['type'],
                        pdata['abilities'],
                        pdata['stats'],
                        pdata['height'],
                        pdata['weight'],
                        pdata['sprite_url']
                    )
                    self.add_pokemon(pokemon)
        except (FileNotFoundError, json.JSONDecodeError):
            self.pokemon_list = []
            print("No saved Pokedex found. Starting a new Pokedex.")
            
def main():
    pokedex = Pokedex()
    pokedex.load_pokedex(DATA_FILE)
    while True:
        print("Welcome to the Pokedex")
        print("1. Search Pokemon by Name/ID")
        print("2. Get Random Pokemon")
        print("3. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            identifier = input("Enter Pokemon Name or ID: ")
            pokedex.search_pokemon(identifier)
        elif choice == '2':
            pokedex.random_pokemon()
        elif choice == '3':
            pokedex.save_pokedex(DATA_FILE)
            print("Exiting Pokedex. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





    



    


        