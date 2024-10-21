import argparse
import key_generator

def generate_new_key(name=""):
    print("Generating new key")
    key_generator.generate_key(name)

def encrypt_file(file, key):
    print(f"Encrypt: {file} with {key}")

def decrypt_file(file, key):
    print(f"Decrypt: {file} with {key}")

def main():
    parser = argparse.ArgumentParser(description="Crypto tool", usage='%(prog)s [options]')
    
    parser.add_argument("-f", "--file", help="The file to encrypt or decrypt.")
    parser.add_argument("-k", "--key", help="The keyfile to encrypt/decrypt with.")
    parser.add_argument("-e", "--encrypt", action="store_true", help="If the script should encrypt a file.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="If the script should decrypt a file.")
    parser.add_argument("-nk", "--newkey", action="store_true", help="Create a new file so encrypt/decrypt other files with.")
    
    args = parser.parse_args()

    key = None

    if not args.key and not args.newkey:
        print("You need to use a file to encrypt/decrypt a file.")
    else:
        try:
            if args.newkey:
                key_name = input("Name the key (Default [secret].key): ")
                key_file = generate_new_key(key_name)
            
            with open(args.key, "rb") as key_file:
                key = key_file.read()
            print(key)
        except FileNotFoundError:
            print("The file couldn't be found.")

if __name__ == "__main__":
    main()
