from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    
    name_input = input("Name the key (Default [secret].key): ")

    if name_input:
        key_name = name_input
    else:
        key_name = "secret"
    
    print("Generating new key.")
    
    with open(f"{key_name}.key", "wb") as key_file:
        key_file.write(key)
    print(f"{key_name}.key is now created and saved.")

    return f"{key_name}.key"

if __name__ == "__main__":
    generate_key()
