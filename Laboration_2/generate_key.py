from cryptography.fernet import Fernet

def generate_key(name = None):
    key_name = "secret"
    key = Fernet.generate_key()
    
    if name:
        key_name = name
    
    with open(f"{key_name}.key", "wb") as key_file:
        key_file.write(key)
    print(f"{key_name}.key is now created and saved.")
