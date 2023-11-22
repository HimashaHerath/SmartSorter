import shutil
import os

def move_files(categorized_files, destination):
    """
    Moves files to their new destination.
    
    Args:
        categorized_files (dict): Categorized files.
        destination (str): Base destination directory.
    """
    for category, files in categorized_files.items():
        category_path = os.path.join(destination, category)
        os.makedirs(category_path, exist_ok=True)
        for file in files:
            shutil.move(file, category_path)
