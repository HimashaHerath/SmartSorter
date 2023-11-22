import sys
sys.path.append('../')

from smartsorter.config_handler import load_config
from smartsorter.file_scanner import scan_directory
from smartsorter.file_categorizer import categorize_files
from smartsorter.file_mover import move_files

def main():
    if len(sys.argv) < 2:
        print("Usage: smartsorter <config_file>")
        sys.exit(1)

    config_file = sys.argv[1]
    config = load_config(config_file)
    
    files = scan_directory(config["scan_directory"])
    categorized_files = categorize_files(files, config["rules"])
    move_files(categorized_files, config["destination_directory"])

if __name__ == "__main__":
    main()
