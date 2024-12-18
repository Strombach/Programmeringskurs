import os
import pyfiglet
from toolbox import crypto_tool, domenus, webgetter,smuggler

def create_title(text):
    return pyfiglet.figlet_format(text)

while True:
    os.system('clear')
    print(create_title("Hacker Toolbox"))
    print("""
1. Crypto Tool
2. DomEnus
3. WebGetter
4. Smuggler
---
9. Help
0. Exit
""")

    menu_choice = input("What app to use?: ")

    match(menu_choice):
        case("1"):
            os.system("clear")
            print(create_title("Cryptos"))
            crypto_tool.crypto_tool()
        case("2"):
            os.system("clear")
            print(create_title("DomEnus"))
            domenus.domenus()
        case("3"):
            os.system("clear")
            print(create_title("WebGetter"))
            webgetter.webgetter()
        case("4"):
            os.system("clear")
            print(create_title("Smuggler"))
            smuggler.smuggler()
        case("0"):
            exit()
        case _:
            print("Not a valid option.")
