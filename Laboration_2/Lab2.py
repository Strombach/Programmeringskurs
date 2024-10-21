import argparse
import key_generator
from cryptography.fernet import Fernet

def encrypt_data(data, key):
    print("Encrypting data...")
    
    cipher_suite = Fernet(key)

    cipher_data =  cipher_suite.encrypt(data)
    return cipher_data

def decrypt_file(file, key):
    print(f"Decrypt: {file} with {key}")

def main():
    parser = argparse.ArgumentParser(description="Crypto tool", usage='%(prog)s -f [file to encrypt or decrypt] [options]')
    
    # Mandatory flag
    parser.add_argument("-f", "--file", help="The file to encrypt or decrypt.", required=True)
    
    # Default options
    parser.add_argument("-nk", "--newkey", action="store_false", help="Create a new file so encrypt/decrypt other files with.")
    parser.add_argument("-e", "--encrypt", action="store_false", help="If the script should encrypt a file.")
    
    # Optional
    parser.add_argument("-k", "--key", help="The keyfile to encrypt/decrypt with.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="If the script should decrypt a file.")
    
    args = parser.parse_args()

    # Finding "content file".
    try:
        with open(args.file, "rb") as content_file:
            content = content_file.read().strip()
    except FileNotFoundError:
        print("The file to encrypt/decrypt couldn't be found")
        exit()

    # Create or find the key.
    try:
        if args.newkey and not args.key:
            key_name = input("Name the key (Default [secret].key): ")
            print("Generating new key.")
            key_file = key_generator.generate_key(key_name)
        else:
            key_file = args.key

        with open(key_file, "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        print("The key file couldn't be found.")
        exit()

    try:
        if args.encrypt and not args.decrypt:
            encrypted_data = encrypt_data(content, key)

            with open(f"{args.file}.enc", "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
        else:
            decrypt_file(content, key)
    except Exception:
        print("Couldn't save to file")

if __name__ == "__main__":
    main()
