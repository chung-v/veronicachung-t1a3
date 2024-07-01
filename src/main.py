from file_operations import load_recipe, save_recipe
from recipe_operations import add_recipe, display_recipe, remove_recipe, export_recipe

FILE_PATH = '../data/recipes.json'

def main():
    manager = load_recipe(FILE_PATH)

    while True:
            print("\nRecipe Manager:\n")
            print("1. Add a recipe")
            print("2. Select a recipe")
            print("3. Remove a recipe")
            print("4. Export a recipe")
            print("5. Exit")

            choice = input("\nChoose an option: ")

            if choice == '1':
                add_recipe(manager)
                save_recipe(FILE_PATH, manager)
            elif choice == '2':
                display_recipe(manager)
            elif choice == '3':
                remove_recipe(manager)
                save_recipe(FILE_PATH, manager)
            elif choice == '4':
                export_recipe(manager)
            elif choice == '5':
                print("Exiting application.")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()