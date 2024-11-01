import os
import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

HELP_STRING = """
        WebGetter
        Using requests and BeutifulSoup WebGetter copies a webpage and
        rewrites all ```<img>,<link>,<script>``` so that src and href
        attributes points to a local downloaded folder. This is so
        that the page should copy look and some functionality when
        running offline.
        """

def main(flags):

    if flags.name:
        download_name = flags.name
    else:
        download_name = "downloaded"

    response = requests.get(flags.url)

    if response.status_code == 200:
        print(f"{flags.url} was found.")

        soup = BeautifulSoup(response.content, "html.parser")

        asset_dir = f"{download_name}_assets"
        os.makedirs(asset_dir, exist_ok=True)

        for tag in soup.find_all(["img", "link", "script"]):
            if tag.name == "img" or tag.name == "script":
                asset_attribute = "src"
            else:
                asset_attribute = "href"

            asset_url = tag.get(asset_attribute)

            if asset_url:
                asset_url = urljoin(flags.url, asset_url)
                asset_name = os.path.basename(urlparse(asset_url).path)

                asset = requests.get(asset_url)
                if asset.status_code == 200:
                    with open(f"{download_name}_assets/{asset_name}", "wb") as asset_file:
                        asset_file.write(asset.content)
                    print(f"Downloaded asset: {asset_name}")

                    tag[asset_attribute] = os.path.join(asset_dir, asset_name)
                else:
                    print(f"Failed to find: {asset_url}")

        with open(f"{download_name}_index.html", "w", encoding="utf-8") as html_file:
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

    # Optional
    parser.add_argument("-n","--name", help="Name for the downloaded file")

    args = parser.parse_args()

    main(args)
else:
    from .args import Webgetter_args

    def webgetter():
        args = Webgetter_args()

        main(args)
