import argparse
import generate_key

def generate_new_key(name=""):
    print("Generating new key")
    generate_key.generate_key(name)

def encrypt_file(file, key):
    print(f"Encrypt: {file} with {key}")

def decrypt_file(file, key):
    print(f"Decrypt: {file} with {key}")

def main():
    parser = argparse.ArgumentParser(description="Crypto tool", usage='%(prog)s [options]')
    parser.add_argument("-e", "--encrypt", action="store_true", help="If the script should encrypt a file.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="If the script should decrypt a file.")
    parser.add_argument("-nf", "--newfile", action="store_true", help="Create a new file so encrypt/decrypt other files with.")
    parser.add_argument("-f", "--file", help="The file to encrypt/decrypt with.")
    
    args = parser.parse_args()

    if not args.file and not args.newfile:
        print("You need to use a file to encrypt/decrypt a file.")
    else:
        try:
            if args.newfile:
                key_name = input("Name the key. Default [secret].key")
            else:
                file = open(args.file, "rb")
        except FileNotFoundError:
            print("The file couldn't be found.")

if __name__ == "__main__":
    main()
