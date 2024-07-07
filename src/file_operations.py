import json
from recipe_operations import Recipe

# Function to import pre-saved recipes from JSON file.
def load_recipe(file_path, manager):
    try:
        with open(file_path, 'r') as file: # Loads JSON data from the file into recipes_data list
            recipes_data = json.load(file)
            for recipe_data in recipes_data:
                recipe = Recipe(recipe_data['name'], recipe_data['cuisine'], recipe_data['ingredients'], recipe_data['instructions']) # Creates a Recipe object using data from JSON
                manager.recipes.append(recipe) # Adds the created recipe object to manager's recipes list
        return manager
    # Error handling
    except FileNotFoundError: 
        print(f"\nFile not found. Please check if file exists.")
        return []
    except PermissionError:
        print(f"\nPermission denied to read file.")
        return []
    except json.JSONDecodeError:
        print(f"\nError decoding JSON from file.")
        return []
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}.")
        return []

# Function to export recipe updates to JSON file
def save_recipe(file_path, manager):
    try:
        recipes_data = []
        for recipe in manager.recipes: 
            recipe_data = { # Creates a dictionary representing each recipe's data
                'name': recipe.name,
                'cuisine': recipe.cuisine,
                'ingredients': recipe.ingredients,
                'instructions': recipe.instructions
            }
            recipes_data.append(recipe_data) # Appends the recipe data dictionary to recipes_data list
        with open(file_path, 'w') as file: # Write recipes_data list to the JSON file specified by file_path
            json.dump(recipes_data, file, indent=4) # Indentation for readability
        print(f"\nRecipe book has been successfully updated.")
    # Error handling
    except PermissionError:
        print(f"\nPermission denied to write file.")
    except json.JSONDecodeError:
        print(f"\nError encoding JSON data to file.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}.")