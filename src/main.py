from file_operations import load_recipe, save_recipe
from recipe_operations import RecipeManager

import pyfiglet
from rich import print

FILE_PATH = '../data/recipes.json'

def main():
    manager = RecipeManager() # Creates an instance of RecipeManager to manage recipes
    manager = load_recipe(FILE_PATH, manager) # Loads recipes from JSON file into manager

    while True:
            title = pyfiglet.figlet_format('RECIPE MANAGER', font='doom') # Styled title using pyfiglet
            print(f'[cornflower_blue]{title}[/]') # Styled display string using rich
            print("[#8190BB]1.[/] Add a recipe") 
            print("[#8190BB]2.[/] Select a recipe")
            print("[#8190BB]3.[/] Remove a recipe")
            print("[#8190BB]4.[/] Export a recipe")
            print("[#8190BB]5.[/] Exit")

            choice = input("\nChoose an option (1-5): ")

            if choice == '1':
                RecipeManager.add_recipe(manager) # Calls method to add a new recipe
                save_recipe(FILE_PATH, manager) # Saves updated recipes to JSON file
            elif choice == '2':
                RecipeManager.display_recipe(manager) # Calls method to display recipes
            elif choice == '3':
                RecipeManager.remove_recipe(manager) # Calls method to remove a recipe
                save_recipe(FILE_PATH, manager) # Saves updated recipes to JSON file
            elif choice == '4':
                RecipeManager.export_recipe(manager) # Calls method to export recipes
            elif choice == '5':
                print("\nExiting application.")
                break # Exits the while loop and ending the program
            else:
                print("[red3]\nInvalid choice. Please try again.[/]") # Emphasise error handling message in red using rich

if __name__ == "__main__":
    main() # Calls main function when script is executed directly