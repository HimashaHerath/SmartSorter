import os

def scan_directory(directory_path):
    """
    Scans a directory and lists all files.
    
    Args:
        directory_path (str): Path to the directory.
    
    Returns:
        list: List of file paths.
    """
    files = []
    for root, _, filenames in os.walk(directory_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files
