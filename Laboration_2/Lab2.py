import argparse
import key_generator

def encrypt_file(file, key):
    print(f"Encrypt: {file} with {key}")

def decrypt_file(file, key):
    print(f"Decrypt: {file} with {key}")

def main():
    parser = argparse.ArgumentParser(description="Crypto tool", usage='%(prog)s [options]')
    
    # Mandatory flag
    parser.add_argument("-f", "--file", help="The file to encrypt or decrypt.", required=True)
    
    # Default options
    parser.add_argument("-nk", "--newkey", action="store_false", help="Create a new file so encrypt/decrypt other files with.")
    parser.add_argument("-e", "--encrypt", action="store_false", help="If the script should encrypt a file.")
    
    # Optional
    parser.add_argument("-k", "--key", help="The keyfile to encrypt/decrypt with.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="If the script should decrypt a file.")
    
    args = parser.parse_args()

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
        print("The file couldn't be found.")
    
    print(key)

if __name__ == "__main__":
    main()
