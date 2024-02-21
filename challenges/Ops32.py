import os
import platform
import hashlib
import time

def search_files(directory):
    # Initialize counters for searched files and hits
    files_searched = 0
    hits_found = 0

    # Perform platform-specific commands
    if platform.system() == "Windows": # For Windows
        command = f'dir /s /b /a-d "{directory}"'
    else:  # For Linux
        command = f'find "{directory}" -type f'

    # Execute command and process output
    output = os.popen(command).read()
    file_paths = output.strip().split('\n')
    for file_path in file_paths:
        # Calculate MD5 hash
        md5_hash = hashlib.md5()
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                md5_hash.update(chunk)
        md5_digest = md5_hash.hexdigest()

        # Get file information
        file_info = os.stat(file_path)
        file_name = os.path.basename(file_path)
        file_size = file_info.st_size
        file_timestamp = time.ctime(file_info.st_mtime)

        # Print file details
        print(f"File Path: {file_path}")
        print(f"File Name: {file_name}")
        print(f"File Size: {file_size} bytes")
        print(f"Timestamp: {file_timestamp}")
        print(f"MD5 Hash: {md5_digest}\n")
        
        # Update counters
        files_searched += 1
        hits_found += 1

    # Print search statistics
    print(f"\nFiles searched: {files_searched}")
    print(f"Hits found: {hits_found}")

if __name__ == "__main__":
    # Prompt user for directory to search
    directory = input("Enter the directory to search in: ")

    # Call the function to search files
    search_files(directory)
