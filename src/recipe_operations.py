import os
from beaupy import confirm, select
from rich import print

# Class to store recipe attributes
class Recipe:
    def __init__(self, name, cuisine, ingredients, instructions):
        self.name = name
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.instructions = instructions

# Class to manage a collection of recipes
class RecipeManager:
    def __init__(self):
        # Initialises empty list to store Recipe objects
        self.recipes = []

    # Method to add recipe
    def add_recipe(self):
        try:
            name = input("\nEnter recipe name: ").strip()
            cuisine = input("\nEnter cuisine: ").strip()
            ingredients = input("\nEnter ingredients (separate each ingredient with comma): ")
            # Initialises empty list to store each ingredient as a separate item
            ingredients_list = []
            # Splits ingredients into a list
            for ingredient in ingredients.split(","):
                ingredients_list.append(ingredient.strip())
            instructions = input("\nEnter instructions (separate each step with enter, and type 'end' to finish): \n")
            # Initialises empty list to store each step as a separate item
            instructions_list = []
            # Allows users to add steps until "end" is entered
            while instructions.strip().lower() != "end":
                instructions_list.append(instructions)
                instructions = input()
            # Creates new Recipe object based on user input
            recipe = Recipe(name, cuisine, ingredients_list, instructions_list)
            self.recipes.append(recipe)
            print("\nRecipe successfully added.")
        # Emphasise error handling message in red using rich
        except Exception as e:
            print(f"[red3]\nUnexpected error occurred: {e}.[/]")
        
    # Method to display recipe
    def display_recipe(self):
        try:
            # Pulls a list of saved recipes
            recipe_names = [recipe.name for recipe in self.recipes] 
            print("\nSelect recipe: ")
            # Displays list of available recipes via beaupy
            recipe_name = select(recipe_names, cursor="🢧", cursor_style="#8190BB")
            for recipe in self.recipes:
                # Checks if entered recipe name matches a name in the recipe book, ignoring case-sensitivity
                if recipe.name.lower() == recipe_name.lower():
                    print(f"\nRecipe: {recipe.name}")
                    print(f"\nCuisine: {recipe.cuisine}")
                    print("\nIngredients: ")
                    # Displays ingredients as a list
                    for ingredient in recipe.ingredients:
                        print("- " + ingredient)
                    print("\nInstructions: ")
                    # Displays each step in sequential order
                    for step, instruction in enumerate(recipe.instructions, 1):
                        print(f"{step}. {instruction}")
            # Prompt to return to main menu when user is ready
            user_input = input("\nPress 'enter' to return to the main menu. ")
            if user_input == "":
                return
        # Emphasise error handling message in red using rich
        except Exception as e:
            print(f"[red3]\nUnexpected error occurred: {e}.[/]")
        
    # Method to remove recipe
    def remove_recipe(self):
        try:
            # Pulls a list of saved recipes
            recipe_names = [recipe.name for recipe in self.recipes]
            print("\nSelect recipe to remove: ")
            # Displays list of available recipes via beaupy
            recipe_name = select(recipe_names, cursor="🢧", cursor_style="#8190BB")
            # Confirms if user wants to remove selected recipe via beaupy
            if confirm(f"\nAre you sure you want to remove '{recipe_name}'?"):
                for recipe in self.recipes:
                    # Checks if entered recipe name matches a name in the recipe book, ignoring case-sensitivity
                    if recipe.name.lower() == recipe_name.lower():
                        self.recipes.remove(recipe)
                print(f"\nRecipe '{recipe_name}' removed.")
            else:
                # Emphasise error handling message in red using rich
                print("[red3]\Recipe removal cancelled.[/]")
            return
        # Emphasise error handling message in red using rich
        except Exception as e:
            print(f"[red3]\nUnexpected error occurred: {e}.[/]")

    # Method to export recipe
    def export_recipe(self):
        try:
            # Removes whitespace and converts input to lowercase.
            recipe_name = input("\nEnter recipe name to export: ").strip().lower()
            for recipe in self.recipes:
                # Checks if entered recipe name matches a name in the recipe book, ignoring case-sensitivity
                if recipe.name.lower() == recipe_name:
                    # Generates file name based on recipe name
                    txt_file = f"{recipe_name.replace(' ', '_')}.txt"
                    # Assumes overwrite is necessary by default
                    overwrite = True
                    # Checks if recipe txt file already exists
                    if os.path.exists(txt_file):
                        # Confirms if user wants to overwrite txt file via beaupy
                        overwrite = confirm(f"\n'{txt_file}' already exists. Do you want to overwrite it?")
                    if overwrite:
                        # Creates txt file with specific layout
                        with open(txt_file, 'w') as file:
                            file.write(f"Recipe: {recipe.name}\n")
                            file.write(f"\nCuisine: {recipe.cuisine}\n")
                            file.write("\nIngredients:\n")
                            for ingredient in recipe.ingredients:
                                file.write(f"- {ingredient}\n")
                            file.write("\nInstructions:\n")
                            for step, instruction in enumerate(recipe.instructions, 1):
                                file.write(f"{step}. {instruction}\n")
                        print(f"\nRecipe '{recipe_name}' exported to {txt_file}.")
                    else:
                        # Emphasise error handling message in red using rich
                        print("[red3]\nRecipe export cancelled.[/]")
                    break
            else:
                print("[red3]\nRecipe not found.[/]")
        # Emphasise error handling message in red using rich
        except FileNotFoundError:
            print(f"[red3]\nFile not found. Please check if file exists.[/]")
        except Exception as e:
            print(f"[red3]\nUnexpected error occurred: {e}.[/]")