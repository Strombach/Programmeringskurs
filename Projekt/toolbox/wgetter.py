import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

HELP_STRING = """
        Wgetter
        """

def main(flags):

    response = requests.get(flags.url)

    if response.status_code == 200:
        print(f"{flags.url} was found.")

        soup = BeautifulSoup(response.content, "html.parser")

        asset_dir = "downloaded_assets"
        os.makedirs(asset_dir)

        for tag in soup.find_all(["img", "link", "script"]):
            if tag.name == "img" or tag.name == "script":
                asset_url = tag.get("src")
            else:
                asset_url = tag.get("href")

            if asset_url:
                asset_url = urljoin(flags.url, asset_url)
                asset_name = os.path.basename(urlparse(asset_url).path)
                print(asset_url)
                print(asset_name)

                asset = requests.get(asset_url)
                if asset.status_code == 200:
                    print("Found asset")
                    with open(f"downloaded_assets/{asset_name}", "wb") as asset_file:
                        asset_file.write(asset.content)
                    print(f"Downloaded asset: {asset_name}")

                    tag["src"] = os.path.join(asset_dir, asset_name)
                else:
                    print(f"Failed to find: {asset_url}")

        with open("downloaded_page.html", "w", encoding="utf-8") as html_file:
            html_file.write(soup.prettify())
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
