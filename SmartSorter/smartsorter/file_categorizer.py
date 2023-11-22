def categorize_files(files, rules):
    """
    Categorizes files based on provided rules.
    
    Args:
        files (list): List of file paths.
        rules (dict): Categorization rules from the config.
    
    Returns:
        dict: Categorized files.
    """
    categorized = {}
    for file in files:
        extension = file.split('.')[-1]
        if extension in rules:
            category = rules[extension]
            if category not in categorized:
                categorized[category] = []
            categorized[category].append(file)
    return categorized
