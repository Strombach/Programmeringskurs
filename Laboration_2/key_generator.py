from cryptography.fernet import Fernet

def generate_key(name = None):
    key = Fernet.generate_key()
    
    if name:
        key_name = name
    else:
        key_name = "secret"
    
    with open(f"{key_name}.key", "wb") as key_file:
        key_file.write(key)
    print(f"{key_name}.key is now created and saved.")

    return f"{key_name}.key"

if __name__ == "__main__":
    generate_key()
