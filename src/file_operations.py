import json

def load_recipe(file_path):
    # Load pre-saved recipes from a JSON file.
    try:
        with open(file_path, 'r') as file:
            manager = json.load(file)
        return manager
    except FileNotFoundError:
        print(f"File not found. Please check if {file_path} exists.")
        return []
    except PermissionError:
        print(f"Permission denied to read file.")
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