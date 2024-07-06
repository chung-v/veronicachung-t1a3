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
            recipe = Recipe(recipe_data['name'], recipe_data['cuisine'], recipe_data['ingredients'], recipe_data['instructions'])
            self.add_recipe(recipe)

    # Method to add recipe
    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    # Method to display recipe
    def display_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                print(f"\nRecipe: {recipe.name}")
                print("\nIngredients: ")
                for ingredient in recipe.ingredients:
                    print("- " + ingredient)
                print("\nInstructions: ")
                for step, instruction in enumerate(recipe.instructions, 1):
                    print(f"{step}. {instruction}")
                return
        print(f"\nRecipe not found.")

    # Method to remove recipe
    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                self.recipes.remove(recipe)
                print(f"\nRecipe '{recipe_name}' removed.")
                return
        print(f"\nRecipe not found.")

    # Method to export recipe
    def export_recipe(self, recipe_name, txt_file):
        with open(txt_file, 'w') as file:
            for recipe in self.recipes:
                if recipe.name.lower() == recipe_name.lower():
                    file.write(f"Recipe: {recipe.name}\n")
                    file.write("\nIngredients:\n")
                    for ingredient in recipe.ingredients:
                        file.write(f"- {ingredient}\n")
                    file.write("\nInstructions:\n")
                    for step, instruction in enumerate(recipe.instructions, 1):
                        file.write(f"{step}. {instruction}\n")
                    print(f"\nRecipe '{recipe_name}' exported to {txt_file}.")
                    return
            print(f"\nRecipe not found.")

# Creating object instance for class RecipeManager
manager = RecipeManager()

# Function to add recipe
def add_recipe(manager):
    try:
        name = input("\nEnter recipe name: ")
        cuisine = input("\nEnter cuisine: ")
        ingredients = input("\nEnter ingredients (separate each ingredient with comma): ")
        ingredients_list = []        
        instructions = input("\nEnter instructions (separate each step with enter. type 'end' to finish.): ")
        instructions_list = []

        for ingredient in ingredients.split(","):
            ingredients_list.append(ingredient.strip())
        
        while instructions.strip().lower() != "end":
            instructions_list.append(instructions.strip())
            instructions = input()
        
        recipe = Recipe(name, cuisine, ingredients_list, instructions_list)
        manager.add_recipe(recipe)
        print("\nRecipe successfully added.")
    except Exception as e:
        print(f"\n Unexpected error occurred: {e}.")

# Function to display recipe
def display_recipe(manager):
    try:
        recipe_name = input("\nSelect recipe: ")
        manager.display_recipe(recipe_name)
    except Exception as e:
        print(f"\n Unexpected error occurred: {e}.")

# Function to remove recipe
def remove_recipe(manager):
    try:
        recipe_name = input("\nEnter recipe name to remove: ")
        manager.remove_recipe(recipe_name)
    except Exception as e:
        print(f"\n Unexpected error occurred: {e}.")

# Function to export recipe
def export_recipe(manager):
    try:
        recipe_name = input("\nEnter recipe name to export: ")
        txt_file = input("\nEnter name for txt file (e.g. 'recipe.txt'): ")
        manager.export_recipe(recipe_name, txt_file)
    except Exception as e:
        print(f"\n Unexpected error occurred: {e}.")