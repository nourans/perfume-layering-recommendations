"""running the recommendations app"""
import os
import json
from gpt_recs import get_layering_recs
from gpt_recs import save_notes_to_file, parse_json_string
from split import get_recs, get_analysis
from utils import load_perfumes, save_perfumes

def display_menu():
    print("\nPerfume Layering CLI: Main Menu: ")
    print("1. Add Perfume")
    print("2. Remove Perfume")
    print("3. Display Perfume Collection")
    print("4. Get Layering Recommendations")
    print("5. Analyze Your Perfume Collection")
    print("6. Save Perfume Notes")
    print("7. Exit")


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
            print("Fetching notes as JSON from ChatGPT...")
            raw = get_layering_recs()
            parsed = parse_json_string(raw)
            save_notes_to_file(parsed)
            print("The notes of you perfume collection have been saved")
            
        elif choice == "7":
            print("Thank you for using the Perfume Layering Recommendation System. Happy sniffing!👃")
            break

        else:
            print("invalid option!")

if __name__ == "__main__":
    main()

            



