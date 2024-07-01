class Recipe:
    def __init__(self, name, cuisine, ingredients, instructions):
        self.name = name
        self.cuisine = cuisine
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeManager:
    def __init__(self):
        self.recipes = []
    
    # Method to add recipe
    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    # Method to display recipe
    def display_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                print(f"Recipe: {recipe.name}")
                print("Ingredients: ")
                for ingredient in recipe.ingredients:
                    print("- " + ingredient)
                print("Instructions: ")
                for step, instruction in enumerate(recipe.instructions, 1):
                    print(f"{step}. {instruction}")
                return
        print(f"Recipe not found.")

    # Method to remove recipe
    def remove_recipe(self, recipe_name):
        for recipe in self.recipes:
            if recipe.name.lower() == recipe_name.lower():
                self.recipes.remove(recipe)
                print(f"Recipe '{recipe_name}' removed.")
                return
        print(f"Recipe not found.")

    # Method to export recipe
    def export_recipe(self, recipe_name, txt_file):
        with open(txt_file, 'w') as file:
            for recipe in self.recipes:
                if recipe.name.lower() == recipe_name.lower():
                    file.write(f"Recipe: {recipe.name}\n")
                    file.write("Ingredients:\n")
                    for ingredient in recipe.ingredients:
                        file.write(f"- {ingredient}\n")
                    file.write("Instructions:\n")
                    for step, instruction in enumerate(recipe.instructions, 1):
                        file.write(f"{step}. {instruction}\n")
                    print(f"Recipe '{recipe_name}' exported to {txt_file}.")
                    return
            print(f"Recipe not found.")

# Creating object instance for class RecipeManager
manager = RecipeManager()

# Function to add recipe
def add_recipe(manager):
    try:
        name = input("Enter recipe name: ")
        cuisine = input("Enter cuisine: ")
        ingredients = input("Enter ingredients (separate each ingredient with comma): ")
        ingredients_list = []        
        instructions = input("Enter instructions (separate each step with enter. type 'end' to finish.): ")
        instructions_list = []

        for ingredient in ingredients.split(","):
            ingredients_list.append(ingredient.strip())
        
        while instructions.strip().lower() != "end":
            instructions_list.append(instructions.strip())
            instructions = input()
        
        recipe = Recipe(name, cuisine, ingredients_list, instructions_list)
        manager.add_recipe(recipe)
        print("Recipe successfully added.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")

# Function to display recipe
def display_recipe(manager):
    try:
        recipe_name = input("Select recipe: ")
        manager.display_recipe(recipe_name)
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")

# Function to remove recipe
def remove_recipe(manager):
    try:
        recipe_name = input("Enter recipe name to remove: ")
        manager.remove_recipe(recipe_name)
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")

# Function to export recipe
def export_recipe(manager):
    try:
        recipe_name = input("Enter recipe name to export: ")
        txt_file = input("Enter name for txt file (e.g. 'recipe.txt'): ")
        manager.export_recipe(recipe_name, txt_file)
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")