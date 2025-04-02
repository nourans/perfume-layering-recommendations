import os
import json

DATA_PATH = "data/perfume_input.json"

def load_perfumes():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_perfumes(perfumes):
    with open(DATA_PATH, "w") as file:
        json.dump(perfumes, file, indent=4)

def display_menu():
    print("\nPerfume Layering CLI: Main Menu: ")
    print("1. Add Perfume")
    print("2. Display Perfumes")
    print("3. Remove Perfume")
    print("4. Exit")


def main():
    perfumes = load_perfumes()

    while True:
        display_menu()

        choice = input("Choose an action: ").strip()

        if choice == "1":
            name = input("Enter perfume name: ").strip()
            brand = input("Enter perfume brand: ").strip() # might use it at a later stage
            fullname = brand + " " + name
            if name not in perfumes:
                perfumes.append(fullname)
                save_perfumes(perfumes)
                print(f"Successfully Added: {name} by {brand}")
            else:
                print("Perfume already exists in your list")
        
        elif choice == "2":
            print("\nYour Perfume Collection:")
            if len(perfumes) == 0:
                print("no perfumes here, loser :p")
            for i, p in enumerate(perfumes, 1):
                print(f"{i}. {p}")

        elif choice == "3":
            print("Select a perfume to remove: ")
            for i, p in enumerate(perfumes):
                print(f"{i+1}. {p}")
            try:
                index = int(input("Enter number or 0 to go back to main menu: ")) - 1
                if index < len(perfumes):
                    removed = perfumes.pop(index)
                    save_perfumes(perfumes)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid index :(")

            except ValueError:
                print("oops. invalid entry")
        elif choice == "4":
            break
        else:
            print("invalid option!")

if __name__ == "__main__":
    main()

            



