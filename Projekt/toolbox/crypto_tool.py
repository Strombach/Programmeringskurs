import argparse
import key_generator
from cryptography.fernet import Fernet

def encrypt_data(data, key):
    print("Encrypting data...")
    
    cipher_suite = Fernet(key)

    cipher_data = cipher_suite.encrypt(data.encode())
    return cipher_data

def decrypt_data(data, key):
    print("Decrypting data...")

    cipher_suite = Fernet(key)

    plain_data = cipher_suite.decrypt(data)
    return plain_data

def main():
    parser = argparse.ArgumentParser(description="Crypto tool", usage='%(prog)s -f [file to encrypt or decrypt] [options]')
    
    # Mandatory flag
    parser.add_argument("-f", "--file", help="The file to encrypt or decrypt.", required=True)
    
    # Default options
    parser.add_argument("-nk", "--newkey", action="store_false", help="Create a new file so encrypt/decrypt other files with.")
    parser.add_argument("-e", "--encrypt", action="store_false", help="If the script should encrypt a file.")
    
    # Optional
    parser.add_argument("-k", "--key", help="If you got a key file to encrypt with, use this flag.")
    parser.add_argument("-dk", "--decryptkey", help="Key file to decrypt with.")
    
    args = parser.parse_args()

    # Finding "content file".
    try:
        if args.decryptkey:
            with open(args.file, "rb") as content_file:
                content = content_file.read()
        else:    
            with open(args.file, "r") as content_file:
                content = content_file.read()
    except FileNotFoundError:
        print("The file to encrypt/decrypt couldn't be found")
        exit()

    # Create or find the key.
    try:
        if args.newkey and not args.key and not args.decryptkey:
            key_name = input("Name the key (Default [secret].key): ")
            print("Generating new key.")
            key_file = key_generator.generate_key(key_name)
        else:
            if args.key or args.decryptkey:
                key_file = args.key or args.decryptkey
            else:
                raise Exception("Need to enter a key file (-k, --key).")

        with open(key_file, "rb") as key_file:
            key = key_file.read()
    except FileNotFoundError:
        print("The key file couldn't be found.")
        exit()
    except Exception as err:
        print(err)
        exit()

    try:
        if args.encrypt and not args.decryptkey:
            encrypted_data = encrypt_data(content, key)

            with open(f"{args.file}.enc", "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
        else:
            decrypted_data = decrypt_data(content, key)

            with open(f"decrypted_data.txt", "w") as decrypted_file:
                decrypted_file.write(decrypted_data.decode())
    except Exception as err:
        print(err)
        print("Couldn't save to file")

if __name__ == "__main__":
    main()
