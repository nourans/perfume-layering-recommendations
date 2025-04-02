import os
import json
from gpt_notes import get_layering_recs

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


def get_recs():
    gpt_output = get_layering_recs()
    output_list = gpt_notes.split("### Taste Analysis")
    return output_list[0]

def get_analysis():
    gpt_output = get_layering_recs()
    output_list = gpt_notes.split("### Taste Analysis")
    return output_list[1]

def display_menu():
    print("\nPerfume Layering CLI: Main Menu: ")
    print("1. Add Perfume")
    print("2. Remove Perfume")
    print("3. Display Perfume Collection")
    print("4. Get perfume Recommendations")
    print("5. Analyze Your Perfume Collection")
    print("6. Exit")



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

        elif choice == "3":
            print("\nYour Perfume Collection:")
            if len(perfumes) == 0:
                print("no perfumes here, loser :p")
            for i, p in enumerate(perfumes, 1):
                print(f"{i}. {p}")

        elif choice == "4":
            print("Fetching layering recommendations...")
            layering_recs = get_recs()
            print("❣️ Layering Combos for Your Collection ❣️")
            print(layering_recs)

        elif choice == "5":
            print("Analyzing your collection...")
            analysis = get_analysis()
            print("❣️ Here is what you like ❣️")
            print(analysis)

        elif choice == "6":
            break
        else:
            print("invalid option!")

if __name__ == "__main__":
    main()

            



