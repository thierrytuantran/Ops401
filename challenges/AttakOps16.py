import time

def offensive_mode(wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            for word in file:
                print(word.strip())
                # Add a short delay
    except FileNotFoundError:
        print("File not found. Please check the file path.")

def defensive_mode(password, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            for word in file:
                if word.strip() == password:
                    print("Password found.")
                    return
            print("Password not found.")
    except FileNotFoundError:
        print("File not found. Check the file path.")

def main():
    mode = input("Choose mode (1 for Offensive, 2 for Defensive): ")
    wordlist_path = input("Enter word list file path: ")

    if mode == '1':
        offensive_mode(wordlist_path)
    elif mode == '2':
        password = input("Enter the password to check: ")
        defensive_mode(password, wordlist_path)
    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
