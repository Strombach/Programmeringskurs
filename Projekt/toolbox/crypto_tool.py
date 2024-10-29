import argparse
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

def main(flags):

    # Finding "content file".
    try:
        if flags.decryptkey:
            with open(flags.file, "rb") as content_file:
                content = content_file.read()
        else:
            with open(flags.file, "r") as content_file:
                content = content_file.read()
    except FileNotFoundError:
        print("The file to encrypt/decrypt couldn't be found")
        exit()

    # Create or find the key.
    try:
        if flags.newkey and not flags.key and not flags.decryptkey:
            key_file = generate_key()
        else:
            if flags.key or flags.decryptkey:
                key_file = flags.key or flags.decryptkey
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

    # Encrypt or decrypt data and save to file.
    try:
        if flags.encrypt and not flags.decryptkey:
            encrypted_data = encrypt_data(content, key)

            with open(f"{flags.file}.enc", "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
        else:
            decrypted_data = decrypt_data(content, key)

            with open(f"decrypted.txt", "w") as decrypted_file:
                decrypted_file.write(decrypted_data.decode())
    except Exception as err:
        print(err)
        print("Couldn't save to file")

if __name__ == "__main__":

    from key_generator import generate_key

    parser = argparse.ArgumentParser(description="Crypto tool", usage='%(prog)s -f [file to encrypt or decrypt] [options]')

    # Mandatory flag
    parser.add_argument("-f", "--file", help="The file to encrypt or decrypt.", required=True)

    # Default options
    parser.add_argument("-nk", "--newkey", action="store_false", help="Create a new file so encrypt/decrypt other files with.")
    parser.add_argument("-e", "--encrypt", action="store_false", help="If the script should encrypt a file.")

    # Optional
    parser.add_argument("-k", "--key", help="If you got a key file to encrypt with, use this flag.")
    parser.add_argument("-dk", "--decryptkey", help="Key file to decrypt with.")

    argparse_args = parser.parse_args()

    main(argparse_args)
else:
    import os
    from .args import Crypto_Args
    from .key_generator import generate_key

    def crypto_tool():
        os.system("clear")
        newkey = False
        decryptkey = None
        existingkey = None

        while True:
            data_file = input("What file to encrypt/decrypt: ")
            if not os.path.isfile(data_file):
                print("File not found")
                continue
            else:
                break

        while True:
            decrypt_or_encrypt = input("Encrypt or decrypt [e/d]: ")
            if decrypt_or_encrypt == "e":
                encrypt = True
                break
            elif decrypt_or_encrypt == "d":
                encrypt = False
                break
            else:
                continue

        if encrypt:
            while True:
                print("Test1")
                newkey_or_existingkey = input("Create a new key? [y/n]: ")
                if newkey_or_existingkey == "y":
                    newkey = True
                    break
                elif newkey_or_existingkey == "n":
                    newkey = False
                    break
                else:
                    continue


        while True:
            if not encrypt:
                decryptkey = input("What key to decrypt with?: ")
            elif encrypt and not newkey:
                existingkey = input("What key to encrypt with?: ")

            if not newkey and not os.path.isfile(existingkey or decryptkey):
                print("File not found")
                continue
            else:
                break


        args = Crypto_Args(file=data_file,encrypt=encrypt,decryptkey=decryptkey,newkey=newkey,key=existingkey)

        main(args)
