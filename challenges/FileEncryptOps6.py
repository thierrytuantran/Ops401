from cryptography.fernet import Fernet
import os

# Generate a key and instantiate a Fernet object
def generate_key():
    key = Fernet.generate_key()
    with open('encryption.key', 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open('encryption.key', 'rb') as key_file:
        return key_file.read()

# Call generate_key only if 'encryption.key' does not exist
if not os.path.exists('encryption.key'):
    generate_key()

key = load_key()
cipher_suite = Fernet(key)
def encrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    with open(file_path, 'wb') as file:
        file.write(encrypted_data)
def load_key():
    with open('encryption.key', 'rb') as key_file:
        return key_file.read()
def decrypt_file(file_path):
    key = load_key()
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

def encrypt_message(message):
    cipher_suite = Fernet(key)  # Use the already loaded key
    encrypted_message = cipher_suite.encrypt(message.encode()).decode()
    return encrypted_message

def decrypt_message(ciphertext):
    cipher_suite = Fernet(key)  # Use the already loaded key
    decrypted_message = cipher_suite.decrypt(ciphertext.encode()).decode()
    return decrypted_message

def main():
    mode = input("Select a mode:\n1. Encrypt a file\n2. Decrypt a file\n3. Encrypt a message\n4. Decrypt a message\n")
    
    if mode == '1':
        file_path = input("Enter the filepath to encrypt: ")
        encrypt_file(file_path)
        print("File encrypted successfully.")

    elif mode == '2':
        file_path = input("Enter the filepath to decrypt: ")
        decrypt_file(file_path)
        print("File decrypted successfully.")

    elif mode == '3':
        message = input("Enter the message to encrypt: ")
        encrypted_message = encrypt_message(message)
        print(f"Encrypted Message: {encrypted_message}")

    elif mode == '4':
        ciphertext = input("Enter the ciphertext to decrypt: ")
        decrypted_message = decrypt_message(ciphertext)
        print(f"Decrypted Message: {decrypted_message}")

    else:
        print("Invalid mode selected.")

if __name__ == "__main__":
    main()
