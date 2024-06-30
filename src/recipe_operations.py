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
        
        recipe = {"Recipe name": name, "Cuisine": cuisine, "Ingredients": ingredients_list, "Instructions": instructions_list}
        manager.add_recipe(recipe)
        print("Recipe successfully added.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}.")
