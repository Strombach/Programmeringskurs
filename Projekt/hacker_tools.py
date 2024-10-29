import os
from toolbox import crypto_tool
from toolbox import domenus

while True:
    os.system('clear')
    print("""
    Hacker Tools
    1. Crypto Tool
    2. DomEnus
    0. Exit
    """)
    menu_choice = input("What app to use?: ")

    match(menu_choice):
        case("1"):
            crypto_tool.crypto_tool()
        case("2"):
            domenus.main()
        case("0"):
            exit()
        case _:
            print("Not a valid option.")
