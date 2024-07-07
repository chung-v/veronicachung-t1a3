import json
from recipe_operations import Recipe
from rich import print

# Function to import pre-saved recipes from JSON file.
def load_recipe(file_path, manager):
    try:
        # Loads JSON data from the file into recipes_data list
        with open(file_path, 'r') as file:
            recipes_data = json.load(file)
            for recipe_data in recipes_data:
                # Creates a Recipe object using data from JSON
                recipe = Recipe(
                    recipe_data['name'],
                    recipe_data['cuisine'],
                    recipe_data['ingredients'],
                    recipe_data['instructions']
                    )
                manager.recipes.append(recipe)
        return manager
    # Emphasise error handling message in red using rich
    except FileNotFoundError:
        print(f"[red3]\nFile not found. Please check if file exists.[/]")
        return []
    except PermissionError:
        print(f"[red3]\nPermission denied to read file.[/]")
        return []
    except json.JSONDecodeError:
        print(f"[red3]\nError decoding JSON from file.[/]")
        return []
    except Exception as e:
        print(f"[red3]\nUnexpected error occurred: {e}.[/]")
        return []

# Function to export recipe updates to JSON file
def save_recipe(file_path, manager):
    try:
        recipes_data = []
        for recipe in manager.recipes:
            #  Creates a dictionary representing each recipe's data
            recipe_data = {
                'name': recipe.name,
                'cuisine': recipe.cuisine,
                'ingredients': recipe.ingredients,
                'instructions': recipe.instructions
            }
            recipes_data.append(recipe_data)
        # Write recipes_data list to the JSON file specified by file_path
        with open(file_path, 'w') as file:
            json.dump(recipes_data, file, indent=4) # Indentation for readability
        print(f"\nRecipe book has been successfully updated.")
    # Emphasise error handling message in red using rich
    except PermissionError:
        print(f"[red3]\nPermission denied to write file.[/]")
    except json.JSONDecodeError:
        print(f"[red3]\nError encoding JSON data to file.[/]")
    except Exception as e:
        print(f"[red3]\nUnexpected error occurred: {e}.[/]")