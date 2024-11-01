from bs4 import BeautifulSoup

with open("app.js", "r") as js_file:
    js_script = js_file.read()

def main():
    with open("index.html", "r", encoding="utf-8") as original_file:
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
