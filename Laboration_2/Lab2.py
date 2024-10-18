import argparse
import generate_key

def generate_new_key():
    generate_key.generate_key()
    print("Generating new key")

def encrypt_file(file, key):
    print(f"Encrypt: {file} with {key}")

def decrypt_file(file, key):
    print(f"Decrypt: {file} with {key}")

if __name__ == "__main__":
    main()