from file_operations import load_recipe, save_recipe
from recipe_operations import RecipeManager

import pyfiglet
from rich import print

FILE_PATH = '../data/recipes.json'

def main():
    manager = RecipeManager()

    manager = load_recipe(FILE_PATH, manager)

    while True:
            title = pyfiglet.figlet_format('RECIPE MANAGER', font='doom')
            print(f'[cornflower_blue]{title}[/]')
            print("[#8190BB]1.[/] Add a recipe")
            print("[#8190BB]2.[/] Select a recipe")
            print("[#8190BB]3.[/] Remove a recipe")
            print("[#8190BB]4.[/] Export a recipe")
            print("[#8190BB]5.[/] Exit")

            choice = input("\nChoose an option: ")

            if choice == '1':
                RecipeManager.add_recipe(manager)
                save_recipe(FILE_PATH, manager)
            elif choice == '2':
                RecipeManager.display_recipe(manager)
            elif choice == '3':
                RecipeManager.remove_recipe(manager)
                save_recipe(FILE_PATH, manager)
            elif choice == '4':
                RecipeManager.export_recipe(manager)
            elif choice == '5':
                print("\nExiting application.")
                break
            else:
                print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()