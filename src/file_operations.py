import json
from recipe_operations import RecipeManager

def load_recipe(file_path):
    # Import pre-saved recipes from a JSON file.
    manager = RecipeManager()
    
    try:
        with open(file_path, 'r') as file:
            recipes_data = json.load(file)

        if recipes_data:
            manager.import_recipes_json(recipes_data)

        return manager

    except FileNotFoundError:
        print(f"\nFile not found. Please check if {file_path} exists.")
        return []
    except PermissionError:
        print(f"\nPermission denied to read file.")
        return []
    except json.decoder.JSONDecodeError as e:
        print(f"\nError decoding JSON in {file_path}: {e}.")
        return []
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}.")
        return []
    
def save_recipe(file_path, manager):
    try:
        recipes_data = []

        for recipe in manager.recipes:
            recipe_data = {
                'name': recipe.name,
                'cuisine': recipe.cuisine,
                'ingredients': recipe.ingredients,
                'instructions': recipe.instructions
            }
            recipes_data.append(recipe_data)

        with open(file_path, 'w') as file:
            json.dump(recipes_data, file, indent=4)

        print(f"\nRecipe book has been successfully updated.")
    except PermissionError:
        print(f"\nPermission denied to write file.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}.")