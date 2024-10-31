import os
import argparse
import requests
from bs4 import BeautifulSoup

HELP_STRING = """
        Wgetter
        """

def main(flags):

    response = requests.get(flags.url)

    if response.status_code == 200:
        print(f"{flags.url} was found.")
    else:
        print(f"Can't reach {flags.url}.")

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="Wgetter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description= HELP_STRING
)

    # Mandatory
    parser.add_argument("-u","--url", help="The URL to the webpage to download.")

    args = parser.parse_args()

    main(args)
