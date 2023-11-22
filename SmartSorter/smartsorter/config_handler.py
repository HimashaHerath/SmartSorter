import json

def load_config(file_path):
    """
    Loads the configuration file.
    
    Args:
        file_path (str): The path to the configuration file.
    
    Returns:
        dict: The configuration settings.
    """
    with open(file_path, 'r') as file:
        return json.load(file)