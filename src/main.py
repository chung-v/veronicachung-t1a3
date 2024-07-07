from file_operations import load_recipe, save_recipe
from recipe_operations import RecipeManager
import pyfiglet
from rich import print

FILE_PATH = '../data/recipes.json'

def main():
    # Creates an instance of RecipeManager to manage recipes
    manager = RecipeManager()
    # Loads recipes from JSON file into manager
    manager = load_recipe(FILE_PATH, manager)

    while True:
            # Styled title using pyfiglet
            title = pyfiglet.figlet_format('RECIPE MANAGER', font='doom')
            # Styled display string using rich
            print(f'[cornflower_blue]{title}[/]')
            print("[#8190BB]1.[/] Add a recipe")
            print("[#8190BB]2.[/] Select a recipe")
            print("[#8190BB]3.[/] Remove a recipe")
            print("[#8190BB]4.[/] Export a recipe")
            print("[#8190BB]5.[/] Exit")

            choice = input("\nChoose an option (1-5): ")

            if choice == '1':
                # Calls method to add a new recipe
                RecipeManager.add_recipe(manager)
                # Saves updated recipes to JSON file
                save_recipe(FILE_PATH, manager)
            elif choice == '2':
                # Calls method to display recipes
                RecipeManager.display_recipe(manager)
            elif choice == '3':
                # Calls method to remove a recipe
                RecipeManager.remove_recipe(manager)
                # Saves updated recipes to JSON file
                save_recipe(FILE_PATH, manager)
            elif choice == '4':
                # Calls method to export recipes
                RecipeManager.export_recipe(manager)
            elif choice == '5':
                print("\nExiting application.")
                break # Exits the while loop and ending the program
            else:
                # Emphasise error handling message in red using rich
                print("[red3]\nInvalid choice. Please try again.[/]")

# Calls main function when script is executed directly
if __name__ == "__main__":
    main()