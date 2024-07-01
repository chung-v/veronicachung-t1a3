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

        return manager, recipes_data

    except FileNotFoundError:
        print(f"File not found. Please check if {file_path} exists.")
        return []
    except PermissionError:
        print(f"Permission denied to read file.")
        return []
    except json.decoder.JSONDecodeError as e:
        print(f"Error decoding JSON in {file_path}: {e}.")
        return []
    except Exception as e:
        print(f"Unexpected error occurred: {e}.")
        return []
    
def save_recipe(file_path, manager):
    try:
        with open(file_path, 'w') as file:
            json.dump(manager, file, indent=4)
        print(f"Recipe successfully saved to {file_path}.")
    except PermissionError:
        print(f"Permission denied to write file.")
    except Exception as e:
        print(f"Unexpected error occurred: {e}.")