import os
from beaupy import confirm, select

class Recipe:
    def __init__(self, name, cuisine, ingredients, instructions):
        self.name = name
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeManager:
    def __init__(self):
        self.recipes = []

    # Method to import pre-saved recipes from JSON file
    def import_recipes_json(self, recipes_data):
        for recipe_data in recipes_data:
            recipe = Recipe(recipe_data['name'], recipe_data['cuisine'], recipe_data['ingredients'], recipe_data['instructions']) #
            self.recipes.append(recipe)

    # Method to add recipe
    def add_recipe(self):
        try:
            name = input("\nEnter recipe name: ").strip()
            cuisine = input("\nEnter cuisine: ").strip()
            ingredients = input("\nEnter ingredients (separate each ingredient with comma): ")
            ingredients_list = [] # Initialises empty list to store each ingredient as a separate item
            for ingredient in ingredients.split(","): # Splits ingredients into a list
                ingredients_list.append(ingredient.strip())
            instructions = input("\nEnter instructions (separate each step with enter, and type 'end' to finish): \n")
            instructions_list = [] # Initialises empty list to store each step as a separate item
            while instructions.strip().lower() != "end": # Allows users to add steps until "end" is entered
                instructions_list.append(instructions)
                instructions = input()
            recipe = Recipe(name, cuisine, ingredients_list, instructions_list) # Creates new Recipe object based on user input
            self.recipes.append(recipe) # Adds recipe
            print("\nRecipe successfully added.")

        except Exception as e:
            print(f"\nUnexpected error occurred: {e}.")
        
    # Method to display recipe
    def display_recipe(self):
        try:
            recipe_names = [recipe.name for recipe in self.recipes] # Pulls a list of saved recipes
            print("\nSelect recipe: ")
            recipe_name = select(recipe_names, cursor="🢧", cursor_style="#8190BB") # Displays list of available recipes via beaupy
            for recipe in self.recipes:
                if recipe.name.lower() == recipe_name.lower(): # Checks if entered recipe name matches a name in the recipe book, ignoring case-sensitivity
                    print(f"\nRecipe: {recipe.name}")
                    print(f"\nCuisine: {recipe.cuisine}")
                    print("\nIngredients: ")
                    for ingredient in recipe.ingredients: # Displays ingredients as a list
                        print("- " + ingredient)
                    print("\nInstructions: ")
                    for step, instruction in enumerate(recipe.instructions, 1): # Displays each step in sequential order
                        print(f"{step}. {instruction}")
            user_input = input("\nPress 'enter' to return to the main menu. ") # Prompt to return to main menu when user is ready
            if user_input == "":
                return

        except Exception as e:
            print(f"\nUnexpected error occurred: {e}.")
        
    # Method to remove recipe
    def remove_recipe(self):
        try:
            recipe_names = [recipe.name for recipe in self.recipes] # Pulls a list of saved recipes
            print("\nSelect recipe to remove: ")
            recipe_name = select(recipe_names, cursor="🢧", cursor_style="#8190BB") # Displays list of available recipes via beaupy
            if confirm(f"\nAre you sure you want to remove '{recipe_name}'?"): # Confirms if user wants to remove selected recipe via beaupy
                for recipe in self.recipes:
                    if recipe.name.lower() == recipe_name.lower(): # Checks if entered recipe name matches a name in the recipe book, ignoring case-sensitivity
                        self.recipes.remove(recipe) # Removes recipe
                print(f"\nRecipe '{recipe_name}' removed.")
            else:
                print("\Recipe removal cancelled.")
            return

        except Exception as e:
            print(f"\nUnexpected error occurred: {e}.")

    # Method to export recipe
    def export_recipe(self):
        try:
            recipe_name = input("\nEnter recipe name to export: ").strip().lower() # Removes whitespace and converts input to lowercase.
            for recipe in self.recipes:
                if recipe.name.lower() == recipe_name: # Checks if entered recipe name matches a name in the recipe book, ignoring case-sensitivity
                    txt_file = f"{recipe_name.replace(' ', '_')}.txt" # Generates file name based on recipe name
                    overwrite = True  # Assumes overwrite is necessary by default
                    if os.path.exists(txt_file): # Checks if recipe txt file already exists
                        overwrite = confirm(f"\n'{txt_file}' already exists. Do you want to overwrite it?") # Confirms if user wants to overwrite txt file via beaupy
                    if overwrite:
                        with open(txt_file, 'w') as file: # Creates txt file with specific layout
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
                        print("\nRecipe export cancelled.")
                    break
            else:
                print("\nRecipe not found.")

        except FileNotFoundError:
            print(f"\nFile not found. Please check if file exists.")
        except Exception as e:
            print(f"\nUnexpected error occurred: {e}.")