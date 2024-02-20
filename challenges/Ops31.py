import os
import platform

def search_files():
    # Prompt user for file name and directory to search
    file_name = input("Enter the file name to search for: ")
    directory = input("Enter the directory to search in: ")

    # Initialize counters for searched files and hits
    files_searched = 0
    hits_found = 0

    # Perform platform-specific commands
    if platform.system() == "Windows": # For Windows
        command = f'dir /s /b /a-d "{directory}\\{file_name}"'
    else:  # For Linux
        command = f'find "{directory}" -type f -name "{file_name}"'

    # Execute command and process output
    output = os.popen(command).read()
    file_paths = output.strip().split('\n')
    for file_path in file_paths:
        print(f"Found: {file_path}")
        hits_found += 1

    # Count searched files
    files_searched = len(file_paths)

    # Print search statistics
    print(f"\nFiles searched: {files_searched}")
    print(f"Hits found: {hits_found}")

if __name__ == "__main__":
    search_files()
