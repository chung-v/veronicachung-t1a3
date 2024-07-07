import json
from recipe_operations import Recipe

FILE_PATH = '../data/recipes.json'

# Import pre-saved recipes from JSON file.
def load_recipe(file_path, manager):
    try:
        with open(file_path, 'r') as file:
            recipes_data = json.load(file)

            for recipe_data in recipes_data:
                recipe = Recipe(recipe_data['name'], recipe_data['cuisine'], recipe_data['ingredients'], recipe_data['instructions']) #
                manager.recipes.append(recipe)

        return manager

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

# Export recipe updates to JSON file
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
    except json.JSONDecodeError:
        print(f"\nError encoding JSON data to file.")
    except Exception as e:
        print(f"\nUnexpected error occurred: {e}.")